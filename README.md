# ARETE EDITOR

**An independent, local-first nonlinear video editor for Windows 11.**

ARETE EDITOR is a long-term engineering project built around a modular Python + C++ architecture, PySide6 interface, FFmpeg/PyAV media pipeline, and optional AI-assisted workflows.

> Current state: repository setup and initial audit. Do not assume product features are implemented until they are tested and documented.

## Project principles
- Real editing, playback, and rendering — no visual-only or simulated features.
- Local-first core with optional AI/cloud integrations.
- Memory-efficient media handling and proxy workflows.
- Hardware acceleration only when detected and verified; CPU fallback is required.
- Incremental development with tests and documented evidence.

## Start here
- [Agent engineering rules](AGENTS.md)
- [Project specification](PROJECT_SPEC.md)
- [Development roadmap](ROADMAP.md)
- [Task board](TASKS.md)
- [Architecture baseline](docs/ARCHITECTURE.md)
- [Initial audit](docs/INITIAL_AUDIT.md)

## Target environment
Windows 11 x64 · Python 3.12 · PySide6 · FFmpeg/FFprobe · PyAV · C++/CMake/pybind11 where justified.

## Status
No runnable application is currently documented as verified in this repository. See the initial audit before treating any capability as available.
