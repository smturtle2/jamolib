from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

import jamolib

text = "JamoLib 0.2 keeps English, numbers 123, and punctuation!"

print("Input:      ", text)
print("Processed:  ", jamolib.decomposeHangulText(text))
print("Round-trip: ", jamolib.composeHangulText(jamolib.decomposeHangulText("한글 ABC 123")))
