from arete.core.project import Project
from arete.timeline.engine import TimelineEngine

def make_project():
    project = Project.new(); project.fps_num, project.fps_den = 30000, 1001
    asset = project.add_media("sample.mp4", {"duration_seconds": 20, "media_type": "video"})
    first = project.add_clip(asset.id, track=0, start=0, source_in=0, duration=10)
    second = project.add_clip(asset.id, track=0, start=10, source_in=10, duration=5)
    other = project.add_clip(asset.id, track=1, start=10, source_in=0, duration=3)
    return project, first, second, other

def test_split_and_undo_redo():
    project, first, _, _ = make_project(); engine = TimelineEngine(project)
    left, right = engine.split(first.id, 150)
    lp, rp = engine.position(left), engine.position(right)
    assert lp.end_frame == rp.start_frame
    assert rp.source_in_frame == lp.source_in_frame + lp.duration_frames
    assert engine.undo() and len(project.clips) == 3
    assert engine.redo() and len(project.clips) == 4

def test_ripple_delete_is_track_local_and_undoable():
    project, first, second, other = make_project(); engine = TimelineEngine(project)
    other_start = engine.position(other).start_frame
    removed = engine.position(first).duration_frames
    engine.ripple_delete(first.id)
    assert engine.position(second).start_frame == 0
    assert engine.position(other).start_frame == other_start
    assert engine.undo()
    restored = next(c for c in project.clips if c.id == second.id)
    assert engine.position(restored).start_frame == removed

def test_trim_start_keeps_timeline_end_and_advances_source():
    project, first, _, _ = make_project(); engine = TimelineEngine(project)
    old = engine.position(first); engine.trim_start(first.id, old.start_frame + 30)
    new = engine.position(first)
    assert new.start_frame == old.start_frame + 30
    assert new.source_in_frame == old.source_in_frame + 30
    assert new.end_frame == old.end_frame

def test_invalid_split_is_non_destructive():
    project, first, _, _ = make_project(); engine = TimelineEngine(project)
    try: engine.split(first.id, 0)
    except ValueError: pass
    else: raise AssertionError("Expected split validation error")
    assert first.duration_seconds == 10
