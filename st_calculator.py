import streamlit as st

# 계산기를 위한 기본 상태 초기화
if 'input' not in st.session_state:
    st.session_state.input = ''
if 'result' not in st.session_state:
    st.session_state.result = ''

# 버튼 클릭 핸들러 함수
def append_input(value):
    st.session_state.input += str(value)

def clear_input():
    st.session_state.input = ''
    st.session_state.result = ''

def calculate_result():
    try:
        st.session_state.result = str(eval(st.session_state.input))
        st.session_state.input = st.session_state.result  # 결과를 입력으로 설정하여 연속 계산 가능
    except Exception as e:
        st.session_state.result = "오류"

# UI 구성
st.title("간단한 웹 계산기")
st.header(" ")
st.subheader(" ")
st.write(" ")

# 계산기 버튼 레이아웃 설정
col1, col2, col3, col4 = st.columns(4)

# 숫자 버튼
with col1:
    if st.button("1"): append_input(1)
    if st.button("4"): append_input(4)
    if st.button("7"): append_input(7)
    if st.button("**C**"): clear_input()

with col2:
    if st.button("2"): append_input(2)
    if st.button("5"): append_input(5)
    if st.button("8"): append_input(8)
    if st.button("0"): append_input(0)

with col3:
    if st.button("3"): append_input(3)
    if st.button("6"): append_input(6)
    if st.button("9"): append_input(9)
    if st.button("**=**"): calculate_result()

# 연산자 버튼
with col4:
    if st.button("**+**"): append_input('+')
    if st.button("**-**"): append_input('-')
    if st.button("**X**"): append_input('*')
    if st.button("**/**"): append_input('/')
    
    
st.write(" ")
st.write(" ")
st.write(" ")

# 현재 입력 및 결과 표시
st.write("입력:", st.session_state.input)
st.write("결과:", st.session_state.result)