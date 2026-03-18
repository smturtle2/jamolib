import random

import pytest

import jamolib


HANGUL_BASE = 0xAC00
HANGUL_LAST = 0xD7A3


def test_public_api_exposes_expected_symbols() -> None:
    assert jamolib.__version__ == "0.2.1"
    assert jamolib.getCharset()


def test_public_api_has_docstrings() -> None:
    for name in jamolib.__all__:
        assert getattr(jamolib, name).__doc__


def test_decompose_and_compose_roundtrip() -> None:
    assert jamolib.decomposeHangul("한") == "ㅎㅏㄴ"
    assert jamolib.decomposeHangulText("한글") == "ㅎㅏㄴㄱㅡㄹ"
    assert jamolib.composeHangul("ㅎㅏㄴ") == "한"
    assert jamolib.composeHangulText("ㅎㅏㄴㄱㅡㄹ") == "한글"


def test_full_hangul_block_roundtrip_as_one_string() -> None:
    syllables = "".join(chr(code) for code in range(0xAC00, 0xD7A4))
    assert jamolib.composeHangulText(jamolib.decomposeHangulText(syllables)) == syllables


def test_random_hangul_strings_roundtrip() -> None:
    random.seed(0)

    for _ in range(100):
        text = "".join(
            chr(random.randint(0xAC00, 0xD7A3))
            for _ in range(random.randint(1, 40))
        )
        assert jamolib.composeHangulText(jamolib.decomposeHangulText(text)) == text


def test_decompose_text_preserves_repeated_and_mixed_characters() -> None:
    assert jamolib.decomposeHangulText("가방") == "ㄱㅏㅂㅏㅇ"
    assert jamolib.decomposeHangulText("한글 ABC 123") == "ㅎㅏㄴㄱㅡㄹ ABC 123"


def test_compose_text_handles_batchim_and_syllable_boundaries() -> None:
    assert jamolib.composeHangulText("ㄱㅏㅂㅅㅇㅣ") == "값이"
    assert jamolib.composeHangulText("ㄷㅏㄹㄱㅇㅣ") == "닭이"
    assert jamolib.composeHangulText("ㅇㅣㄹㄱㅇㅓ") == "읽어"
    assert jamolib.composeHangulText("ㄱㅏㄱㅅㅏ") == "각사"
    assert jamolib.composeHangulText("ㄱㅏㄴㅏ") == "가나"
    assert jamolib.composeHangulText("ㄱㅏㄴㅇㅏ") == "간아"
    assert jamolib.composeHangulText("ㄱㅗㅏ") == "과"
    assert jamolib.composeHangulText("ㄱㅅ") == "ㄱㅅ"
    assert jamolib.composeHangulText("가ㄹㅎ") == "가ㄹㅎ"


def test_complex_hangul_words_roundtrip() -> None:
    samples = [
        "값이",
        "읽어",
        "닭이",
        "앉아",
        "많이",
        "삶과",
        "싫어",
        "넓다",
        "핥아",
        "읊조리다",
        "괜찮아",
        "의의",
        "회의",
        "되어",
        "과외",
        "귀여워",
        "쌓이다",
        "밟아",
        "없어",
        "꽃이",
        "밖에",
        "앉히다",
        "훑어",
        "닭과 값이 많아",
        "읽고 앉아 있다.",
    ]

    for sample in samples:
        decomposed = jamolib.decomposeHangulText(sample)
        assert jamolib.composeHangulText(decomposed) == sample


def test_all_hangul_syllables_roundtrip() -> None:
    for code in range(HANGUL_BASE, HANGUL_LAST + 1):
        syllable = chr(code)
        decomposed = jamolib.decomposeHangulText(syllable)
        assert jamolib.composeHangulText(decomposed) == syllable


def test_representative_pairs_roundtrip_for_all_second_syllables() -> None:
    for jong_index in range(28):
        first = chr(HANGUL_BASE + jong_index)
        for code in range(HANGUL_BASE, HANGUL_LAST + 1):
            text = first + chr(code)
            decomposed = jamolib.decomposeHangulText(text)
            assert jamolib.composeHangulText(decomposed) == text


def test_invalid_inputs_raise_clear_value_errors() -> None:
    with pytest.raises(ValueError):
        jamolib.decomposeHangul("ㄱ")

    with pytest.raises(ValueError):
        jamolib.decomposeHangul("한글")

    with pytest.raises(ValueError):
        jamolib.composeHangul("ㅎ")

    with pytest.raises(ValueError):
        jamolib.composeHangul("aㅏ")


def test_english_keyboard_translation() -> None:
    assert jamolib.translateEngToKor("dkssudgktpdy") == "안녕하세요"
    assert jamolib.translateEngToKor("rhkqrns") == "괍군"
