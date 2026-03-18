"""Public package interface for JamoLib."""

from .core import (
    composeHangul,
    composeHangulText,
    decomposeHangul,
    decomposeHangulText,
    getCharset,
    translateEngToKor,
)

__all__ = [
    "composeHangul",
    "composeHangulText",
    "decomposeHangul",
    "decomposeHangulText",
    "getCharset",
    "translateEngToKor",
]

__version__ = "0.2.0"
