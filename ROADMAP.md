# ARETE EDITOR — Development Roadmap

This roadmap is the intended order, not a claim that any phase is complete. Every phase requires a tested deliverable and explicit approval before moving to the next major phase.

| Phase | Scope | Status |
|---|---|---|
| 0 | Repository setup and baseline audit | In progress |
| 1 | Foundation: desktop shell, custom UI, media import, metadata, basic preview, project save/load, initial timeline model | Not started |
| 1.1 | Stabilization: audit, bug fixes, dependency verification, architecture docs, automated tests | Not started |
| 2 | Professional timeline: multitrack, drag/drop, selection, split, trim, snapping, undo/redo, track controls | Not started |
| 3 | Playback: real decoding, synchronization, seeking, scrubbing, caching, performance | Not started |
| 4 | Advanced editing: ripple/roll/slip/slide, nested sequences, keyframes | Not started |
| 5 | Audio: waveforms, mixing, automation, EQ, effects | Not started |
| 6 | Effects: transitions, masks, transform, effect stacking, animation | Not started |
| 7 | Color: wheels, curves, LUTs, scopes, color management | Not started |
| 8 | Rendering: FFmpeg pipeline, queue, hardware encoding, export profiles | Not started |
| 9 | Native performance: profile bottlenecks, C++/pybind11 optimized paths | Not started |
| 10 | GPU acceleration: memory architecture, verified hardware decode/encode, CPU fallback | Not started |
| 11 | AI editing: silence detection, transcription, subtitles, scene detection, automation | Not started |
| 12 | Plugin ecosystem: SDK, API, integrations, developer docs | Not started |
| 13 | Release: stability, performance testing, installer, documentation, release prep | Not started |

## Phase gates
- No phase is marked complete based on plans, mockups, or unexecuted code.
- Record test commands and results for each deliverable.
- Benchmark on the target hardware when performance is relevant.
- Preserve a runnable application at each completed milestone.
- Stop and request approval before starting the next major phase.
