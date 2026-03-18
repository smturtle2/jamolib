# Changelog

All notable changes to this project will be documented in this file.

## [0.2.0] - 2026-03-18

- Reworked Hangul text processing to use linear-time scanners instead of repeated global string replacement.
- Improved `composeHangulText` handling for common batchim boundary cases such as `값이`, `닭이`, and `읽어`.
- Added common compound-medial composition support such as `ㄱㅗㅏ -> 과`.
- Added clearer `ValueError` messages for invalid single-syllable and invalid jamo inputs.
- Expanded automated tests for mixed text and tricky composition boundaries.
- Added reproducible local benchmark script at `scripts/benchmark.py`.
- Rewrote the README with richer examples, badges, benchmark notes, and visual assets.
- Added GitHub-friendly repository docs including CI, examples, issue templates, and contribution guidance.

## [0.1.0] - 2026-03-18

- Initial public release.
