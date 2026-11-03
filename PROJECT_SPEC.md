# ARETE EDITOR — Project Specification

## Product identity
ARETE EDITOR is an independent, professional, local-first nonlinear video editor for Windows 11 x64. It aims to combine approachable workflows with advanced editing capabilities and a modular architecture that can evolve into a commercial application.

The product's source code and project intellectual property belong to ARETE EDITOR. Third-party dependencies remain subject to their own licenses.

## Target development machine
- OS: Windows 11 64-bit
- CPU: Intel Core i7-13650HX
- GPU: NVIDIA RTX 3050 Laptop GPU, 6GB VRAM
- RAM: 24GB
- Storage: SSD + HDD

## Performance requirements
- Efficient memory management and bounded caches.
- Never load entire video files into RAM.
- Proxy workflows for demanding media.
- Background media processing without blocking the UI.
- Avoid unnecessary frame copies.
- Configurable hardware acceleration with graceful CPU fallback.
- Do not assume every codec supports hardware decoding or encoding.
- Benchmark before making performance claims.

## Intended technology stack
| Area | Technology |
|---|---|
| Application/core | Python 3.12 |
| Desktop UI | PySide6 |
| Persistence | SQLite plus versioned native project format |
| Numeric processing | NumPy |
| Media inspection and processing | FFmpeg / FFprobe |
| Python media access | PyAV |
| Graphics | OpenGL where justified |
| Native performance | C++, CMake, pybind11 |
| Optional local AI | Ollama and local speech recognition |

Dependencies must be selected deliberately, with compatibility, licensing, and fallback documented.

## Product modules
1. Application Core — lifecycle, configuration, events, logging, errors, dependency checks.
2. Media Engine — import video/audio/images, metadata, thumbnails, indexing, proxies, missing-media detection and relinking.
3. Timeline Engine — multiple video/audio tracks, clip positioning, split/trim, ripple/roll/slip/slide, snapping, zoom/scroll, track controls, nested sequences, undo/redo, frame-accurate timing.
4. Playback Engine — real decoding, frame-accurate seeking, playback, scrubbing, synchronization, preview quality, caching.
5. Audio Engine — decoding, waveforms, mixing, volume automation, meters, EQ, effects, noise reduction, synchronization.
6. Effects Engine — effects, transitions, transform, crop, blur, sharpen, masks, opacity, keyframes, effect stacking.
7. Color Engine — wheels, curves, exposure, contrast, saturation, white balance, LUTs, scopes, non-destructive grading.
8. Rendering Engine — export queue, H.264/H.265 and supported ProRes workflows, resolution/FPS/bitrate controls, hardware encoding with CPU fallback, progress and logs.
9. Project Engine — native project format, save/save-as, autosave, recovery, versioning, media relinking, backups.
10. AI Engine — silence detection, automatic cuts, speech-to-text, subtitles, transcript editing, scene detection, audio cleanup, AI-assisted editing, optional local agent.
11. Plugin System — discovery, loading, configuration, API, compatibility, practical isolation.

## Interface direction
- Original dark professional workspace, clean typography, high information density.
- Resizable/dockable panels, keyboard shortcuts, context menus, customizable layouts.
- Main areas: Media Browser, Source Monitor, Program Monitor, Timeline, Inspector, Effects, Audio Mixer, Color, Export.
- Long-running work must not freeze the UI.
- Do not imitate the exact visual identity of existing commercial editors.

## Engineering quality bar
A feature is complete only when its real behavior is implemented, tested, and documented. Incomplete functionality must be explicitly labeled. No fake playback/rendering, no unsupported GPU claims, no destructive changes without approval, and no unnecessary cloud dependency in the core workflow.
