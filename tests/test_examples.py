from __future__ import annotations

import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def run_example(path: str) -> str:
    completed = subprocess.run(
        [sys.executable, path],
        cwd=ROOT,
        check=True,
        capture_output=True,
        text=True,
    )
    return completed.stdout


def test_quickstart_example() -> None:
    output = run_example("examples/quickstart.py")
    assert "한글과 English 123" in output
    assert "안녕하세요" in output


def test_batchim_boundaries_example() -> None:
    output = run_example("examples/batchim_boundaries.py")
    assert "ㄱㅏㅂㅅㅇㅣ -> 값이" in output
    assert "ㅇㅣㄹㄱㅇㅓ -> 읽어" in output
