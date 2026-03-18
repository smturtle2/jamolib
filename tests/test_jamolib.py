import jamolib


def test_public_api_exposes_expected_symbols() -> None:
    assert jamolib.__version__ == "0.1.0"
    assert jamolib.getCharset()


def test_decompose_and_compose_roundtrip() -> None:
    assert jamolib.decomposeHangul("한") == "ㅎㅏㄴ"
    assert jamolib.decomposeHangulText("한글") == "ㅎㅏㄴㄱㅡㄹ"
    assert jamolib.composeHangul("ㅎㅏㄴ") == "한"
    assert jamolib.composeHangulText("ㅎㅏㄴㄱㅡㄹ") == "한글"


def test_english_keyboard_translation() -> None:
    assert jamolib.translateEngToKor("dkssudgktpdy") == "안녕하세요"
