# JamoLib

[![CI](https://github.com/smturtle2/jamolib/actions/workflows/ci.yml/badge.svg)](https://github.com/smturtle2/jamolib/actions/workflows/ci.yml)
[![PyPI](https://img.shields.io/pypi/v/jamolib.svg)](https://pypi.org/project/jamolib/)
[![Python](https://img.shields.io/pypi/pyversions/jamolib.svg)](https://pypi.org/project/jamolib/)
[![GitHub release](https://img.shields.io/github/v/release/smturtle2/jamolib?sort=semver)](https://github.com/smturtle2/jamolib/releases)

<p align="center">
  <img src="https://raw.githubusercontent.com/smturtle2/jamolib/master/docs/assets/jamolib-hero.png" alt="JamoLib hero image" width="100%">
</p>

Fast Hangul text utilities for Python.
`JamoLib` helps you decompose Hangul syllables into jamo, compose jamo back into syllables, and convert two-set Korean keyboard input into readable Korean text.

## Why JamoLib

- Linear-time text scanning for large Hangul strings.
- Small API surface that is easy to drop into search, normalization, keyboard-input, and NLP preprocessing pipelines.
- Preserves mixed text such as English, numbers, punctuation, and whitespace.
- Handles common batchim boundary cases like `값이`, `닭이`, and `읽어`.
- Supports common compound-medial combinations such as `ㄱㅗㅏ -> 과`.

<p align="center">
  <img src="https://raw.githubusercontent.com/smturtle2/jamolib/master/docs/assets/jamolib-preview.png" alt="JamoLib example preview" width="920">
</p>

## Installation

```bash
pip install jamolib
```

## Quick Start

```python
import jamolib

text = "한글과 English 123"
decomposed = jamolib.decomposeHangulText(text)

print(decomposed)
# ㅎㅏㄴㄱㅡㄹㄱㅘ English 123

print(jamolib.composeHangulText("ㄱㅏㅂㅅㅇㅣ"))
# 값이

print(jamolib.translateEngToKor("dkssudgktpdy"))
# 안녕하세요
```

## API At A Glance

| Function | Input | Output | Use case |
| --- | --- | --- | --- |
| `decomposeHangul` | Single Hangul syllable | Compatibility jamo string | Token-level preprocessing |
| `decomposeHangulText` | Mixed text | Text with Hangul syllables decomposed | Search normalization, phonetic indexing |
| `composeHangul` | `초성 + 중성 [+ 종성]` | Single Hangul syllable | Rebuilding syllables |
| `composeHangulText` | Jamo text | Re-composed Hangul text | UI input handling, postprocessing |
| `translateEngToKor` | Two-set English keyboard input | Hangul text | Keyboard typo correction |
| `getCharset` | None | Supported compatibility jamo list | Validation and custom pipelines |

## Examples

- [`examples/quickstart.py`](examples/quickstart.py): decomposition, composition, and keyboard conversion in one script
- [`examples/mixed_text.py`](examples/mixed_text.py): preserving non-Hangul text while processing Hangul
- [`examples/batchim_boundaries.py`](examples/batchim_boundaries.py): tricky batchim and syllable-boundary cases

Run an example from the repository root:

```bash
python examples/quickstart.py
```

## Notes

- `decomposeHangul` expects a single Hangul syllable.
- `composeHangul` expects compatibility jamo in the order `초성 + 중성 [+ 종성]`.
- `composeHangulText` also combines common compound medials like `ㅗㅏ`, `ㅜㅓ`, and `ㅡㅣ`.
- `translateEngToKor` uses the standard two-set Korean keyboard mapping.
- Mixed strings are preserved as-is outside Hangul processing.

## Performance

The current implementation uses a single-pass scanner instead of repeated global string replacement. Local measurements on Python 3.12 in this repository produced the following averages:

| Operation | Input shape | Average time |
| --- | --- | ---: |
| `decomposeHangulText` | Repeated Hangul sentence x500 | `0.0041s` |
| `composeHangulText` | Recompose decomposed sentence x500 | `0.0205s` |
| `translateEngToKor` | Keyboard string x2000 | `0.0123s` |

These numbers are environment-dependent, but they reflect the optimized code currently in the repository.

## Development

```bash
python -m pip install -e .[test]
pytest
python scripts/benchmark.py
python -m build
```

## Project Docs

- [Changelog](CHANGELOG.md)
- [Contributing guide](CONTRIBUTING.md)
- [Issue tracker](https://github.com/smturtle2/jamolib/issues)
- [Releases](https://github.com/smturtle2/jamolib/releases)
