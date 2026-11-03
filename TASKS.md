# ARETE EDITOR — Task Board

## Active mission: Timeline Engine Alpha

### Implemented
- [x] Repository product vision and architecture documents.
- [x] Frame-based timeline domain engine in `arete/timeline/engine.py`.
- [x] Split at an exact frame boundary while preserving source continuity.
- [x] Trim start and trim end operations.
- [x] Move clips between tracks and timeline positions.
- [x] Track-local ripple delete.
- [x] Undo / redo snapshots for timeline operations.
- [x] Timeline engine regression tests.

### Verification in this build environment
- [x] Existing starter tests: 6 passed.
- [x] Timeline engine tests: 4 passed.
- [x] Combined local suite: 10 passed.
- [ ] Verify Python 3.12 on the target Windows 11 machine.
- [ ] Install and verify PySide6 on Windows.
- [ ] Integrate timeline engine into the interactive Qt timeline UI.
- [ ] Verify media ingest against real user media and FFprobe on Windows.
- [ ] Implement and verify actual decoded video playback.
- [ ] Implement native render/export pipeline.
- [ ] Validate GPU decode/encode paths on RTX 3050; do not assume acceleration.

## Next vertical slice
1. Interactive multitrack timeline with selectable clips and frame ruler.
2. Connect split/trim/move/ripple-delete and undo/redo to UI commands.
3. Real playback backend with seek and frame-accurate playhead.
4. Export a real rendered file and compare output against expected timeline.

## Engineering constraints
- No fake playback, fake render, or unverified GPU claims.
- Preserve the current project format until a versioned migration is designed.
- Keep frame arithmetic rational/integer internally; avoid cumulative float drift.
- Test every edit operation and its undo/redo behavior.
- Do not claim Windows compatibility until tested on Windows 11 / Python 3.12.
