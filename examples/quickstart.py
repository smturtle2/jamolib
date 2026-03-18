from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

import jamolib

text = "한글과 English 123"
decomposed = jamolib.decomposeHangulText(text)

print("Original:   ", text)
print("Decomposed: ", decomposed)
print("Recomposed: ", jamolib.composeHangulText(decomposed))
print("Keyboard:   ", jamolib.translateEngToKor("dkssudgktpdy"))
