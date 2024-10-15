import streamlit as st # streamlit 라이브러리 임포트

# 타이틀 텍스트 출력
st.title('첫번째 웹 어플 만들기 👋')


# 텍스트 출력
7 st.write('# 1. Markdown 텍스트 작성하기')
8
9 # Markdown 문법으로 작성된 문장 출력
10 st.markdown(
11 '''
12 # 마크다운 헤더1
13 - 마크다운 목록1. **굵게** 표시
14 - 마크다운 목록2. *기울임* 표시
15 - 마크다운 목록2-1
16 - 마크다운 목록2-2
17
18 ## 마크다운 헤더2
19 - [네이버](https://naver.com)
20 - [구글](https://google.com)
21
22 ### 마크다운 헤더3
23 일반 텍스트
24 '''
25 )
26
27 # DataFrame 출력
28 import pandas as pd # pandas 라이브러리 임포트
29
30 st.write('# 2. DataFrame 표시하기') # 텍스트 출력
31 df = pd.DataFrame({ # DataFrame 생성
32 '이름': ['홍길동', '이순신', '강감찬'],
33 '나이': [20, 45, 35]
34 })
