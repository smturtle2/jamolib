"""Utilities for decomposing, composing, and keyboard-mapping Hangul text."""

JM_BASE = 0xAC00
JM_LAST = 0xD7A3
JM_CHO = 588
JM_JUNG = 28

JM_LIST_CHO = (
    "ㄱ",
    "ㄲ",
    "ㄴ",
    "ㄷ",
    "ㄸ",
    "ㄹ",
    "ㅁ",
    "ㅂ",
    "ㅃ",
    "ㅅ",
    "ㅆ",
    "ㅇ",
    "ㅈ",
    "ㅉ",
    "ㅊ",
    "ㅋ",
    "ㅌ",
    "ㅍ",
    "ㅎ",
)
JM_LIST_JUNG = (
    "ㅏ",
    "ㅐ",
    "ㅑ",
    "ㅒ",
    "ㅓ",
    "ㅔ",
    "ㅕ",
    "ㅖ",
    "ㅗ",
    "ㅘ",
    "ㅙ",
    "ㅚ",
    "ㅛ",
    "ㅜ",
    "ㅝ",
    "ㅞ",
    "ㅟ",
    "ㅠ",
    "ㅡ",
    "ㅢ",
    "ㅣ",
)
JM_LIST_JONG = (
    "",
    "ㄱ",
    "ㄲ",
    "ㄳ",
    "ㄴ",
    "ㄵ",
    "ㄶ",
    "ㄷ",
    "ㄹ",
    "ㄺ",
    "ㄻ",
    "ㄼ",
    "ㄽ",
    "ㄾ",
    "ㄿ",
    "ㅀ",
    "ㅁ",
    "ㅂ",
    "ㅄ",
    "ㅅ",
    "ㅆ",
    "ㅇ",
    "ㅈ",
    "ㅊ",
    "ㅋ",
    "ㅌ",
    "ㅍ",
    "ㅎ",
)

JM_DICT_CHO = dict(zip(JM_LIST_CHO, range(len(JM_LIST_CHO))))
JM_DICT_JUNG = dict(zip(JM_LIST_JUNG, range(len(JM_LIST_JUNG))))
JM_DICT_JONG = dict(zip(JM_LIST_JONG, range(len(JM_LIST_JONG))))
JM_SET_CHO = frozenset(JM_LIST_CHO)
JM_SET_JUNG = frozenset(JM_LIST_JUNG)
JM_SET_JONG = frozenset(JM_LIST_JONG[1:])

JM_DICT_JONG_DECOMPOSE = {
    "ㄳ": "ㄱㅅ",
    "ㄵ": "ㄴㅈ",
    "ㄶ": "ㄴㅎ",
    "ㄺ": "ㄹㄱ",
    "ㄻ": "ㄹㅁ",
    "ㄼ": "ㄹㅂ",
    "ㄽ": "ㄹㅅ",
    "ㄾ": "ㄹㅌ",
    "ㄿ": "ㄹㅍ",
    "ㅀ": "ㄹㅎ",
    "ㅄ": "ㅂㅅ",
}
JM_DICT_JONG_COMPOSE = {
    "ㄱㅅ": "ㄳ",
    "ㄴㅈ": "ㄵ",
    "ㄴㅎ": "ㄶ",
    "ㄹㄱ": "ㄺ",
    "ㄹㅁ": "ㄻ",
    "ㄹㅂ": "ㄼ",
    "ㄹㅅ": "ㄽ",
    "ㄹㅌ": "ㄾ",
    "ㄹㅍ": "ㄿ",
    "ㄹㅎ": "ㅀ",
    "ㅂㅅ": "ㅄ",
}
JM_DICT_JUNG_COMPOSE = {
    "ㅗㅏ": "ㅘ",
    "ㅗㅐ": "ㅙ",
    "ㅗㅣ": "ㅚ",
    "ㅜㅓ": "ㅝ",
    "ㅜㅔ": "ㅞ",
    "ㅜㅣ": "ㅟ",
    "ㅡㅣ": "ㅢ",
}

JM_ENG_KOR = {
    "r": "ㄱ",
    "R": "ㄲ",
    "s": "ㄴ",
    "e": "ㄷ",
    "E": "ㄸ",
    "f": "ㄹ",
    "a": "ㅁ",
    "q": "ㅂ",
    "Q": "ㅃ",
    "t": "ㅅ",
    "T": "ㅆ",
    "d": "ㅇ",
    "w": "ㅈ",
    "W": "ㅉ",
    "c": "ㅊ",
    "z": "ㅋ",
    "x": "ㅌ",
    "v": "ㅍ",
    "g": "ㅎ",
    "k": "ㅏ",
    "o": "ㅐ",
    "i": "ㅑ",
    "O": "ㅒ",
    "j": "ㅓ",
    "p": "ㅔ",
    "u": "ㅕ",
    "P": "ㅖ",
    "h": "ㅗ",
    "hk": "ㅘ",
    "ho": "ㅙ",
    "hl": "ㅚ",
    "y": "ㅛ",
    "n": "ㅜ",
    "nj": "ㅝ",
    "np": "ㅞ",
    "nl": "ㅟ",
    "b": "ㅠ",
    "m": "ㅡ",
    "ml": "ㅢ",
    "l": "ㅣ",
}
JM_CHARSET = tuple(JM_ENG_KOR.values())


def getCharset() -> list[str]:
    """Return the compatibility jamo characters used by the keyboard mapping."""

    return list(JM_CHARSET)


def _is_hangul_syllable(char: str) -> bool:
    return len(char) == 1 and JM_BASE <= ord(char) <= JM_LAST


def _decompose_hangul_syllable(syllable: str) -> str:
    code = ord(syllable) - JM_BASE
    cho = code // JM_CHO
    jung = (code % JM_CHO) // JM_JUNG
    jong = code % JM_JUNG

    result = [JM_LIST_CHO[cho], JM_LIST_JUNG[jung]]
    jong_char = JM_LIST_JONG[jong]
    result.append(JM_DICT_JONG_DECOMPOSE.get(jong_char, jong_char))
    return "".join(result)


def decomposeHangul(syllable: str) -> str:
    """Decompose a single Hangul syllable into compatibility jamo."""

    if not _is_hangul_syllable(syllable):
        raise ValueError("syllable must be a single Hangul syllable in the range '가' to '힣'.")
    return _decompose_hangul_syllable(syllable)


def decomposeHangulText(text: str) -> str:
    """Decompose every Hangul syllable in text while preserving non-Hangul characters."""

    result: list[str] = []
    append = result.append
    jong_decompose = JM_DICT_JONG_DECOMPOSE.get

    for char in text:
        code = ord(char)
        if JM_BASE <= code <= JM_LAST:
            offset = code - JM_BASE
            cho = offset // JM_CHO
            jung = (offset % JM_CHO) // JM_JUNG
            jong = offset % JM_JUNG
            append(JM_LIST_CHO[cho])
            append(JM_LIST_JUNG[jung])
            jong_char = JM_LIST_JONG[jong]
            append(jong_decompose(jong_char, jong_char))
            continue

        append(char)

    return "".join(result)


def composeHangul(jamos: str) -> str:
    """Compose one Hangul syllable from compatibility jamo."""

    if len(jamos) not in (2, 3, 4):
        raise ValueError("jamos must contain 2 to 4 compatibility jamo characters.")

    try:
        cho = JM_DICT_CHO[jamos[0]]
        jung = JM_DICT_JUNG[jamos[1]]
    except KeyError as exc:
        raise ValueError(
            "jamos must start with a valid choseong followed by a valid jungseong."
        ) from exc

    jong = 0
    if len(jamos) == 3:
        try:
            jong = JM_DICT_JONG[jamos[2]]
        except KeyError as exc:
            raise ValueError("the final jamo must be a valid jongseong.") from exc
    elif len(jamos) == 4:
        try:
            jong = JM_DICT_JONG[JM_DICT_JONG_COMPOSE[jamos[2:4]]]
        except KeyError as exc:
            raise ValueError(
                "the last two jamo characters must form a valid double jongseong."
            ) from exc

    return chr(JM_BASE + JM_CHO * cho + JM_JUNG * jung + jong)


def composeHangulText(text: str) -> str:
    """Compose Hangul syllables from compatibility jamo text in a single pass."""

    result: list[str] = []
    append = result.append
    set_cho = JM_SET_CHO
    set_jung = JM_SET_JUNG
    set_jong = JM_SET_JONG
    jong_compose = JM_DICT_JONG_COMPOSE
    jung_compose = JM_DICT_JUNG_COMPOSE
    i = 0
    text_len = len(text)

    while i < text_len:
        char = text[i]
        if char not in set_cho or i + 1 >= text_len or text[i + 1] not in set_jung:
            append(char)
            i += 1
            continue

        medial = text[i + 1]
        medial_width = 1
        if i + 2 < text_len:
            medial_pair = text[i + 1 : i + 3]
            if medial_pair in jung_compose:
                medial = jung_compose[medial_pair]
                medial_width = 2

        jamos = text[i] + medial
        advance = 1 + medial_width
        tail_index = i + advance

        if tail_index < text_len and text[tail_index] in set_jong:
            next_index = tail_index + 1
            if next_index >= text_len or text[next_index] not in set_jung:
                jamos += text[tail_index]
                advance += 1

                pair_index = tail_index + 1
                next_after_pair = tail_index + 2
                if (
                    pair_index < text_len
                    and text[tail_index : pair_index + 1] in jong_compose
                    and (next_after_pair >= text_len or text[next_after_pair] not in set_jung)
                ):
                    jamos += text[pair_index]
                    advance += 1

        append(composeHangul(jamos))
        i += advance

    return "".join(result)


def translateEngToKor(text: str) -> str:
    """Convert two-set Korean keyboard input written with English keys into Hangul."""

    prepared: list[str] = []
    append = prepared.append
    eng_kor = JM_ENG_KOR
    i = 0
    text_len = len(text)

    while i < text_len:
        pair = text[i : i + 2]
        if len(pair) == 2 and pair in eng_kor:
            append(eng_kor[pair])
            i += 2
            continue

        char = text[i]
        append(eng_kor.get(char, char))
        i += 1

    return composeHangulText("".join(prepared))
