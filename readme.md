# JamoLib

JamoLib는 한글 텍스트를 자모 단위로 분해하고 다시 조합하거나, 영문 키보드 입력을 한글로 변환할 때 사용할 수 있는 가벼운 파이썬 라이브러리입니다.

## 설치

```bash
pip install jamolib
```

## 주요 기능

- `decomposeHangul`: 한글 음절 하나를 자모 단위로 분해합니다.
- `decomposeHangulText`: 문자열 전체를 자모 문자열로 분해합니다.
- `composeHangul`: 자모를 한글 음절 하나로 조합합니다.
- `composeHangulText`: 자모 문자열을 다시 한글 문자열로 조합합니다.
- `translateEngToKor`: 두벌식 영문 키 입력을 한글 문자열로 변환합니다.

## 사용 예시

```python
import jamolib

print(jamolib.decomposeHangulText("한글"))
# ㅎㅏㄴㄱㅡㄹ

print(jamolib.composeHangulText("ㅎㅏㄴㄱㅡㄹ"))
# 한글

print(jamolib.translateEngToKor("dkssudgktpdy"))
# 안녕하세요
```

## 개발

```bash
python -m pip install -e .[test]
pytest
python -m build
```
