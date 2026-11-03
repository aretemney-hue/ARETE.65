# ARETE EDITOR — Workspace and Interaction Specification

## Global shell
- Dark neutral interface; restrained ARETE accent colors, not a full-screen purple treatment.
- Top-level workspace switcher: MEDIA / EDIT / FUSION / COLOR / AUDIO / DELIVER.
- Shared project/media browser, command search, task monitor, transport controls, timecode display.
- Dockable/resizable panels and saved workspace layouts.
- Context-sensitive inspector and keyboard shortcut system.
- Never imitate the exact panel arrangement, iconography, or visual assets of another editor.

## EDIT workspace
- Left: project/media bins, search, metadata, proxy status.
- Center: source/program viewers with scopes and playback controls.
- Bottom: multi-track timeline, track headers, tools, snapping, markers, zoom and time ruler.
- Right: inspector, clip properties, effects stack, transitions.
- Timeline must be a real interactive widget backed by the domain model, not a text rendering.

## FUSION workspace
- Center: node graph canvas with pan/zoom, connections, selection, grouping.
- Left: node library and media pool.
- Right: parameter inspector.
- Bottom: viewer(s), keyframe/curve editor, render/cache status.
- Nodes are typed and connected; invalid connections are rejected with actionable feedback.
- First milestone is 2D compositing; 3D is a later phase.

## COLOR workspace
- Viewer plus primary wheels/controls.
- Node/grade stack, curves, qualifiers and masks as they become implemented.
- Scopes must use actual frame data.
- Color controls must be serialized and reflected in rendered output, not UI-only sliders.

## AUDIO workspace
- Multitrack audio timeline, waveforms, mixer, meters, automation and effect chain.
- Metering must reflect actual audio signal.
- Audio processing remains synchronized to sequence time.

## DELIVER workspace
- Export preset, codec/container, resolution, frame rate, quality/bitrate, audio settings.
- Hardware encoder status shown only after runtime verification.
- Render queue with real progress, cancellation, logs, and output validation.

## First usable milestone
A user can create/open a project, import media, inspect metadata, place clips on a real timeline, preview through a real backend, save/reopen, and export a basic sequence. Until this vertical slice passes, advanced panels may be planned but must not be presented as functional.
