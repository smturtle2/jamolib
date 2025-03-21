'''
JamoLib : 한글 조합 및 분해 관련 함수들을 제공하는 라이브러리
    - decomposeHangul(syllable: str) -> tuple : 한글 음절을 자모 단위로 분해
    - decomposeHangulText(text: str) -> str : 전체 텍스트에 대해 자모 분해를 수행
    - composeHangul(jamos: list) -> str : 자모를 합쳐서 한글 음절로 조합
    - composeHangulText(text: str) -> str : 전체 텍스트에 대해 자모 조합을 수행
    - translateEngToKor(text: str) -> str : 영타를 한글로 변환
'''

JM_BASE = 0xAC00
JM_CHO = 588
JM_JUNG = 28

JM_LIST_CHO = ['ㄱ', 'ㄲ', 'ㄴ', 'ㄷ', 'ㄸ', 'ㄹ', 'ㅁ', 'ㅂ', 'ㅃ', 'ㅅ', 'ㅆ', 'ㅇ', 'ㅈ', 'ㅉ', 'ㅊ', 'ㅋ', 'ㅌ', 'ㅍ', 'ㅎ']
JM_LIST_JUNG = ['ㅏ', 'ㅐ', 'ㅑ', 'ㅒ', 'ㅓ', 'ㅔ', 'ㅕ', 'ㅖ', 'ㅗ', 'ㅘ', 'ㅙ', 'ㅚ', 'ㅛ', 'ㅜ', 'ㅝ', 'ㅞ', 'ㅟ', 'ㅠ', 'ㅡ', 'ㅢ', 'ㅣ']
JM_LIST_JONG = ['', 'ㄱ', 'ㄲ', 'ㄳ', 'ㄴ', 'ㄵ', 'ㄶ', 'ㄷ', 'ㄹ', 'ㄺ', 'ㄻ', 'ㄼ', 'ㄽ', 'ㄾ', 'ㄿ', 'ㅀ', 'ㅁ', 'ㅂ', 'ㅄ', 'ㅅ', 'ㅆ', 'ㅇ', 'ㅈ', 'ㅊ', 'ㅋ', 'ㅌ', 'ㅍ', 'ㅎ']

JM_DICT_CHO = dict(zip(JM_LIST_CHO, range(0, len(JM_LIST_CHO))))
JM_DICT_JUNG = dict(zip(JM_LIST_JUNG, range(0, len(JM_LIST_JUNG))))
JM_DICT_JONG = dict(zip(JM_LIST_JONG, range(0, len(JM_LIST_JONG))))

JM_DICT_JONG_DECOMPOSE = {
    'ㄳ': ('ㄱ', 'ㅅ'), 'ㄵ': ('ㄴ', 'ㅈ'), 'ㄶ': ('ㄴ', 'ㅎ'), 'ㄺ': ('ㄹ', 'ㄱ'), 'ㄻ': ('ㄹ', 'ㅁ'), 
    'ㄼ': ('ㄹ', 'ㅂ'), 'ㄽ': ('ㄹ', 'ㅅ'), 'ㄾ': ('ㄹ', 'ㅌ'), 'ㄿ': ('ㄹ', 'ㅎ'), 'ㅀ': ('ㅎ', 'ㅇ'),
}
JM_DICT_JONG_COMPOSE = {
    ('ㄱ', 'ㅅ'): 'ㄳ', ('ㄴ', 'ㅈ'): 'ㄵ', ('ㄴ', 'ㅎ'): 'ㄶ', ('ㄹ', 'ㄱ'): 'ㄺ', ('ㄹ', 'ㅁ'): 'ㄻ',
    ('ㄹ', 'ㅂ'): 'ㄼ', ('ㄹ', 'ㅅ'): 'ㄽ', ('ㄹ', 'ㅌ'): 'ㄾ', ('ㄹ', 'ㅎ'): 'ㄿ', ('ㅎ', 'ㅇ'): 'ㅀ',
}

JM_ENG_KOR = {
    'r': 'ㄱ', 'R': 'ㄲ', 's': 'ㄴ', 'e': 'ㄷ', 'E': 'ㄸ', 'f': 'ㄹ', 'a': 'ㅁ',
    'q': 'ㅂ', 'Q': 'ㅃ', 't': 'ㅅ', 'T': 'ㅆ', 'd': 'ㅇ', 'w': 'ㅈ', 'W': 'ㅉ',
    'c': 'ㅊ', 'z': 'ㅋ', 'x': 'ㅌ', 'v': 'ㅍ', 'g': 'ㅎ',
    'k': 'ㅏ', 'o': 'ㅐ', 'i': 'ㅑ', 'O': 'ㅒ', 'j': 'ㅓ', 'p': 'ㅔ', 'u': 'ㅕ',
    'P': 'ㅖ', 'h': 'ㅗ', 'hk': 'ㅘ', 'ho': 'ㅙ', 'hl': 'ㅚ', 'y': 'ㅛ', 'n': 'ㅜ',
    'nj': 'ㅝ', 'np': 'ㅞ', 'nl': 'ㅟ', 'b': 'ㅠ', 'm': 'ㅡ', 'ml': 'ㅢ', 'l': 'ㅣ',
}

def decomposeHangul(syllable: str) -> list:
    code = ord(syllable) - JM_BASE
    cho = code // JM_CHO
    jung = (code - JM_CHO * cho) // JM_JUNG
    jong = (code - JM_CHO * cho - JM_JUNG * jung)

    rt = []
    rt.append(JM_LIST_CHO[cho])
    rt.append(JM_LIST_JUNG[jung])
    jong = JM_LIST_JONG[jong]
    if jong in JM_DICT_JONG_DECOMPOSE:
        rt.extend(JM_DICT_JONG_DECOMPOSE[jong])
    else:
        rt.append(jong)

    return rt

def decomposeHangulText(text: str) -> str:
    result = []
    for char in text:
        if ord(char) < 0xAC00 or ord(char) > 0xD7A3:
            result.append(char)
            continue
        result.extend(decomposeHangul(char))
    return ''.join(result)

def composeHangul(jamos: list) -> str:
    cho = JM_DICT_CHO[jamos[0]]
    jung = JM_DICT_JUNG[jamos[1]]

    code = JM_BASE + JM_CHO * cho + JM_JUNG * jung
    if len(jamos) == 2:
        return chr(code)
    
    jong = 0
    if len(jamos) == 3:
        jong = JM_DICT_JONG[jamos[2]]
    else:
        jong = JM_DICT_JONG[JM_DICT_JONG_COMPOSE[(jamos[2], jamos[3])]]

    code = JM_BASE + JM_CHO * cho + JM_JUNG * jung + jong
    return chr(code)

def composeHangulText(text: str) -> str:
    comb = ""
    skip = 0
    for i, c in enumerate(text):
        if skip > 0:                                            # skip
            skip -= 1
            continue
        if c not in JM_DICT_JUNG:                               # c가 모음이 아님
            comb += c
            continue
        if i == 0:                                              # c가 첫 글자임
            comb += c
            continue
        if text[i-1] not in JM_DICT_CHO:                        # c가 모음이지만 앞글자가 초성이 아님
            comb += c
            continue
        comb = comb[:-1]                                        # 조합가능하므로 comb에 있는 초성을 제거
        if i == len(text) - 1:                                  # c가 마지막 글자임
            comb += composeHangul(text[i-1:i+1])
            continue
        if text[i+1] not in JM_DICT_JONG:                       # 받침이 없음
            comb += composeHangul(text[i-1:i+1])
            continue
        if i == len(text) - 2:                                  # c가 마지막에서 두번째 글자임
            comb += composeHangul(text[i-1:i+2])
            skip = 1
            continue
        if text[i+2] in JM_DICT_JUNG:                           # 받침이 다음 모음과 조합 가능함
            comb += composeHangul(text[i-1:i+1])
            continue
        if text[i+2] not in JM_DICT_JONG:                       # 이중종성의 가능성이 없음
            comb += composeHangul(text[i-1:i+2])
            skip = 1
            continue
        if (text[i+1], text[i+2]) not in JM_DICT_JONG_COMPOSE:  # 이중종성 조합이 불가능함
            comb += composeHangul(text[i-1:i+2])
            skip = 1
            continue
        if i == len(text) - 3:                                  # c가 마지막에서 세번째 글자임
            comb += composeHangul(text[i-1:i+3])
            skip = 2
            continue
        if text[i+3] in JM_DICT_JUNG:                           # 이중종성 조합이 가능한 글자가 다음 모음과 조합 가능함
            comb += composeHangul(text[i-1:i+2])
            skip = 1
            continue
        comb += composeHangul(text[i-1:i+3])
        skip = 2
    
    # comb에 남아있는 조합가능한 종성을 조합
    for i in range(len(comb)-2, -1, -1):
        if comb[i] not in JM_DICT_JONG:
            continue
        if comb[i+1] not in JM_DICT_JONG:
            continue
        if (comb[i], comb[i+1]) not in JM_DICT_JONG_COMPOSE:
            continue
        comb = comb[:i] + JM_DICT_JONG_COMPOSE[(comb[i], comb[i+1])] + comb[i+2:]

    return comb

def translateEngToKor(text: str) -> str:
    prep = ""
    skip = 0
    for i, c in enumerate(text):
        if skip > 0:
            skip -= 1
            continue
        if c not in JM_ENG_KOR:
            prep += c
            continue
        if i == len(text) - 1:
            prep += JM_ENG_KOR[c]
            continue
        if text[i+1] not in JM_ENG_KOR:
            prep += JM_ENG_KOR[c]
            continue
        if text[i:i+2] not in JM_ENG_KOR:
            prep += JM_ENG_KOR[c]
            continue
        prep += JM_ENG_KOR[text[i:i+2]]
        skip = 1

    return composeHangulText(prep)