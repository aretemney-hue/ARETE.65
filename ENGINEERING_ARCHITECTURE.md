# ARETE EDITOR — Target Engineering Architecture

## Architecture decision
Use a custom PySide6 application and project model around a proven media engine. Evaluate MLT as the primary timeline/playback/render backend, with FFmpeg/FFprobe for codec tooling and media diagnostics. Keep the compositor and animation graph as first-class ARETE domain models; do not assume the NLE backend alone supplies an After Effects-class graph editor.

## Proposed layers

### Desktop application
- PySide6 main window, dockable workspaces, command system, shortcuts, panels.
- UI communicates with application services; widgets must not own media processing logic.
- Long-running work runs in cancellable background jobs.

### Project and domain layer
- Versioned project schema.
- Rational timebase and frame-based timeline positions.
- Media assets, bins, sequences, tracks, clips, transitions, markers, effects, keyframes, node graphs.
- Undo/redo through explicit commands and reversible state changes.
- Stable IDs and migration tests.

### Media backend
- MLT adapter for multitrack timeline playback/rendering after Windows packaging and feature validation.
- FFmpeg/FFprobe for probing, proxy/transcode, image sequence operations, waveform support, and fallback utilities.
- PyAV only where Python-level frame access is justified; avoid unnecessary frame copies.
- Backend interfaces isolate the app from any one engine.

### Compositor
- Typed directed acyclic graph (DAG): nodes declare input/output types, parameters, time dependence, and render requirements.
- Initial nodes: Footage, Image, Solid, Text, Transform, Merge, Mask, Blur, Color Correct, Crop, Output.
- Evaluation cache keyed by node state + frame + render scale.
- CPU reference implementation first; GPU execution only after profiling and validation.
- Graph serialization is part of the native project schema.

### Animation
- Frame-based keyframes, interpolation modes, Bezier easing, expression-safe parameter model.
- Shared animation curves for clip properties, effects, and compositor nodes.
- Graph editor and curve editor are separate views over the same animation data.

### Color pipeline
- Explicit pixel format, bit depth, transfer function, primaries, and working/output color spaces.
- Non-destructive grade stack and scopes.
- Avoid silently converting color spaces or claiming HDR support without end-to-end validation.

### Rendering
- Render graph compiled from sequence + effects + compositor graph.
- Queue, cancellation, progress derived from actual backend events, logs, and reproducible export settings.
- Hardware decode/encode selected only after runtime capability checks; CPU fallback is mandatory.

### Native acceleration
- C++/pybind11 only for measured hotspots: timeline evaluation, image kernels, graph scheduling, or memory-critical paths.
- Do not create a native layer before profiling.
- Keep Python API boundaries small and testable.

## Proposed repository layout
- `app/core`: lifecycle, config, commands, logging, jobs.
- `app/project`: schema, migrations, persistence, recovery.
- `app/media`: asset database, probe, thumbnails, proxies, relink.
- `app/timeline`: sequences, tracks, clips, edit operations, timebase.
- `app/playback`: backend adapter, frame scheduling, preview cache.
- `app/compositor`: graph model, nodes, evaluation, cache.
- `app/animation`: keyframes, curves, interpolation.
- `app/color`: color management, grading model, scopes.
- `app/audio`: audio graph, waveform, mixer, meters.
- `app/render`: graph compiler, queue, export profiles.
- `app/plugins`: later OpenFX discovery/host boundary.
- `app/ui`: workspaces, panels, view models.
- `native`: profiled C++ components only.
- `tests`: unit, integration, regression, golden-frame tests.

## Engine and licensing gates
- MLT is an attractive candidate because it supports multitrack media authoring, filters, transitions, serialization, bindings, and GPU-related paths. Validate the exact Windows build, Python integration, module set, and LGPL/GPL configuration before committing to distribution.
- FFmpeg licensing depends on build configuration and enabled components. Pin and audit the exact build used for development and distribution.
- OpenFX is an interoperability target for plug-ins; implementing an OFX host is a distinct engineering project and requires API, binary-loading, threading, image-format, and crash-isolation work.
- Do not copy code from GPL applications into this repository without a license review.

## Technical risks
1. MLT Windows packaging and Python binding reliability.
2. Color consistency between preview and final render.
3. GPU memory pressure on 6GB VRAM.
4. Node-graph cache invalidation and deterministic rendering.
5. Audio/video synchronization and variable-frame-rate media.
6. Plug-in crashes and ABI compatibility.
7. Project migration as features evolve.

## Validation gates
No engine is considered selected until a Windows proof-of-concept demonstrates:
- Open and inspect representative H.264/H.265 media.
- Accurate seeking and stable preview.
- Two video tracks with compositing/transition.
- Audio playback synchronized to video.
- A rendered export that matches the preview within defined tolerances.
- Clean shutdown, error reporting, and repeatable tests.
