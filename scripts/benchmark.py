from __future__ import annotations

import statistics
import sys
import timeit
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

import jamolib

SAMPLE_TEXT = (
    "안녕하세요. 이것은 예제입니다. 어떤 한글 문장이든 분해하고 조합할 수 있습니다. "
    * 500
)
SAMPLE_ENG = "dkssudgktpdy " * 2000


def benchmark(label: str, stmt: str, repeat: int, number: int) -> None:
    runs = timeit.repeat(stmt, repeat=repeat, number=number, globals=globals())
    per_run = [value / number for value in runs]
    print(
        f"{label:20} min={min(per_run):.6f}s "
        f"mean={statistics.mean(per_run):.6f}s "
        f"max={max(per_run):.6f}s"
    )


def main() -> None:
    print(f"jamolib {jamolib.__version__}")
    benchmark("decomposeHangulText", "jamolib.decomposeHangulText(SAMPLE_TEXT)", 5, 20)
    benchmark(
        "composeHangulText",
        "jamolib.composeHangulText(jamolib.decomposeHangulText(SAMPLE_TEXT))",
        5,
        10,
    )
    benchmark("translateEngToKor", "jamolib.translateEngToKor(SAMPLE_ENG)", 5, 10)


if __name__ == "__main__":
    main()
