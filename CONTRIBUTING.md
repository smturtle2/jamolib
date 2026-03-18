# Contributing

Thanks for contributing to JamoLib.

## Development Setup

```bash
python -m pip install -e .[test]
pytest -q
python scripts/benchmark.py
python -m build
```

## What To Check Before Opening A PR

- Keep public API compatibility unless the change is intentionally versioned.
- Add or update tests for Hangul edge cases and mixed-text behavior.
- If README examples change, update the matching example scripts as well.
- Run `pytest -q` and `python -m build` locally.

## Scope Guidelines

- Good contributions: performance improvements, correctness fixes, docs, examples, CI, release automation.
- Be careful with behavior changes around syllable boundaries and compatibility jamo parsing. Those changes should include explicit tests and notes in the changelog.

## Pull Request Tips

- Keep PRs focused and explain the user-visible behavior change.
- Include before/after examples when changing composition logic.
- Mention benchmark methodology if performance is part of the claim.
