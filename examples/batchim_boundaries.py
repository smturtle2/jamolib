from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

import jamolib

cases = {
    "값이": "ㄱㅏㅂㅅㅇㅣ",
    "닭이": "ㄷㅏㄹㄱㅇㅣ",
    "읽어": "ㅇㅣㄹㄱㅇㅓ",
    "각사": "ㄱㅏㄱㅅㅏ",
}

for expected, source in cases.items():
    print(f"{source} -> {jamolib.composeHangulText(source)} (expected: {expected})")
