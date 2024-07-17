import streamlit as st

# CSS를 사용하여 오른쪽 메뉴 스타일 정의
st.markdown(
    """
    <style>
    .sidebar .sidebar-content {
        position: fixed;
        right: 0;
        top: 0;
        bottom: 0;
        width: 20rem;
        padding: 2rem 1rem;
        background-color: #f8f9fa;
        z-index: 1;
    }
    .main .block-container {
        max-width: calc(100% - 22rem);
        padding-left: 1rem;
        padding-right: 1rem;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# 메인 컨텐츠
st.title("메인 페이지")
st.write("여기에 메인 컨텐츠가 들어갑니다.")

# 오른쪽 메뉴 (사이드바 사용)
with st.sidebar:
    st.header("오른쪽 메뉴")
    option = st.selectbox(
        '메뉴를 선택하세요:',
        ('메뉴 1', '메뉴 2', '메뉴 3')
    )
    
    if st.button('버튼 1'):
        st.write('버튼 1을 클릭했습니다.')
    
    if st.button('버튼 2'):
        st.write('버튼 2를 클릭했습니다.')

# 선택된 메뉴에 따른 내용 표시
if option == '메뉴 1':
    st.write('메뉴 1의 내용입니다.')
elif option == '메뉴 2':
    st.write('메뉴 2의 내용입니다.')
elif option == '메뉴 3':
    st.write('메뉴 3의 내용입니다.')