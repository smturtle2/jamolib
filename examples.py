import jamolib

# Example usage of jamolib
s1 = "안녕하세요. 이것은 예제입니다. 어떤 한글 문장이든 분해하고 조합할 수 있습니다. 조합ㅂ이 제ㅔ대로ㅗ 되ㅣ지 않아ㅏ도 괜챃ㄴ습니다.\n그건 너무 값이 비싸"
decomposed = jamolib.decomposeHangulText(s1)
print("Decomposed:", decomposed)
recomposed = jamolib.composeHangulText(decomposed)
print("Recomposed:", recomposed)

s2 = "dkssudgktpdy. dudxk gksrmf qusghks dPwpdlqslek."
print("Eng:", s2)
translated = jamolib.translateEngToKor(s2)
print("Translated:", translated)