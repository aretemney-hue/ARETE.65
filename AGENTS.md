# ARETE EDITOR — Agent Engineering Rules

## Mission
Build ARETE EDITOR as a real, independent, local-first nonlinear video editor (NLE) for Windows 11 x64. This is an engineering product, not a visual-only prototype.

## Product constraints
- Product name: ARETE EDITOR.
- Primary platform: Windows 11 64-bit.
- Primary language: Python 3.12.
- UI: PySide6 with an original ARETE interface; do not copy Adobe or DaVinci branding.
- Native performance layer: C++ with CMake and pybind11 where profiling justifies it.
- Core workflow must remain local-first and usable offline.
- Target development hardware: RTX 3050 Laptop GPU 6GB, Intel Core i7-13650HX, 24GB RAM.
- Preserve memory efficiency; never load entire video files into RAM.
- GPU acceleration must be configurable and verified per codec/path; provide CPU fallback.

## Preferred technology stack
- Core: Python 3.12, PySide6, SQLite, NumPy.
- Media: FFmpeg, FFprobe, PyAV.
- Graphics: OpenGL where appropriate.
- Native: C++, CMake, pybind11.
- AI: optional local integrations (including Ollama and local speech recognition); external APIs must remain optional.

Do not add dependencies without documenting the need, compatibility, license implications, and fallback.

## Mandatory engineering rules
1. Inspect the existing repository before editing.
2. Read this file and PROJECT_SPEC.md before each task.
3. Preserve working code and backward compatibility.
4. Do not rewrite the project without a demonstrated reason.
5. Do not create empty placeholder modules.
6. Keep UI, domain logic, media processing, and persistence separated.
7. Use type hints, explicit error handling, and structured logging.
8. Add automated tests for core behavior.
9. Run relevant tests after each meaningful change and report exact commands/results.
10. Never claim a feature works unless it was executed and verified.
11. No fake playback, fake rendering, or simulated GPU claims.
12. Do not overwrite user media or delete project files without explicit approval.
13. Do not install dependencies globally; use a project virtual environment.
14. Keep the app runnable at each completed milestone.
15. Document architecture and important decisions.

## Workflow
For every task:
1. Inspect instructions, repository state, relevant source, dependencies, and tests.
2. State the implementation plan and risks before substantial changes.
3. Implement the smallest complete, testable increment.
4. Run tests and regression checks.
5. Update TASKS.md and relevant documentation.
6. Report files changed, tests run, known limitations, and next step.
7. Stop at the mission boundary and wait for user approval.

## Reporting
All user-facing reports must be in Persian (Farsi). Keep code, filenames, paths, identifiers, and commands in English. Use these headings:
- خلاصه وضعیت
- فایل‌های بررسی‌شده
- آزمایش‌ها
- مشکلات
- تغییرات
- مرحله بعد
- تأیید

## Licensing and third-party code
Do not copy third-party source code into this repository without checking its license and compatibility. Prefer documented APIs and dependencies. Record license obligations for bundled libraries and FFmpeg builds before distribution.
