import streamlit as st

# 전체 페이지 너비 설정
st.set_page_config(layout="wide", page_title="Python 활용 가이드")

# CSS 및 JavaScript 추가
st.markdown("""
<style>
    .custom-box {
        background-color: #f0f2f6;
        border-radius: 10px;
        padding: 20px;
        position: fixed;
        right: 10px;
        top: 60px;
        width: 300px;
        height: calc(100vh - 80px);
        overflow-y: auto;
        z-index: 1000;  /* 이 줄을 추가하여 메뉴 박스를 최상위로 설정 */
        box-shadow: -5px 0 15px rgba(0,0,0,0.1);  /* 그림자 효과 추가 */
    }
    .content-section {
        padding-top: 50px;
        max-width: calc(100% - 320px);
    }
    code {
        white-space: pre-wrap;
    }
    /* 스크롤바 스타일링 */
    .custom-box::-webkit-scrollbar {
        width: 5px;
    }
    .custom-box::-webkit-scrollbar-track {
        background: #f1f1f1;
    }
    .custom-box::-webkit-scrollbar-thumb {
        background: #888;
    }
    .custom-box::-webkit-scrollbar-thumb:hover {
        background: #555;
    }
</style>

<script>
    function scrollToSection(sectionId) {
        var element = document.getElementById(sectionId);
        element.scrollIntoView({behavior: "smooth"});
    }
</script>
""", unsafe_allow_html=True)

# 메인 제목
st.title("Python 활용 가이드")

# 카테고리 선택
category = st.selectbox("카테고리 선택", ["Python 기초 문법", "Pandas", "Matplotlib"])

if category == "Pandas":
    # 오른쪽 메뉴
    st.markdown("""
    <div class="custom-box">
        <h3>Pandas 목차</h3>
        <ul>
            <li><a href="#section1" onclick="scrollToSection('section1'); return false;">엑셀 데이터 불러오기</a></li>
            <li><a href="#section2" onclick="scrollToSection('section2'); return false;">데이터프레임으로 변형</a></li>
            <li><a href="#section3" onclick="scrollToSection('section3'); return false;">결측치 제거하기</a></li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

    # 섹션 1: 엑셀 데이터 불러오기
    st.markdown('<div id="section1" class="content-section">', unsafe_allow_html=True)
    st.header("엑셀 데이터 불러오기")
    st.write("Pandas를 사용하여 엑셀 파일을 불러오는 방법입니다.")
    
    code1 = """
    import pandas as pd

    # 엑셀 파일 불러오기
    df = pd.read_excel('example.xlsx', sheet_name='Sheet1')
    
    # 데이터 확인
    print(df.head())
    """
    st.code(code1, language='python')
    st.markdown('</div>', unsafe_allow_html=True)

    # 섹션 2: 데이터프레임으로 변형
    st.markdown('<div id="section2" class="content-section">', unsafe_allow_html=True)
    st.header("데이터프레임으로 변형")
    st.write("다양한 데이터 소스를 Pandas DataFrame으로 변형하는 방법입니다.")
    
    code2 = """
    import pandas as pd

    # 딕셔너리로부터 DataFrame 생성
    data = {'Name': ['John', 'Anna', 'Peter', 'Linda'],
            'Age': [28, 34, 29, 32],
            'City': ['New York', 'Paris', 'Berlin', 'London']}
    df = pd.DataFrame(data)
    
    print(df)
    """
    st.code(code2, language='python')
    st.markdown('</div>', unsafe_allow_html=True)

    # 섹션 3: 결측치 제거하기
    st.markdown('<div id="section3" class="content-section">', unsafe_allow_html=True)
    st.header("결측치 제거하기")
    st.write("DataFrame에서 결측치를 제거하는 방법입니다.")
    
    code3 = """
    import pandas as pd
    import numpy as np

    # 결측치가 있는 DataFrame 생성
    df = pd.DataFrame({'A': [1, 2, np.nan, 4],
                       'B': [5, np.nan, np.nan, 8],
                       'C': [9, 10, 11, 12]})

    print("원본 데이터:")
    print(df)

    # 결측치 제거
    df_cleaned = df.dropna()

    # 결측치 제거 후
    print(df_cleaned)
    """
    st.code(code3, language='python')
    st.markdown('</div>', unsafe_allow_html=True)

elif category == "Python 기초 문법":
    st.write("Python 기초 문법 내용 추가.")

elif category == "Matplotlib":
    st.write("Matplotlib 내용 추가.")