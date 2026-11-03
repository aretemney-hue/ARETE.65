# ARETE EDITOR — Architecture Baseline

## Architectural direction
ARETE EDITOR is planned as a modular hybrid application:
- Python owns application orchestration, UI integration, project workflows, and most feature logic.
- PySide6 provides the desktop UI.
- FFmpeg/FFprobe and PyAV provide media inspection and processing capabilities.
- C++ is reserved for measured performance bottlenecks, exposed through stable Python bindings where appropriate.
- SQLite and a versioned native project format support durable project state.
- GPU paths are optional capabilities with explicit detection and CPU fallback.

This is a target architecture, not a description of already implemented code. The current repository baseline has not yet demonstrated an application implementation.

## Proposed dependency boundaries
- `app/core`: lifecycle, configuration, logging, event contracts, errors.
- `app/media`: media discovery, probing, indexing, thumbnails, proxies, relinking.
- `app/timeline`: timebase, tracks, clips, edit operations, undo/redo.
- `app/playback`: decoder orchestration, frame scheduling, preview cache, synchronization.
- `app/audio`: audio decode, waveform, mixing, meters and effects.
- `app/effects`: effect graph, transitions, masks and keyframes.
- `app/color`: grading parameters, LUT handling and scopes.
- `app/export`: render graph, queue, encoding, progress and logs.
- `app/ai`: optional local inference and AI-assisted editing workflows.
- `app/plugins`: plugin discovery, API and compatibility.
- `app/ui`: PySide6 windows, panels, commands and view models.
- `native`: only profiled C++ components; do not create empty native modules.
- `tests`: unit, integration and regression tests.

Modules should be created when implemented; empty directories and placeholder packages are not deliverables.

## Data-flow principles
1. UI actions invoke application/domain services rather than implementing media logic in widgets.
2. Media probing and expensive operations run outside the UI thread.
3. Timeline time is represented using an explicit timebase/frame rate; avoid floating-point drift for frame-accurate operations.
4. Project state is serialized through a versioned schema with migration strategy.
5. Decoded frames and proxies use bounded caches; full source files are never loaded into RAM.
6. Playback and rendering must use real media pipelines and report errors.
7. Hardware acceleration is selected only after capability checks and can fall back to CPU.
8. Third-party engines are integrated through documented interfaces, with license obligations recorded.

## Decisions still requiring implementation-time validation
- Whether MLT should be used as a central timeline/render engine or only evaluated as an alternative.
- Exact FFmpeg distribution/build and its enabled codecs and license implications.
- PyAV/FFmpeg version compatibility on Windows and Python 3.12.
- Qt multimedia versus an FFmpeg/PyAV-backed custom preview path.
- OpenGL rendering scope and whether a separate GPU processing layer is justified.
- Native C++ boundaries based on profiling rather than premature optimization.

## Current verified state
At initial setup, only the repository README was confirmed. No application modules, tests, dependency manifests, or runtime behavior have yet been verified in this repository. Update this section only after inspection and execution.
