"""Frame-accurate timeline editing operations with undo/redo snapshots."""
from __future__ import annotations
from copy import deepcopy
from dataclasses import dataclass
from fractions import Fraction
from uuid import uuid4
from arete.core.project import Project, TimelineClip
from arete.core.timebase import Timebase

@dataclass(frozen=True, slots=True)
class TimelinePosition:
    track: int
    start_frame: int
    source_in_frame: int
    duration_frames: int
    @property
    def end_frame(self) -> int:
        return self.start_frame + self.duration_frames

class TimelineEngine:
    """Edit Project clips using integer frames internally."""
    def __init__(self, project: Project, history_limit: int = 100) -> None:
        if project.fps_num <= 0 or project.fps_den <= 0:
            raise ValueError("Project frame rate must be positive")
        self.project = project
        self.timebase = Timebase(project.fps_num, project.fps_den)
        self.history_limit = max(1, history_limit)
        self._undo: list[list[TimelineClip]] = []
        self._redo: list[list[TimelineClip]] = []

    def _to_frame(self, seconds: float) -> int:
        return self.timebase.seconds_to_frames(Fraction(str(seconds)))

    def _to_seconds(self, frames: int) -> float:
        return float(self.timebase.frames_to_seconds(frames))

    def position(self, clip: TimelineClip) -> TimelinePosition:
        return TimelinePosition(clip.track, self._to_frame(clip.start_seconds),
            self._to_frame(clip.source_in_seconds), self._to_frame(clip.duration_seconds))

    def _save_undo(self) -> None:
        self._undo.append(deepcopy(self.project.clips))
        if len(self._undo) > self.history_limit: self._undo.pop(0)
        self._redo.clear()

    def _find(self, clip_id: str) -> TimelineClip:
        for clip in self.project.clips:
            if clip.id == clip_id: return clip
        raise KeyError(f"Unknown clip: {clip_id}")

    def split(self, clip_id: str, at_frame: int) -> tuple[TimelineClip, TimelineClip]:
        clip = self._find(clip_id); p = self.position(clip)
        if at_frame <= p.start_frame or at_frame >= p.end_frame:
            raise ValueError("Split point must be strictly inside the clip")
        left = at_frame - p.start_frame; right_frames = p.duration_frames - left
        self._save_undo()
        clip.duration_seconds = self._to_seconds(left)
        right = TimelineClip(str(uuid4()), clip.media_id, clip.track,
            self._to_seconds(at_frame), self._to_seconds(p.source_in_frame + left),
            self._to_seconds(right_frames))
        self.project.clips.append(right)
        return clip, right

    def trim_start(self, clip_id: str, new_start_frame: int) -> None:
        clip = self._find(clip_id); p = self.position(clip)
        delta = new_start_frame - p.start_frame
        if delta < 0 or delta >= p.duration_frames: raise ValueError("New start must be within the clip")
        self._save_undo()
        clip.start_seconds = self._to_seconds(new_start_frame)
        clip.source_in_seconds = self._to_seconds(p.source_in_frame + delta)
        clip.duration_seconds = self._to_seconds(p.duration_frames - delta)

    def trim_end(self, clip_id: str, new_end_frame: int) -> None:
        clip = self._find(clip_id); p = self.position(clip)
        duration = new_end_frame - p.start_frame
        if duration <= 0 or duration > p.duration_frames:
            raise ValueError("New end must shorten the clip without removing it")
        self._save_undo(); clip.duration_seconds = self._to_seconds(duration)

    def ripple_delete(self, clip_id: str) -> None:
        clip = self._find(clip_id); p = self.position(clip)
        self._save_undo(); self.project.clips.remove(clip)
        for other in self.project.clips:
            op = self.position(other)
            if op.track == p.track and op.start_frame >= p.end_frame:
                other.start_seconds = self._to_seconds(op.start_frame - p.duration_frames)

    def move(self, clip_id: str, *, track: int, start_frame: int) -> None:
        if track < 0 or start_frame < 0: raise ValueError("Track and start frame must be non-negative")
        clip = self._find(clip_id); self._save_undo()
        clip.track = track; clip.start_seconds = self._to_seconds(start_frame)

    def undo(self) -> bool:
        if not self._undo: return False
        self._redo.append(deepcopy(self.project.clips))
        self.project.clips = deepcopy(self._undo.pop())
        return True

    def redo(self) -> bool:
        if not self._redo: return False
        self._undo.append(deepcopy(self.project.clips))
        self.project.clips = deepcopy(self._redo.pop())
        return True
