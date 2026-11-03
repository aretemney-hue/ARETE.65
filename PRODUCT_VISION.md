# ARETE EDITOR — Product Vision

## Product definition
ARETE EDITOR is a unified post-production workstation: a nonlinear editor, node-based compositor, professional color workspace, and audio post-production environment in one application. It takes workflow inspiration from Premiere Pro, DaVinci Resolve, and After Effects without copying their interfaces, branding, or proprietary implementation.

This is an ambitious product target, not a statement that these capabilities already exist.

## The three creative pillars

### 1. EDIT — the Premiere-class editing experience
- Multicam-ready, multi-track video/audio timeline.
- Source and program monitors.
- Frame-accurate editing, ripple/roll/slip/slide, snapping, markers, nested sequences.
- Proxy-first workflow and background media indexing.
- Transcript-driven editing, subtitles, and reusable editing presets.

### 2. COLOR — the Resolve-class finishing experience
- Primary correction: lift/gamma/gain, offset, exposure, contrast, saturation, temperature/tint.
- Curves, wheels, qualifiers, masks, tracking, LUT management.
- Scopes: waveform, vectorscope, histogram, RGB parade.
- Color-managed pipeline with explicit working/output color spaces and bit-depth handling.
- Non-destructive node/layer grading with per-clip and group-level controls.

### 3. COMPOSITE — the After Effects-class motion/VFX experience
- Node-based compositing graph with image, transform, blend, mask, key, blur, text, shape, and color nodes.
- Layer-based motion graphics workspace for approachable animation.
- Keyframes, Bezier curves, easing, parenting, nulls, anchors, motion paths.
- 2D compositing first; 3D camera/geometry only after a stable 2D graph.
- OpenFX plug-in compatibility as a later interoperability milestone, not a promise for day one.

## Shared platform
- One project format, one media pool, one timeline/timebase, one render graph, and shared color management.
- Workspaces: Media, Edit, Fusion, Color, Fairlight-style Audio, Export.
- Custom dark ARETE visual identity, dockable panels, command search, keyboard shortcuts, workspace layouts.
- Background task manager for proxies, thumbnails, waveforms, analysis, and renders.
- Local-first operation; optional AI integrations must never be required for core editing.

## Product quality bar
- Real decode, preview, compositing, and export — no mock playback or fake render progress.
- Every effect must have a defined parameter model, serialization, preview behavior, and render behavior.
- Timeline and animation time must use rational frame/time units, not accumulated floating-point seconds.
- Every project format change needs a schema version and migration path.
- Hardware acceleration must be capability-detected and benchmarked on the target GPU.
- The app must remain useful with CPU fallback and proxy media.
- No claim of parity with commercial products until measured feature-by-feature.

## Explicit non-goals for the first release
- Reimplement every feature of all three commercial applications at once.
- Copy proprietary code, assets, icons, UI layouts, or undocumented formats.
- Promise real-time 8K, unlimited nodes, or unrestricted GPU effects on a 6GB laptop GPU.
- Ship an unverified OpenFX host or arbitrary third-party binary plug-ins in the first milestone.
