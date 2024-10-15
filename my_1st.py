import streamlit as st # streamlit 라이브러리 임포트

# 타이틀 텍스트 출력

# 텍스트
st.header('🚗 원하는 텍스트 출력 💜💜💜💜💜')
st.write('') # 빈 줄 삽입

st.write('# 마크다운 H1 : st.write()')
st.write('### 마크다운 H3 : st.write()')
st.write('- 목록')
st.write('')

# 제목, 헤더, 서브헤더, 본문텍스트의 차이를 보기 위해서..
st.title('제목 : st.title()')
st.header('헤더 : st.header()')
st.subheader('서브헤더 : st.subheader()')
st.text('본문 텍스트 : st.text()')
st.write('')

st.markdown('## 마크다운 : st.markdown()')
st.markdown('''
            1. ordered item
            - unordered item
                - unordered
            - unordered item
            1. ordered item
                1. ordered
                1. ordered
                10. ordered 
            10. ordered item
            ''')
st.divider() # 👈 구분선

# 마크다운
'''# 👑 Magic에 마크다운을 조합
1. ordered item
    - 강조: **unordered item**
    - 기울임: *unordered item*
2. ordered item
3. ordered item
'''

# 데이터프레임
import pandas as pd
df = pd.DataFrame({'A':[1, 2, 3],'B':[4, 5, 6]})
df # 👈 데이터프레임 출력

# 차트
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 10, 100)
y = np.sin(x)

fig, ax = plt.subplots()
ax.plot(x, y)
fig # 👈 차트 출력

# 사이드바
st.sidebar.header('⬅️⬅️⬅️⬅️ 사이드바')
st.sidebar.write('## 사이드바 텍스트')
st.sidebar.checkbox('체크박스 1')
st.sidebar.checkbox('체크박스 2')
st.sidebar.radio('라디오 버튼', ['radio 1', 'radio 2', 'radio 3'])
st.sidebar.selectbox('셀렉트박스', ['select 1', 'select 2', 'select 3'])

# 레이아웃: 컬럼
st.header('🧑🏻‍🚀 컬럼 레이아웃')
col_1, col_2, col_3 = st.columns([1,2,1]) # 컬럼 인스턴스 생성. 1:2:1 비율로 컬럼을 나눔

with col_1:
    st.write('## 1번 컬럼')
    st.checkbox('이것은 1번 컬럼에 속한 체크박스 1')
    st.checkbox('이것은 1번 컬럼에 속한 체크박스 2')

with col_2:
    st.write('## 2번 컬럼')
    st.radio('2번 컬럼의 라디오 버튼', ['radio 1', 'radio 2', 'radio 3'])
    # 사이드바에 이미 라디오 버튼이 생성되어 있으므로, 여기서는 라디오 버튼의 내용을 변경해야 오류가 발생하지 않음!!

col_3.write('## 3번 컬럼')
col_3.selectbox('3번 컬럼의 셀렉트박스', ['select 1', 'select 2', 'select 3'])
# 사이드바에 이미 셀렉트박스가 생성되어 있기 때문에, 여기서는 셀렉트박스의 내용을 변경해야 오류가 발생하지 않음!!

# 레이아웃: 탭
st.header('👮 탭 레이아웃')

# 탭 인스턴스 생성. 3개의 탭을 생성
tab_1, tab_2, tab_3 = st.tabs(['탭AAAA', '탭BBBB', '탭CCCC'])
with tab_1:
    st.write('## 탭AAAA')
    st.write('이것은 탭A의 내용입니다.')

with tab_2:
    st.write('## 탭BBBB')
    st.write('이것은 탭B의 내용입니다.')
    '''
    ```python
    import pandas as pd
    a=3
    b=4
    print(a+b)
    ```
    '''

tab_3.write('## 탭CCCC')
tab_3.write('이것은 탭C의 내용입니다.')
tab_3.write(fig)


st.dataframe(df) # DataFrame 출력

# 그래프 출력
import numpy as np # numpy 라이브러리 임포트

st.write('# 3. 그래프 표시하기') # 텍스트 출력
chart_data = pd.DataFrame(np.random.randn(20, 3), columns=["a", "b", "c"]) # DataFrame 생성

st.bar_chart(chart_data) # 바 차트 출력

# 이미지 출력
from PIL import Image # 이미지 처리를 위한 PIL 라이브러리 임포트

st.write('# 4. 이미지 표시하기') # 텍스트 출력
img = Image.open('python.png') # 이미지 파일 열기
st.image(img, width=300) # 이미지 출력



