import streamlit as st
from streamlit_option_menu import option_menu
import matplotlib.pyplot as plt
import numpy as np

class IndexAllocator:
    def __init__(self):
        self.parentIdx = 0
        self.childIdx = 0
        
    def nextSection(self):
        self.parentIdx += 1
        self.childIdx = 0
        
    def getSectionIdx(self) :
        #format : 1. / 2. / 3. ...
        return f"{self.parentIdx}. "
    
    def getIdx(self):
        self.childIdx += 1
        #format : 1.1 / 1.2 ...
        return f"{self.parentIdx}.{self.childIdx} " 


@st.cache_data
def load_contents() :
    #topic - chapter - section
    contents = {
        "파이썬 기초": {
            "대단원 01": ["소단원01", "소단원02"],
            "대단원 02": ["소단원01"],
            "대단원 03": ["소단원01", "소단원02", "소단원03"]
        },
        "Pandas 기초": {
            "DataFrame": ["데이터프레임 생성", "데이터프레임 속성", "데이터프레임 조회",
                          "데이터프레임 정렬", "Indexing, Slicing, 조건 필터링"],
            "Excel/CSV": ["Excel", "CSV"],
            "Data 전처리": ["데이터 복사", "데이터 결측치", "column 추가", "데이터 삭제", "column 연산", "데이터 변환"],
            "Data 연결과 병합": ["데이터 연결", "데이터 병합"],
            "Static" : ["기술 통계", "고급 통계"]
        },
        "Matplotlib 기초": {
            "대단원 01": ["소단원01", "소단원02", "소단원03"],
            "대단원 02": ["소단원01", "소단원02"]
        }
    }
    topics = list(contents.keys())
    return contents, topics
CONTENTS , TOPICS = load_contents()

def init_session_state() :
    if 'page' not in st.session_state:
        st.session_state['page'] = 'page_topic'

    if 'topic' not in st.session_state:
        st.session_state['topic'] = TOPICS[0]

    if 'chapter' not in st.session_state:
        st.session_state['chapter'] = None

    if 'section' not in st.session_state:
        st.session_state['section'] = None

    #(page, topic, chapter, section)
    return (st.session_state['page'], st.session_state['topic'], 
            st.session_state['chapter'], st.session_state['section'])

def update_session_state(*args) :
    key = args[0]

    #topic 변경(사이드바)
    if key == 'change_topic':
        st.session_state['page'] = 'page_topic'
        st.session_state['topic'] = st.session_state['change_topic']
        st.session_state['chapter'] = None
        st.session_state['section'] = None
    
    #chapter 변경(학습하기)
    elif key == 'change_chapter' :
        st.session_state['page'] = 'page_chapter'
        st.session_state['chapter'] = args[1]['chapter']
    
    #section 변경(셀렉트박스)
    elif key == 'change_section' :
        st.session_state['section'] = st.session_state['change_section']
    
    #돌아가기
    elif key == 'go_back' :
        st.session_state['page'] = 'page_topic'
        st.session_state['chapter'] = None
        st.session_state['section'] = None

def show_topic(topic):
    chapters = CONTENTS[topic]

    st.title(topic)
    info_txt = {
            "파이썬 기초" : "파이썬 기초 문법을 제공합니다.",
            "Pandas 기초" : "Pandas 기초 문법을 제공합니다.",
            "Matplotlib 기초" : "Matplotlib 기초 문법을 제공합니다.",
    }
    st.info(info_txt[topic])
    
    table = [st.columns(3)] * ((len(chapters) + 2) // 3)
    for i, title in enumerate(chapters):
        with table[i // 3][i % 3]:
            card = st.container(height=200, border=True)
            subcard = card.container(height=110, border=False)
            subcard.subheader(title)

            card.button("학습하기", 
                        key=f"btn_{i}",
                        on_click=update_session_state, 
                        args=('change_chapter', {'chapter':title}),
                        use_container_width=True)

def show_chapter(topic, chapter):
    sections = CONTENTS[topic][chapter]

    st.title(chapter)
    
    st.session_state['section'] = st.selectbox("Choose a section:",
                                               sections,
                                               key = 'change_section',
                                               on_change = update_session_state,
                                               args=('change_section',),
                                               label_visibility="hidden")
    section = st.session_state['section']
    show_section(topic, chapter, section)

    st.button("돌아가기", on_click=update_session_state, args=('go_back',))

### pandas에서 사용할 타이타닉 데이터셋

def pandas_dataset():
        st.subheader('실습에 사용할 데이터셋')
        with st.echo():
            import seaborn as sns
            df = sns.load_dataset('titanic')
            df

        st.subheader('**컬럼(columns) 설명**')
        st.markdown('- survived: 생존여부 (1: 생존, 0: 사망)\n'
                    '- pclass: 좌석 등급 (1등급, 2등급, 3등급)\n'
                    '- sex: 성별\n'
                    '- age: 나이\n'
                    '- sibsp: 형제 + 배우자 수\n'
                    '- parch: 부모 + 자녀 수\n'
                    '- fare: 좌석 요금\n'
                    '- embarked: 탑승 항구 (S, C, Q)\n'
                    '- class: pclass와 동일\n'
                    '- who: 남자(man), 여자(woman), 아이(child)\n'
                    '- adult_male: 성인 남자 여부\n'
                    '- deck: 데크 번호 (알파벳 + 숫자 혼용)\n'
                    '- embark_town: 탑승 항구 이름\n'
                    '- alive: 생존여부 (yes, no)\n'
                    '- alone: 혼자 탑승 여부\n')
        st.divider()

###########################################

def show_section(topic, chapter, section):
    st.write(f"path : {topic}  / {chapter} / {section}")
    path = (topic, chapter, section)
    idx = IndexAllocator()

    ### 컨텐츠 작성
    if path == ("파이썬 기초", "대단원 01", "소단원01") :
        st.write("예시코드 1")
    
        with st.echo():
            import pandas as pd
            df = pd.DataFrame()
        st.divider()

        st.write("예시코드 1")
        with st.echo():
            import pandas as pd
            df = pd.DataFrame()
        st.divider()
    
    ### 컨텐츠 작성
    elif path == ("Pandas 기초", "DataFrame", "데이터프레임 생성") :
        idx.nextSection()

        st.header(f"{idx.getSectionIdx()}데이터프레임 생성") ## 소단원01

        st.markdown('- 2차원 데이터 구조 (Excel 데이터 시트와 비슷합니다.) \n'
            '- 행(row), 열(column)으로 구성되어 있습니다. \n' 		# 공백 2칸
            '- 각 열(column)은 각각의 데이터 타입 (dtype)을 가집니다. \n' 		# 공백 2칸
            )
        
        st.subheader(f"{idx.getIdx()}list 통한 생성")
        st.markdown("**list 를 통해 생성**할 수 있습니다. DataFrame을 만들 때는 **2차원 list를 대입**합니다.")
        with st.echo():
            import pandas as pd
            df = pd.DataFrame([[1,2,3],
                        [4,5,6],
                        [7,8,9]])
            df

        st.divider()
        st.markdown("**columns를 지정**하면, DataFrame의 각 열에 대한 컬럼명이 붙습니다.")
        with st.echo():
            import pandas as pd
            df = pd.DataFrame([[1, 2, 3], 
                            [4, 5, 6], 
                            [7, 8, 9]], columns=['가', '나', '다'])
            df

        st.divider()
        st.subheader(f"{idx.getIdx()}dictionary 통한 생성")
        st.markdown('**dictionary를 통한 생성**도 가능합니다.\n'
                    'dictionary의 **key 값이 자동으로 column 명으로 지정**되어 편리합니다.')
        with st.echo():
            import pandas as pd
            data = {
                'name': ['Kim', 'Lee', 'Park'], 
                'age': [24, 27, 34], 
                'children': [2, 1, 3]
            }
            df = pd.DataFrame(data)
            df


        st.divider()

        idx.nextSection()
        st.header(f"{idx.getSectionIdx()}데이터프레임 속성") # 소단원02

        st.markdown('DataFrame은 다음과 같은 **속성**을 가집니다.\n'
                    '- **index**: index (기본 값으로 RangeIndex)\n'
                    '- **columns**: column 명\n'
                    '- **values**: numpy array 형식의 데이터 값\n'
                    '- **dtypes**: column 별 데이터 타입\n')

        with st.echo():
            import pandas as pd
            data = {
                'name': ['Kim', 'Lee', 'Park'], 
                'age': [24, 27, 34], 
                'children': [2, 1, 3]
            }
            df = pd.DataFrame(data)

        st.divider()

        st.subheader(f"{idx.getIdx()}df.index")
        st.write('''데이터프레임의''', '**인덱스(행)**','''을 출력합니다.''')
        with st.echo():
            df.index
        st.divider()

        st.subheader(f"{idx.getIdx()}df.columns")
        st.write("데이터프레임의", "**컬럼(열)**", "을 출력합니다.")
        with st.echo():
            df.columns
        st.divider()

        st.subheader(f"{idx.getIdx()}df.values")
        st.write("데이터프레임의 **데이터 값** 을 출력합니다.")
        with st.echo():
            df.values
        st.divider()

        st.subheader(f"{idx.getIdx()}df.dtypes")
        st.write("데이터프레임의 **데이터 타입** 을 출력합니다.")
        with st.echo():
            df.dtypes
        st.divider()

        idx.nextSection()
        st.header(f"{idx.getSectionIdx()}데이터프레임 조회") ## 소단원03

        st.write('데이터프레임(DataFrame)에서 가장 많이 사용하는 **조회, 정렬 그리고 조건필터**에 대해 알아보겠습니다.')
        st.write('조회, 정렬, 조건필터 기능은 엑셀에서도 가장 많이 활용하는 기능입니다.')
        st.write('Pandas는 조회, 정렬, 조건필터의 기능을 매우 편리하게 사용할 수 있도록 지원합니다.')
        st.divider()

        pandas_dataset()

        st.subheader(f"{idx.getIdx()}head() 앞 부분 / tail() 뒷 부분 조회")
        st.write('- default 옵션 값으로 **5개의 행이 조회**됩니다.')
        st.write('- 괄호 안에 숫자를 넣어 명시적으로 조회하고 싶은 행의 갯수를 지정할 수 있습니다.')
        
        import seaborn as sns
        df = sns.load_dataset('titanic')
        import io
        st.code('''df.head()''')
        st.write(df.head())
        
        st.code('''df.tail()''')
        
        st.write(df.tail())
        st.divider()

        with st.echo():
            df.head(3)

        st.write(df.head(3))
        st.divider()

        st.code('''df.tail(7)''')
        st.write(df.tail(7))
        st.divider()

        st.subheader(f"{idx.getIdx()}info()")
        st.write('- 컬럼별 정보(information)를 보여줍니다.')
        st.write('- 데이터의 갯수, 그리고 데이터 타입(dtype)을 확인할 때 사용합니다.')
        st.code('''df.info()''')
        buffer = io.StringIO()
        df.info(buf=buffer)
        s = buffer.getvalue()
        st.text(s)

        st.write('- **object** 타입은 쉽게 문자열이라고 생각하면 됩니다.')
        st.write('''- **category** 타입도 있습니다. category 타입은 문자열이지만, '남자' / '여자'처럼 카테고리화 할 수 있는 컬럼을 의미 합니다''')
        st.divider()

        st.subheader(f"{idx.getIdx()}value_counts()")
        st.write('- column 별 **값의 분포를 확인**할 때 사용합니다.')
        st.write('- **남자, 여자, 아이의 데이터 분포를 확인**하고 싶다면 다음과 같이 실행합니다.')

        with st.echo():
            df['who'].value_counts()
        st.write(df['who'].value_counts())
        st.divider()

        st.subheader(f"{idx.getIdx()}Attributes : 속성")
        st.write('속성 값은 **함수형으로 조회하지 않습니다.**')
        st.write('자주 활용하는 DataFrame은 **속성 값**들은 다음과 같습니다.')
        st.markdown('- ndim\n' '- shape\n' '- index\n' '- columns\n' '- values\n')
        st.divider()

        st.write('**차원**을 나타냅니다. DataFrame은 2가 출력됩니다.')
        with st.echo():
            df.ndim
        st.divider()

        st.write('**(행, 열)** 순서로 출력됩니다.')
        with st.echo():
            df.shape
        st.divider()

        st.write('index는 기본 설정된 **RangeIndex**가 출력됩니다.')
        with st.echo():
            df.index
        st.divider()

        st.write('columns **열**을 출력합니다.')
        with st.echo():
            df.columns
        st.divider()

        st.write('values는 모든 값을 출력하며, **numpy array 형식**으로 출력됩니다.')
        with st.echo():
            df.values

        idx.nextSection()
        st.header(f"{idx.getSectionIdx()}데이터프레임 정렬") ## 소단원04

        st.write('데이터프레임(DataFrame)에서 가장 많이 사용하는 **조회, 정렬 그리고 조건필터**에 대해 알아보겠습니다.')
        st.write('조회, 정렬, 조건필터 기능은 엑셀에서도 가장 많이 활용하는 기능입니다.')
        st.write('Pandas는 조회, 정렬, 조건필터의 기능을 매우 편리하게 사용할 수 있도록 지원합니다.')
        st.divider()

        pandas_dataset()

        st.subheader(f"{idx.getIdx()}sort_index: index 정렬")
        st.write('- index 기준으로 정렬합니다. (기본 오름차순이 적용되어 있습니다.)')
        st.write('내림차순 정렬을 적용하려면, :blue-background[ascending=False]를 옵션 값으로 설정합니다.')

        import seaborn as sns
        df = sns.load_dataset('titanic')

        st.code('''df.sort_index().head(5)''')
        st.write(df.sort_index().head(5))
        st.divider()

        st.code('''df.sort_index(ascending=False).head(5)''')
        st.write(df.sort_index(ascending=False).head(5))
        st.divider()

        st.subheader(f"{idx.getIdx()}sort_values: 값에 대한 정렬")
        st.write('- 값을 기준으로 행을 정렬합니다.')
        st.write('- by에 기준이 되는 행을 설정합니다.')
        st.write('- by에 2개 이상의 컬럼을 지정하여 정렬할 수 있습니다.')
        st.write('- 오름차순/내림차순을 컬럼 별로 지정할 수 있습니다.')
        st.code('''df.sort_values(by='age').head()''')
        st.write(df.sort_values(by='age').head())
        st.divider()

        st.write('내림차순 정렬: :blue-background[ascending=False]')
        st.code('''df.sort_values(by='age', ascending=False).head()''')
        st.write(df.sort_values(by='age', ascending=False).head())
        st.divider()

        st.write('**문자열 컬럼도 오름차순/내림차순 정렬이 가능**하며 알파벳 순서로 정렬됩니다.')
        st.code('''df.sort_values(by='class', ascending=False).head()''')
        st.write(df.sort_values(by='class', ascending=False).head())    
        st.divider()

        st.write('**2개 이상의 컬럼**을 기준으로 값 정렬 할 수 있습니다.')
        st.code('''df.sort_values(by=['fare', 'age']).head()''')
        st.write(df.sort_values(by=['fare', 'age']).head())
        st.divider()

        st.write('오름차순/내림차순 정렬도 컬럼 **각각에 지정**해 줄 수 있습니다.')
        st.code('''df.sort_values(by=['fare', 'age'], ascending=[False, True]).head()''')
        st.write(df.sort_values(by=['fare', 'age'], ascending=[False, True]).head())
        st.divider()

        idx.nextSection()
        st.header(f"{idx.getSectionIdx()}Indexing, Slicing, 조건 필터링") ## 소단원05

        st.write('데이터프레임(DataFrame)에서 가장 많이 사용하는 **조회, 정렬 그리고 조건필터**에 대해 알아보겠습니다.')
        st.write('조회, 정렬, 조건필터 기능은 엑셀에서도 가장 많이 활용하는 기능입니다.')
        st.write('Pandas는 조회, 정렬, 조건필터의 기능을 매우 편리하게 사용할 수 있도록 지원합니다.')
        st.divider()

        pandas_dataset()

        import seaborn as sns
        df = sns.load_dataset('titanic')

        st.subheader(f"{idx.getIdx()}loc - indexing / slicing")
        st.write('- indexing과 slicing을 할 수 있습니다.')
        st.write('- slicing은 [**시작(포함): 끝(포함)**] 규칙에 유의합니다. 둘 다 포함 합니다.')

        st.write('**01-1. indexing 예시**')
        st.code('''df.loc[5, 'class']''')
        st.write(df.loc[5, 'class'])
        st.divider()

        st.write('**01-2. fancy indexing 예시**')
        st.code('''df.loc[2:5, ['age', 'fare', 'who']]''')
        st.write(df.loc[2:5, ['age', 'fare', 'who']])
        st.divider()

        st.write('**01-3. slicing 예시**')
        st.code('''df.loc[2:5, 'class':'deck'].head()''')
        st.write(df.loc[2:5, 'class':'deck'].head())

        st.code('''df.loc[:6, 'class':'deck']''')
        st.write(df.loc[:6, 'class':'deck'])
        st.divider()

        st.write('**01-4. loc - 조건 필터**')
        st.write('boolean index을 만들어 조건에 맞는 데이터만 추출해 낼 수 있습니다.')
        st.code('''cond = (df['age'] >= 70)\ncond''')
        cond = (df['age'] >= 70)
        st.write(cond)
        st.divider()
        st.code('''df.loc[cond]''')
        st.write(df.loc[cond])
        st.divider()

        st.write('**01-5. loc - 다중조건**')
        st.write('다중 조건은 먼저 condition(조건)을 정의하고 **&** 와 **|** 연산자로 **복합 조건을 생성**합니다.')
        st.code(
            '''# 조건1 정의\ncond1 = (df['fare'] > 30)\n# 조건2 정의\ncond2 = (df['who'] == 'woman')''')
        cond1 = (df['fare'] > 30)
        cond2 = (df['who'] == 'woman')
        st.code('''df.loc[cond1 & cond2]''')
        st.write(df.loc[cond1 & cond2])
        st.divider()

        st.code('''df.loc[cond1 | cond2]''')
        st.write(df.loc[cond1 | cond2])
        st.divider()

        st.write('**01-6. 조건 필터 후 데이터 대입**')
        st.code('''cond = (df['age'] >= 70)\ncond''')
        cond = (df['age'] >= 70)
        st.write(cond)
        st.divider()
        st.code('''#조건 필터\ndf.loc[cond]''')
        st.write(df.loc[cond])
        st.divider()

        st.write('**01-7. 나이 컬럼**만 가져옵니다.')
        with st.echo():
            df.loc[cond, 'age']
        st.divider()

        st.write('**조건 필터** 후 원하는 값을 대입할 수 있습니다. (단일 컬럼 선택에 유의)')
        with st.echo():
            df.loc[cond, 'age'] = -1
        with st.echo():
            df.loc[cond]
        st.divider()

        st.subheader(f"{idx.getIdx()}iloc")
        st.write('- :blue-background[loc]와 유사하지만, index만 허용합니다.')
        st.write('loc와 마찬가지고, indexing / slicing 모두 가능합니다.')
        st.code('''df.head()''')
        st.write(df.head())
        st.divider()

        st.write('**02-1. indexing**')
        st.code('''df.iloc[1, 3]''')
        st.write(df.iloc[1, 3])
        st.divider()

        st.write('**02-2. Fancy Indexing**')
        st.code('''df.iloc[[0, 3, 4], [0, 1, 5, 6]]''')
        st.write(df.iloc[[0, 3, 4], [0, 1, 5, 6]])
        st.divider()

        st.write('**02-3. Slicing**')
        st.code('''df.iloc[:3, :5]''')
        st.write(df.iloc[:3, :5])
        st.divider()

        st.write('**02-4. isin**')
        st.write('특정 값의 포함 여부는 isin 함수를 통해 비교가 가능합니다. (파이썬의 in 키워드는 사용 불가 합니다.)')
        with st.echo():
            import pandas as pd
            sample = pd.DataFrame({'name': ['kim', 'lee', 'park', 'choi'], 
                                'age': [24, 27, 34, 19]
                            })
            sample
        st.divider()
        st.code('''sample['name'].isin(['kim', 'lee'])''')
        st.write(sample['name'].isin(['kim', 'lee']))

        st.divider()
        st.code('''sample.isin(['kim', 'lee'])''')
        st.write(sample.isin(['kim', 'lee']))
        st.divider()

        st.write(':blue-background[loc] 를 활용한 **조건 필터링**으로도 찰떡궁합입니다.')
        with st.echo():
            condition = sample['name'].isin(['kim', 'lee'])
        with st.echo():
            sample.loc[condition]

    ## Excel/CSV        

    elif path == ("Pandas 기초", "Excel/CSV", "Excel") :
        idx.nextSection()
        
        st.header(f"{idx.getSectionIdx()}Excel") ## 소단원01
        st.subheader(f"{idx.getIdx()}Excel-불러오기") ## 소단원01 - 세부01


        st.write('- Excel 데이터를 바로 읽어들일 수 있습니다. sheet_name 지정시 해당 sheet를 가져옵니다.\n'
                    '''- [참고] :blue-background[pd.read_excel()]로 데이터 로드시 에러 발생한다면 engine='openpyxl'을 추가합니다.''' 
                    )
        st.divider()
        st.write('**철도 Sheet의 데이터 불러오기**')

        with st.echo():
            import pandas as pd
            excel = pd.read_excel('data/서울시대중교통/seoul_transportation.xlsx', 
                                sheet_name='철도')
            excel.head()
        
        
        import pandas as pd
        excel = pd.read_excel('data/서울시대중교통/seoul_transportation.xlsx', 
                                sheet_name='철도')
        st.write(excel.head())

        st.divider()

        st.write('**버스 Sheet의 데이터 불러오기**')

        with st.echo():
            import pandas as pd
            excel = pd.read_excel('data/서울시대중교통/seoul_transportation.xlsx', 
                                sheet_name='버스', engine='openpyxl')
            excel.head()
        excel = pd.read_excel('data/서울시대중교통/seoul_transportation.xlsx', 
                                sheet_name='버스', engine='openpyxl')
        st.write(excel.head())
        st.divider()
        st.markdown(''':blue-background[sheet_name]을 None으로 지정하면 모든 sheet를 가지고 옵니다.''')
                    
        st.write('가지고 올 때는 OrderedDict로 가져오며, :blue-background[keys()]로 시트명을 조회할 수 있습니다.')
        with st.echo():
            import pandas as pd
            excel = pd.read_excel('data/서울시대중교통/seoul_transportation.xlsx', 
                                sheet_name=None, engine='openpyxl')
            excel

        st.divider()
        st.markdown(':blue-background[keys()]를 통해 엑셀이 포함하고 있는 시트를 조회할 수 있습니다.')
        with st.echo():
            excel.keys()
        st.write(excel.keys())
        st.divider()

        st.subheader(f"{idx.getIdx()}Excel-저장하기") ## 소단원01 - 세부02

        st.write('DataFrame을 Excel로 저장할 수 있으며, Excel로 저장시 **파일명**을 지정합니다.\n'
                    '- index=False 옵션은 가급적 꼭 지정하는 옵션입니다. 지정을 안하면 **index가 별도의 컬럼으로 저장**되게 됩니다.\n'
                    '- sheet_name을 지정하여, 저장할 시트의 이름을 변경할 수 있습니다.\n'
                    )
        st.divider()

        with st.echo():
            import pandas as pd
            excel = pd.read_excel('data/서울시대중교통/seoul_transportation.xlsx', sheet_name='철도', engine='openpyxl')
            excel.head()
        st.write(excel.head())
            
        st.divider()
        

        st.write('**시트명 없이 저장**')
        code = '''excel.to_excel('sample.xlsx', index=True)'''
        st.code(code, language="python")
        st.write('현재 디렉터리에서 sample.xlsx가 저장된 것을 확인할 수 있습니다.')
        st.divider()
        
        st.write('**시트명 지정하여 저장**')
        code = '''excel.to_excel('sample1.xlsx', index=False, sheet_name='샘플')'''
        st.write('현재 디렉터리에서 sample1.xlsx가 저장된 것을 확인할 수 있습니다.')
        st.code(code, language="python")
        st.divider()

        idx.nextSection()
        st.header(f"{idx.getSectionIdx()}CSV") ## 소단원02

        st.write('한 줄이 한 개의 행에 해당하며, 열 사이에는 **쉼표(,)를 넣어 구분**합니다.\n')
        st.write('Excel보다 훨씬 가볍고 **차지하는 용량이 적기 때문에 대부분의 파일 데이터는 csv 형태**로 제공됩니다.')

        st.subheader(f"{idx.getIdx()}CSV-불러오기") ## 소단원02- 세부01
        with st.echo():
            import pandas as pd
            df = pd.read_csv('data/서울시주민등록인구/seoul_population.csv')
            df
        st.divider()

        st.subheader(f"{idx.getIdx()}CSV-저장하기") ## 소단원02 - 세부02
        st.markdown('저장하는 방법은 excel과 유사합니다.\n'
                    '다만, csv파일 형식에는 sheet_name 옵션은 없습니다.')

        with st.echo():
            import pandas as pd
            df = pd.read_csv('data/서울시주민등록인구/seoul_population.csv')
            df
        st.divider()

        st.write(''':blue-background[to_csv()]로 csv 파일형식으로 저장할 수 있습니다.''')
        code='''df.to_csv('sample.csv', index=False)'''
        st.code(code, language="python")
        st.write('현재 디렉터리에서 sample.csv가 저장된 것을 확인할 수 있습니다.')
        st.divider()

        st.markdown("읽어드린 **Excel 파일도 csv**로 저장할 수 있습니다.")
        with st.echo():
            import pandas as pd
            excel = pd.read_excel('data/서울시대중교통/seoul_transportation.xlsx', 
                                sheet_name='버스')
        code = '''excel.to_csv('sample1.csv', index=False)'''
        st.code(code, language="python")
        st.write('현재 디렉터리에서 sample1.csv가 저장된 것을 확인할 수 있습니다.')
        st.divider()

    elif path == ("Pandas 기초", "Data 전처리", "데이터 복사"):
        idx.nextSection()
        st.header(f"{idx.getSectionIdx()}데이터 복사") ## 소단원01
        
        st.write('Pandas DataFrame의 **복사(Copy), 결측치 처리**, 그리고 row, column의 **추가, 삭제, 컬럼간 연산, 타입의 변환**을 다뤄보겠습니다.')
        st.divider()

        pandas_dataset()

        import seaborn as sns
        df = sns.load_dataset('titanic')

        st.write('DataFrame을 **복제**합니다. 복제한 DataFrame을 수정해도 **원본에는 영향을 미치지 않습니다.**')
        code = '''df.head()'''
        st.code(code)
        st.write(df.head())
        st.divider()

        st.write(':blue-background[copy()]로 DataFrame을 복제합니다.')
        code = '''df_copy = df.copy()'''
        st.code(code)
        code = '''df_copy.head()'''
        st.code(code)
        df_copy = df.copy()
        st.write(df_copy.head())
        st.divider()

        st.write(':blue-background[df_copy]의 :blue-background[age]를 99999로 임의 수정하도록 하겠습니다.')
        code = '''df_copy.loc[0, 'age'] = 99999'''
        st.code(code)
        df_copy.loc[0, 'age'] = 99999
        st.write('수정사항이 반영된 것을 확인할 수 있습니다.')
        code = '''df_copy.head()'''
        st.code(code)
        st.write(df_copy.head())
        st.divider()

        st.write('하지만, 원본 DataFrame의 **데이터는 변경되지 않고 그대로 남아** 있습니다.')
        code = 'df.head()'
        st.code(code)
        st.write(df.head())
        st.divider()

        idx.nextSection()
        st.header(f"{idx.getSectionIdx()}데이터 결측치") ## 소단원02

        import seaborn as sns
        df = sns.load_dataset('titanic')


        st.write('결측치는 **비어있는 데이터**를 의미합니다.')
        st.write('결측치에 대한 처리는 매우 중요합니다.')
        st.write('결측치에 대한 처리를 해주려면 **다음의 내용**을 반드시 알아야 합니다.')
        st.write('1. 결측 데이터 확인')
        st.write('2. 결측치가 **아닌** 데이터 확인')
        st.write('3. 결측 데이터 **채우기**')
        st.write('4. 결측 데이터 **제거하기**')
        st.divider()

        st.subheader(f"{idx.getIdx()}결측치 확인 - isnull(), isnan()")
        st.write('컬럼(column)별 결측치의 갯수를 확인하기 위해서는 :blue-background[sum()] 함수를 붙혀주면 됩니다.')
        st.write(':blue-background[sum()]은 Pandas의 통계 관련 함수이며, 통계 관련 함수는 **Static** 챕터에서 알 수 있습니다.')
        st.divider()
        st.write('**isnull()**')
        
        code = 'df.isnull().sum()'
        st.code(code)
        st.write(df.isnull().sum())
        st.divider()

        st.write('**isna()**')
        st.write('isnull() 과 동작이 완전 같습니다. 편한 것으로 써주세요. (심지어 도큐먼트도 같습니다)')
        code ='df.isna().sum()'
        st.code(code)
        st.write(df.isna().sum())
        st.divider()

        st.write('DataFrame 전체 결측 데이터의 갯수를 합산하기 위해서는 :blue-background[sum()]을 두 번 사용하면 됩니다.')
        code = 'df.isnull().sum().sum()'
        st.code(code)
        st.write(df.isnull().sum().sum())    
        st.divider()

        st.subheader(f"{idx.getIdx()}결측치가 아닌 데이터 확인 - notnull()")
        st.write(':blue-background[notnull()]은 :blue-background[isnull()]과 정확히 **반대** 개념입니다.')
        code = 'df.notnull().sum()'
        st.code(code)
        st.write(df.notnull().sum())
        st.divider()

        st.subheader(f"{idx.getIdx()}결측 데이터 필터링")

        st.write(':blue-background[isnull()] 함수가 결측 데이터를 찾는 **boolean index** 입니다.')
        st.write('즉, :blue-background[loc]에 적용하여 조건 필터링을 걸 수 있습니다.')
        code = '''df.loc[df['age'].isnull()]'''
        st.code(code)
        st.write(df.loc[df['age'].isnull()])
        st.divider()

        st.subheader(f"{idx.getIdx()}결측치 채우기 - fillna()")
        st.write(':blue-background[fillna()]를 활용하면 결측치에 대하여 일괄적으로 값을 채울 수 있습니다.')
        code = ''' # 다시 원본 DataFrame 로드\ndf = sns.load_dataset('titanic')'''
        st.code(code)
        df = sns.load_dataset('titanic')
        code = '''# 원본을 copy하여 df1 변수에\ndf1 = df.copy()'''
        st.code(code)
        df1 = df.copy()    
        code = '''df1.tail()'''
        st.code(code)
        st.write(df1.tail())
        st.divider()

        st.write('888번 index의 **결측치가 700으로 채워**진 것을 확인할 수 있습니다.')
        code = '''df1['age'].fillna(700).tail()'''
        st.code(code)
        st.write(df1['age'].fillna(700).tail())
        st.divider()

        st.write('df1에 **결측치를 700**으로 채우고 저장합니다.')
        code = '''df1['age'] = df1['age'].fillna(700)'''
        st.code(code)
        df1['age'] = df1['age'].fillna(700)
        code = 'df1.tail()'
        st.code(code)
        st.write(df1.tail())    
        st.divider()

        st.subheader(f"{idx.getIdx()}통계값으로 채우기")
        code = '''df1 = df.copy()'''
        st.code(code)
        df1 = df.copy()
        code = 'df1.tail()'
        st.code(code)
        st.write(df1.tail())
        st.divider()

        st.write('**05-1. 평균으로 채우기**')
        code = '''df1['age'].fillna(df1['age'].mean()).tail()'''
        st.code(code)
        st.code(df1['age'].fillna(df1['age'].mean()).tail())
        st.divider()

        st.write('**05-2. 최빈값으로 채우기**')
        code = '''df1['deck'].mode()'''
        st.code(code)
        st.write(df1['deck'].mode())
        st.divider()

        st.write('''최빈값(mode)으로 채울 때에는 반드시 **0번째 index 지정**하여 값을 추출한 후 채워야 합니다.''')
        code = '''df1['deck'].mode()[0]'''
        st.code(code)
        st.write(df1['deck'].mode()[0])
        st.divider()
                    
        code = '''df1['deck'].fillna(df1['deck'].mode()[0]).tail()'''
        st.code(code)
        st.write(df1['deck'].fillna(df1['deck'].mode()[0]).tail())
        
        st.divider()

        st.subheader(f"{idx.getIdx()}NaN 값이 있는 데이터 제거하기 (dropna)")
        code = '''df1 = df.copy()
            df1.tail()'''
        st.code(code)
        df1 = df.copy()
        st.write(df1.tail())

        code = 'df1.tail()'
        st.code(code)
        st.write(df1.tail())
        st.divider()

        st.write(''':blue-background[dropna()]로 **1개 라도 NaN 값이 있는 행**은 제거할 수 있습니다. :blue-background[(how='any')]''')
        code = '''df1.dropna()'''
        df1.dropna()
        st.write(df1)
        st.divider()

        st.write('기본 옵션 값은 :blue-background[how=any]로 설정되어 있으며, 다음과 같이 변경할 수 있습니다.')
        st.write('- **any**: 1개 라도 NaN값이 존재시 drop')

        st.write('- **all**: 모두 NaN값이 존재시 drop')
        code = '''df1.dropna(how='all')'''
        st.code(code)
        df1.dropna(how='all')
        st.write(df1)

        idx.nextSection()
        st.header(f"{idx.getSectionIdx()}column 추가") ## 소단원03

        st.subheader(f"{idx.getIdx()}새로운 column 추가") 

        import seaborn as sns
        df = sns.load_dataset('titanic')
        import numpy as np

        code = '''df1 = df.copy()'''
        st.code(code)
        df1 = df.copy()
        code = '''df1.head()'''
        st.code(code)
        st.write(df1.head())
        st.divider()

        st.write('임의의 값을 대입하여 새로운 컬럼을 추가할 수 있습니다.')
        code = '''df1['VIP'] = True'''
        st.code(code)
        df1['VIP'] = True
        code = '''df1.head()'''
        st.code(code)
        st.write(df1.head())
        st.divider()

        st.write('중간에 컬럼을 추가하고 싶은 경우 :blue-background[insert()]를 활용할 수 있습니다.')
        st.write(':blue-background[insert(컬럼인덱스, 컬럼명, 값)]')
        st.code('''df1.insert(5, 'RICH', df1['fare'] > 100)''')
        st.write('- 5번째 위치에 RICH 컬럼을 추가')
        st.write('- fare 컬럼이 100보다 크면 True, 작으면 False 값을 채웁니다.')
        df1.insert(5, 'RICH', df1['fare'] > 100)
        code = '''df1.head()'''
        st.code(code)
        st.write(df1.head())
        st.divider()

        idx.nextSection()
        st.header(f"{idx.getSectionIdx()}데이터 삭제") ## 소단원04
        import seaborn as sns
        df = sns.load_dataset('titanic')
        df1 = df.copy()
        import numpy as np

        st.write('삭제는 **행(row) 삭제와 열(column) 삭제**로 구분할 수 있습니다.')
        st.divider()

        st.subheader(f"{idx.getIdx()}행 (row) 삭제")
        st.write('행 삭제시 **index를 지정하여 삭제**합니다.')
        
        code = 'df1.drop(1)'
        st.code(code)
        st.write(df1.drop(1))
        
        st.divider()
        st.write('행 삭제시 **범위를 지정하여 삭제**할 수 있습니다.')
        code = 'df1.drop(np.arange(10))'
        st.code(code)
        st.write(df1.drop(np.arange(10)))

        st.write('**fancy indexing**을 활용하여 삭제할 수 있습니다.')
        code = 'df1.drop([1, 3, 5, 7, 9])'
        st.code(code)
        st.write(df1.drop([1, 3, 5, 7, 9]))
            
        st.divider()

        st.subheader(f"{idx.getIdx()}열 (column) 삭제")
        st.code('df1.head()')
        st.write(df1.head())
        st.divider()

        st.write('열 삭제시 **반드시** :blue-background[axis=1] **옵션을 지정**해야 합니다. 2번째 위치에 지정시 :blue-background[axis=]을 생략할 수 있습니다.')
        st.code('''df1.drop('class', axis=1).head()''')
        st.write(df1.drop('class', axis=1).head())
        st.divider()

        st.write('**다수의 컬럼(column) 삭제**도 가능합니다.')
        st.code('''df1.drop(['who', 'deck', 'alive'], axis=1)''')
        st.write(df1.drop(['who', 'deck', 'alive'], axis=1))
        st.divider()

        st.write('삭제된 내용을 바로 적용하려면')
        st.write('1. :blue-background[inplace=True]를 지정합니다.')
        st.write('2. 변수에 **재대입** 하여 결과를 반영합니다.')
        st.code('''df1.drop(['who', 'deck', 'alive'], axis=1, inplace=True)''')
        df1.drop(['who', 'deck', 'alive'], axis=1, inplace=True)
        st.code('df1.head()')
        st.write(df1.head())

        idx.nextSection()
        st.header(f"{idx.getSectionIdx()}column 연산")

        st.write('**컬럼(column) 과 컬럼 사이의 연산을 매우 쉽게 적용**할 수 있습니다.')
        
        import seaborn as sns
        df = sns.load_dataset('titanic')
        df1 = df.copy()

        st.code('''# 데이터프레임 복제\ndf1 = df.copy()''')
        st.write('**family(가족)**','의 총합은 **sibsp**컬럼과 **parch**의 합산으로 구할 수 있습니다.')

        st.code('''df1['family'] = df1['sibsp'] + df1['parch']''')
        df1['family'] = df1['sibsp'] + df1['parch']
        st.code('df1.head()')
        st.write(df1.head())
        st.divider()

        st.write('컬럼간 연산시 :blue-background[round()]를 사용하여 소수점 자릿수를 지정할 수 있습니다.')
        st.write('**round(숫자, 소수 몇 째자리)**')
        st.code('''df1['round'] = round(df1['fare'] / df1['age'], 2)''')
        df1['round'] = round(df1['fare'] / df1['age'], 2)
        st.code('df1.head()')
        st.write(df1.head())
        st.divider()

        st.write('연산시 1개의 컬럼이라도 **NaN 값을 포함하고 있다면 결과는 NaN** 이 됩니다.')
        st.code('''df1.loc[df1['age'].isnull(), 'deck':].head()''')
        st.write(df1.loc[df1['age'].isnull(), 'deck':].head())
        st.divider()
    
        idx.nextSection()
        st.header(f"{idx.getSectionIdx()}데이터 변환")

        st.write('- 데이터 변환에서는 category 타입으로 변환하는 방법에 대해 알아보겠습니다.')
        st.write('- category로 변경시 사용하는 메모리를 줄일 수 있습니다.')
        import seaborn as sns
        df = sns.load_dataset('titanic')
        import io
        st.divider()

        st.subheader(f"{idx.getIdx()}category 타입")
        
        st.code('''df1 = df.copy()\ndf1.head(2)''')
        df1 = df.copy()
        st.write(df1.head(2))
        st.divider()
        st.code('df1.info()')
        buffer = io.StringIO()
        df1.info(buf=buffer)
        s = buffer.getvalue()
        st.text(s)
        st.divider()

        st.subheader(f"{idx.getIdx()}category로 변경")
        st.write(':blue-background[category]로 변경시에는 Categories가 같이 출력됩니다.')
        st.code('''df1['who'].astype('category').head()''')
        st.write(df1['who'].astype('category').head())
        st.divider()

        st.write('변경사항을 적용합니다.')
        st.code('''df1['who'] = df1['who'].astype('category')''')
        df1['who'] = df1['who'].astype('category')
        st.divider()
        
        st.write(':blue-background[category]로 변경시 사용하는 메모리도 감소합니다.')
        st.code('df1.info()')
        buffer = io.StringIO()
        df1.info(buf=buffer)
        s = buffer.getvalue()
        st.text(s)
        st.divider()

    

    elif path == ("Pandas 기초", "Data 연결과 병합", "데이터 연결"):
        idx.nextSection()

        import pandas as pd

        st.header(f"{idx.getSectionIdx()}데이터 연결") ## 소단원01

        st.write('여러 개의 DataFrame으로 이루어진 데이터를 합치는 방법인 concat()(연결), merge()(병합)에 대하여 다뤄보겠습니다.')
        st.write('- :blue-background[concat()]은 2개 이상의 DataFrame을 행 혹은 열 방향으로 연결합니다.')
        
        st.divider()

        st.write('**1월부터 6월까지 상반기** 데이터 로드')
        code = '''gas1 = pd.read_csv('data/유가정보/gas_first_2019.csv', encoding='euc-kr')'''
        st.code(code)
        st.code('print(gas1.shape)\ngas1.head()')
        gas1 = pd.read_csv('data/유가정보/gas_first_2019.csv', encoding='euc-kr')
        st.write(gas1.shape)
        st.write(gas1.head())
        
        st.write('**7월 부터 12월 까지 하반기** 데이터 로드')
        code =  '''gas2 = pd.read_csv('data/유가정보/gas_second_2019.csv', encoding='euc-kr')'''
        gas2 = pd.read_csv('data/유가정보/gas_second_2019.csv', encoding='euc-kr')
        code = '''print(gas2.shape)\ngas2.head()'''    
        st.write(gas2.shape)
        st.write(gas2.head())

        st.divider()

        st.write(':blue-background[concat()]은 DataFrame을 연결합니다.')
        st.write('단순하게 지정한 DataFrame을 이어서 연결합니다.')
        st.divider()

        st.subheader(f"{idx.getIdx()}행 방향으로 연결")
        st.write('기본 값인 :blue-background[axis=0]이 지정되어 있고, 행 방향으로 연결합니다.')
        st.write('또한, 같은 column을 알아서 찾아서 데이터를 연결합니다.')

        st.code('pd.concat([gas1, gas2])')
        st.write(pd.concat([gas1, gas2]))
        st.divider()

        st.write('연결시 위와 같이 index가 초기화가 되지 않아 **전체 DataFrame의 개수와 index가 맞지 않는** 모습입니다.')
        st.code('''pd.concat([gas1, gas2]).iloc[90588:90593]''')
        st.write(pd.concat([gas1, gas2]).iloc[90588:90593])
        st.divider()

        st.write('연결 하면서 **index를 무시하고 연결** 할 수 있습니다.')
        st.code('''gas = pd.concat([gas1, gas2], ignore_index=True)\ngas''')
        gas = pd.concat([gas1, gas2], ignore_index=True)
        st.code('gas')
        st.write(gas)
        st.divider()

        st.write('합치고자 하는 데이터프레임의 **일부 컬럼이 누락되거나 순서가 바뀌어도** 알아서 같은 컬럼끼리 병합합니다.')
        code = '''gas11 = gas1[['지역', '주소', '상호', '상표', '휘발유']]\ngas22 = gas2[['상표', '번호', '지역', '상호', '주소', '경유', '휘발유']]'''
        st.code(code)
        gas11 = gas1[['지역', '주소', '상호', '상표', '휘발유']]
        gas22 = gas2[['상표', '번호', '지역', '상호', '주소', '경유', '휘발유']]
        st.code('gas11.head()')
        st.write(gas11.head())

        st.code('gas22.head()')
        st.write(gas22.head())
        st.divider()
        st.code('pd.concat([gas11, gas22], ignore_index=True)')
        st.write(pd.concat([gas11, gas22], ignore_index=True))
        st.divider()

        st.subheader(f"{idx.getIdx()}열 방향으로 연결")
        st.write('열(column) 방향으로 연결 가능하며, :blue-background[axis=1]로 지정합니다.')
        code='''# 실습을 위한 DataFrame 임의 분할\n +
            gas1 = gas.iloc[:, :5]\n +
            gas2 = gas.iloc[:, 5:]'''
        gas1 = gas.iloc[:, :5]
        gas2 = gas.iloc[:, 5:]
        st.code('gas1.head()')
        st.write(gas1.head())
        st.divider()
        st.code('gas2.head()')
        st.write(gas2.head())
        st.divider()

        st.write('같은 index 행끼리 연결됩니다.')
        st.code('pd.concat([gas1, gas2], axis=1)')
        st.write(pd.concat([gas1, gas2], axis=1))
        
        idx.nextSection()
        st.header(f"{idx.getSectionIdx()}데이터 병합") ## 소단원02
        import pandas as pd

        st.write('여러 개의 DataFrame으로 이루어진 데이터를 합치는 방법인 concat() - 연결, merge() - 병합에 대하여 알아보겠습니다.')
        st.write('- :blue-background[merge()]는 2개의 DataFrame을 특정 key를 기준으로 병합할 때 활용하는 메서드입니다.')

        st.write('서로 **다른 구성의 DataFrame이지만, 공통된 key값(컬럼)을 가지고 있다면 병합**할 수 있습니다.')
        with st.echo():
            df1 = pd.DataFrame({
            '고객명': ['박세리', '이대호', '손흥민', '김연아', '마이클조던'],
            '생년월일': ['1980-01-02', '1982-02-22', '1993-06-12', '1988-10-16', '1970-03-03'],
            '성별': ['여자', '남자', '남자', '여자', '남자']})
            df1
        

        with st.echo():
            df2 = pd.DataFrame({
            '고객명': ['김연아', '박세리', '손흥민', '이대호', '타이거우즈'],
            '연봉': ['2000원', '3000원', '1500원', '2500원', '3500원']})
            df2
        st.divider()
        with st.echo():
            pd.merge(df1, df2)
        st.write(pd.merge(df1, df2))
        
        st.divider()

        st.subheader(f"{idx.getIdx()}병합하는 방법 4가지")

        st.write(':blue-background[how] 옵션 값을 지정하여 4가지 방식으로 병합을 할 수 있으며, 각기 다른 결과를 냅니다.')
        st.write('''- **how** : '{':blue-background[left], :blue-background[right], :blue-background[outer], :blue-background[inner]'}',''')
        st.write('- **default**로 설정된 값은 :blue-background[inner] 입니다.')
        st.code('''# how='inner' 입니다.\npd.merge(df1, df2)''')
        st.write(pd.merge(df1, df2))
        st.divider()

        st.code('''pd.merge(df1, df2, how='left')''')
        st.write(pd.merge(df1, df2, how='left'))
        st.divider()

        st.code('''pd.merge(df1, df2, how='right')''')
        st.write(pd.merge(df1, df2, how='right'))
        st.divider()

        st.code('''pd.merge(df1, df2, how='outer')''')
        st.write(pd.merge(df1, df2, how='outer'))
        st.divider()

        st.subheader(f"{idx.getIdx()}병합하려는 컬럼의 이름이 다른 경우")
        with st.echo():
            df1 = pd.DataFrame({
            '이름': ['박세리', '이대호', '손흥민', '김연아', '마이클조던'],
            '생년월일': ['1980-01-02', '1982-02-22', '1993-06-12', '1988-10-16', '1970-03-03'],
            '성별': ['여자', '남자', '남자', '여자', '남자']})
            df1
        st.divider()

        with st.echo():
            df2 = pd.DataFrame({
            '고객명': ['김연아', '박세리', '손흥민', '이대호', '타이거우즈'],
            '연봉': ['2000원', '3000원', '1500원', '2500원', '3500원']})
            df2
        st.divider()

        st.write(':blue-background[left_on]과 :blue-background[right_on]을 지정합니다.')
        st.write('이름과 고객명 컬럼이 모두 drop되지 않고 살아 있음을 확인할 수 있습니다.')
        code = '''pd.merge(df1, df2, left_on='이름', right_on='고객명')'''
        st.code(code)
        st.write(pd.merge(df1, df2, left_on='이름', right_on='고객명'))

    elif path == ("Pandas 기초", "Static", "기술 통계"):
        idx.nextSection()
        
        st.header(f"{idx.getSectionIdx()}기술 통계") # 소단원01

        st.write('**통계**는 데이터 분석에서 굉장히 중요한 요소입니다.')
        st.write('데이터에 대한 통계 계산식을 Pandas 함수로 제공하기 때문에 쉽게 통계 값을 산출할 수 있습니다.')

        pandas_dataset()

        import pandas as pd
        import seaborn as sns
        df = sns.load_dataset('titanic')
        # for col in df.select_dtypes(include=['object']):
        #     df[col] = df[col].astype('category')

        st.subheader(f"{idx.getIdx()}describe() - 요약통계")

        st.write('전반적인 주요 통계를 확인할 수 있습니다.')
        st.write('기본 값으로 **수치형(Numberical) 컬럼**에 대한 통계표를 보여줍니다.')

        st.write('- **count**: 데이터 개수')
        st.write('- **mean**: 평균')
        st.write('- **std**: 표준편차')
        st.write('- **min**: 최솟값')
        st.write('- **max**: 최대값')

        code = 'df.describe()'
        st.code(code)
        st.write(df.describe())
        st.divider()

        st.write('**문자열 컬럼에 대한 통계표**도 확인할 수 있습니다.')
        st.write('- **count**: 데이터 개수')
        st.write('- **unique**: 고유 데이터 값 개수')
        st.write('- **top**: 가장 많이 출현한 데이터 개수')
        st.write('- **freq**: 가장 많이 출현한 데이터의 빈도수')

        ## warning 문 뜸
        # st.header('문자열 칼럼에 대한 요약통계')
        st.code('''df.describe(include='object')''')
        st.write(df.describe(include='object'))
        st.divider()

        import seaborn as sns
        # dataset = sns.load_dataset('titanic')
        # # df 결측치 제거
        # df = dataset.dropna()
        df = sns.load_dataset('titanic')
        # for col in df.select_dtypes(include=['object']):
        #     df[col] = df[col].astype('category')

        st.subheader(f"{idx.getIdx()}count() - 개수")

        st.write('데이터의 개수')
        st.write('DataFrame 전체의 개수를 구하는 경우')

        st.code('df.count()')
        st.write(df.count())

        st.write('단일 column의 데이터 개수를 구하는 경우')
        st.code('''df['age'].count()''')
        st.write(df['age'].count())

        st.divider()

        st.subheader('mean() - 평균')

        st.write('데이터의 **평균**')
        st.write('DataFrame 평균')

        st.code('df')
        st.write(df)

        st.write(':blue-background[age] 컬럼에 대한 평균')
        st.code('''df['age'].mean()''')
        st.write(df['age'].mean())

        st.divider()

        st.subheader(f"{idx.getIdx()}mean - 조건별 평균")
        st.write('성인 남성의 나이의 평균 구하기')
        code = '''condition = (df['adult_male'] == True)\ndf.loc[condition, 'age'].mean()'''
        st.code(code)
        condition = (df['adult_male'] == True)
        st.write(df.loc[condition, 'age'].mean()    )

        st.divider()

        st.subheader(f"{idx.getIdx()}median() - 중앙값")
        st.write('데이터의 중앙 값을 출력 합니다. 데이터를 **오름차순 정렬하여 중앙에 위치한 값**입니다.')
        st.write('이상치(outlier)가 존재하는 경우, mean()보다 median()을 대표값으로 더 선호합니다.')

        st.code('pd.Series([1, 2, 3, 4, 5]).median()')
        st.write(pd.Series([1, 2, 3, 4, 5]).median())
        
        st.code('pd.Series([4, 5, 1, 2, 3]).median()')
        st.write(pd.Series([4, 5, 1, 2, 3]).median())

        st.code('pd.Series([1, 2, 3, 4, 5, 6]).median()')
        st.write(pd.Series([1, 2, 3, 4, 5, 6]).median())

        st.write('**짝수** 개의 데이터가 있는 경우에는 **가운데 2개 중앙 데이터의 평균 값을 출력** 합니다.')
        st.code('pd.Series([1, 2, 3, 4, 5, 6]).median()')
        st.write(pd.Series([1, 2, 3, 4, 5, 6]).median())
        st.divider()

        st.write('나이의 평균(mean)과 중앙값(median)은 약간의 **차이가 있음**을 확인할 수 있습니다.')

        code='''print(f"나이 평균: {df['age'].mean():.5f}\n\t나이 중앙값: {df['age'].median()}\n\t차이: {df['age'].mean() - df['age'].median():.5f}")'''
        st.code(code)
        st.write((f"나이 평균: {df['age'].mean():.5f}\n\t나이 중앙값: {df['age'].median()}\n\t차이: {df['age'].mean() - df['age'].median():.5f}"))

        st.divider()

        st.subheader(f"{idx.getIdx()}sum() - 합계")

        st.write('데이터의 **합계**입니다. 문자열 column은 모든 데이터가 붙어서 출력될 수 있습니다.')
        st.code('''df.loc[:, ['age', 'fare']].sum()''')
        st.write(df.loc[:, ['age', 'fare']].sum())

        st.write('단일 column에 대한 **합계 출력**')
        st.code('''df['fare'].sum()''')
        st.write(df['fare'].sum())   

        st.divider()

        st.subheader(f"{idx.getIdx()}var() - 분산")

        st.latex(r'''
        \text{분산} = \frac{\sum_{i=1}^n (X_i - \bar{X})^2}{n-1}
        ''')

        st.code('''
            # 평균
            fare_mean = df['fare'].values.mean()
            # 분산
            my_var = ((df['fare'].values - fare_mean) ** 2).sum() / (df['fare'].count() - 1)
            my_var''')
        fare_mean = df['fare'].values.mean()
        my_var = ((df['fare'].values - fare_mean) ** 2).sum() / (df['fare'].count() - 1)
        st.write(my_var)
        st.divider()
        st.subheader(f"{idx.getIdx()}std() - 표준편차")
        st.latex(r'''
        \text{표준편차} = \sqrt{\text{분산}} = \sqrt{\frac{\sum_{i=1}^n (X_i - \bar{X})^2}{n-1}}
                ''')
        st.write('분산(var)의 제곱근')
        st.code(
            '''import numpy as np\nnp.sqrt(df['fare'].var())''')
        import numpy as np
        st.write(np.sqrt(df['fare'].var()))
        st.code('''df['fare'].std()''')
        st.write(df['fare'].std())
        st.divider()

        st.subheader(f"{idx.getIdx()}min() - 최소값, max() - 최대값")
        st.code(
         '''# 최소값
            df['age'].min()
            # 최대값
            df['age'].max()''')
        st.write(df['age'].min())
        st.write(df['age'].max())
        st.divider()

        st.subheader(f"{idx.getIdx()}mode() - 최빈값")
        st.write('최빈값은 **가장 많이 출현한 데이터**를 의미합니다.')
        st.code('''df['who'].mode()''')
        st.write(df['who'].mode())   

        st.write('카테고리형 데이터에도 적용 가능합니다.')
        st.code('''df['deck'].mode()''')
        st.write(df['deck'].mode())
        st.divider()
        
        idx.nextSection()
        st.header(f"{idx.getSectionIdx()}고급 통계")

        st.write('"고급 통계 함수"는 기술 통계보다 더 복잡한 연산이나 특수한 목적을 가진 함수입니다.')

        pandas_dataset()
        import pandas as pd
        import seaborn as sns
        df = sns.load_dataset('titanic')

        
        st.subheader(f"{idx.getIdx()}agg - aggregation: 통합 통계 적용 (복수의 통계 함수 적용)")
        st.write('단일 컬럼에 agg 적용')
        st.code('''df['age'].agg(['min', 'max', 'count','mean'])''')
        st.write(df['age'].agg(['min', 'max', 'count','mean']))       

        st.write('복수의 컬럼에 agg 적용')
        st.code('''df[['age', 'fare']].agg(['min', 'max', 'count', 'mean'])''')
        st.write(df[['age', 'fare']].agg(['min', 'max', 'count', 'mean']))
    
        st.divider()

        st.subheader(f"{idx.getIdx()}quantile() - 분위")
        st.write('**Quantile이란 주어진 데이터를 동등한 크기로 분할하는 지점**Quantile이란 주어진 데이터를 동등한 크기로 분할하는 지점을 말합니다.')
        st.write('10%의 경우 0.1을, 80%의 경우 0.8을 대입하여 값을 구합니다.')
        st.code('''# 10% quantile\ndf['age'].quantile(0.1)''')
        st.write(df['age'].quantile(0.1))
        st.divider()
        
        st.code('''# 80% quantile\ndf['age'].quantile(0.8)''')
        st.write(df['age'].quantile(0.8))

        st.divider()

        st.subheader(f"{idx.getIdx()}unique() - 고유값, nunique() - 고유값 개수")
        st.write('고유값과 고유값의 개수를 구하고자 할 때 사용합니다.')

        st.write('**unique()**')
        st.code('''df['who'].unique()''')
        st.write(df['who'].unique())   
        st.divider()
        st.write('**nonique()**: 고유값의 개수를 출력합니다.')
        st.code('''df['who'].nunique()''')
        st.write(df['who'].nunique())
        st.divider()

        st.subheader(f"{idx.getIdx()}cumsum() - 누적합, cumprod() - 누적곱")

        st.write('누적되는 합계를 구할 수 있습니다.')
        st.code('''df['age'].cumsum()''')
        st.write(df['age'].cumsum())
        st.divider()

        st.write('누적되는 곱도 구할 수 있으나, 일반적으로 **값이 너무 커지므로 잘 활용하지는 않습니다.**')

        st.code('''df['age'].cumprod()''')
        st.write(df['age'].cumprod())
        st.divider()

        st.subheader(f"{idx.getIdx()}corr() - 상관관계")
        st.write(':blue-background[corr()]로 컬럼(column)별 **상관관계**를 확인할 수 있습니다.')

        st.write('- **-1~1 사이의 범위**를 가집니다.')
        st.write('- **-1에 가까울수록 반비례** 관계, **1에 가까울수록 정비례** 관계를 의미합니다.')
        code = '''
            numeric_df = df[['survived','age', 'pclass','sibsp', 'parch','fare']]
            numeric_df.corr()'''
        st.code(code)
        numeric_df = df[['survived','age', 'pclass','sibsp', 'parch','fare']]
        st.write(numeric_df.corr())

        st.divider()
        st.write('**특정 컬럼에 대한 상관관계**를 확인할 수 있습니다.')
        st.code('''numeric_df.corr()['survived']''')
        st.write(numeric_df.corr()['survived']) 
        st.divider()

        
    elif path == ("Matplotlib 기초", "대단원 01", "소단원01") :
        st.write("예시코드 1")
    
        with st.echo():
            import pandas as pd
            df = pd.DataFrame()
        st.divider()

        st.write("예시코드 1")
        with st.echo():
            import pandas as pd
            df = pd.DataFrame()
        st.divider()
    
    else :
        st.error("Content Not Found !")

def main() :
    page, topic, chapter, section = init_session_state()
    
    if page == 'page_topic':
        show_topic(topic)
    elif page == 'page_chapter':
        show_chapter(topic, chapter)
    
    with st.sidebar:
        option_menu(
            "데이터 분석 역량 강화", 
            TOPICS,
            manual_select = TOPICS.index(topic) if topic in TOPICS else 0,
            key = "change_topic",
            on_change = update_session_state,
            styles={
                "menu-title": {"font-size": "13px", "text-align": "left", "margin":"0px", "--hover-color": "#eee"},
                "nav-link": {"font-size": "13px", "text-align": "left", "margin":"0px", "--hover-color": "#eee"},
                "nav-link-selected": {"background-color": "#RGB(255,99,99)"}
            }
        )

if __name__ == "__main__":
    main()

