from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parent / "src"))

import jamolib

s1 = "안녕하세요. 이것은 예제입니다. 어떤 한글 문장이든 분해하고 조합할 수 있습니다."
decomposed = jamolib.decomposeHangulText(s1)
print("Decomposed:", decomposed)
print("Recomposed:", jamolib.composeHangulText(decomposed))

s2 = "dkssudgktpdy"
print("Eng:", s2)
print("Translated:", jamolib.translateEngToKor(s2))
