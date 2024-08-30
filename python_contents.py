    elif path == ("파이썬 기초", "모듈과 패키지") :
        st.write('''파이썬은 코드의 재사용성과 유지보수성을 높이기 위해 모듈과 패키지라는 개념을 제공합니다. 이를 통해 코드를 논리적으로 분리하고, 필요한 부분만 가져와 사용할 수 있습니다.''')
        st.divider()
        st.header(f"{idx.getHeadIdx()}모듈")
        st.write('''모듈은 파이썬 코드를 논리적으로 그룹화한 파일입니다. :blue-background[.py] 확장자를 가진 파이썬 파일 하나가 하나의 모듈입니다. 모듈은 변수, 함수, 클래스 등을 포함할 수 있으며, 다른 파이썬 코드에서 가져와 사용할 수 있습니다.''')
        st.divider()
        st.subheader(f"{idx.getSubIdx()}모듈 생성과 사용")
        st.write('''모듈을 생성하려면 :blue-background[.py] 파일을 작성하면 됩니다. 예를 들어, :blue-background[mymodule.py]라는 파일을 생성합니다.''')
        st.code('''
# mymodule.py

def greet(name):
    return f"Hello, {name}!"

pi = 3.14159
''', line_numbers=True)
        st.write('''이제 이 모듈을 다른 파이썬 파일에서 사용할 수 있습니다.''')
        st.code('''
# main.py

import mymodule

print(mymodule.greet("Alice"))  # Hello, Alice!
print(mymodule.pi)  # 3.14159
''', line_numbers=True)
        st.divider()
        st.subheader(f"{idx.getSubIdx()}모듈에서 특정 항목 가져오기")
        st.write('''모듈 전체를 가져오는 대신, 필요한 항목만 선택적으로 가져올 수도 있습니다.''')
        st.code('''
# main.py

from mymodule import greet, pi

print(greet("Bob"))  # Hello, Bob!
print(pi)  # 3.14159
''', line_numbers=True)
        st.divider()
        st.header(f"{idx.getHeadIdx()}패키지 생성")
        st.write('''패키지는 관련된 모듈을 그룹화한 디렉토리입니다. 패키지는 모듈을 계층적으로 구성하여 더 큰 프로그램을 체계적으로 관리할 수 있게 합니다. 패키지는 디렉토리 구조로 나타내며, 각 디렉토리는 :blue-background[__init__.py] 파일을 포함하여 패키지로 인식됩니다.''')
        st.divider()

        st.subheader(f"{idx.getSubIdx()}패키지 디렉토리 구조")
        st.code('''
mypackage/
    __init__.py
    module1.py
    module2.py''', line_numbers=True)
        st.divider()
        
        st.subheader(f"{idx.getSubIdx()}각 모듈 파일 작성")
        st.code('''
# module1.py
def func1():
    return "This is function 1"

# module2.py
def func2():
    return "This is function 2"''', line_numbers=True)
        st.divider()
        
        st.subheader(f"{idx.getSubIdx()}패키지 초기화 파일 작성")
        st.write('''__init__.py 파일은 패키지를 초기화하는 데 사용됩니다. 이 파일을 통해 패키지에서 어떤 모듈을 기본적으로 가져올지 정의할 수 있습니다.''')
        st.code('''
# __init__.py
from .module1 import func1
from .module2 import func2''', line_numbers=True)
        st.divider()
        
        st.subheader(f"{idx.getSubIdx()}패키지 사용")
        st.write('''이제 이 패키지를 다른 파이썬 파일에서 사용할 수 있습니다.''')
        st.code('''
# main.py
import mypackage

print(mypackage.func1())  # This is function 1
print(mypackage.func2())  # This is function 2''', line_numbers=True)
        
        st.divider()

        st.header(f"{idx.getHeadIdx()}하위 패키지")
        st.write('''패키지는 하위 패키지를 가질 수 있습니다. 이를 통해 더 복잡한 프로젝트를 구조화할 수 있습니다.''')
        st.divider()

        st.subheader(f"{idx.getSubIdx()}하위 패키지 디렉토리 구조")
        st.code('''
mypackage/
    __init__.py
    subpackage/
        __init__.py
        submodule.py

''')
        st.divider()
        st.subheader(f"{idx.getSubIdx()}하위 패키지 모듈 작성")
        st.code('''
# submodule.py
def sub_func():
    return "This is a subpackage function"
''', line_numbers=True)
        st.divider()
        st.subheader(f"{idx.getSubIdx()}패키지와 하위 패키지 초기화 파일 작성")
        st.code('''
# mypackage/__init__.py
from .subpackage import submodule

# mypackage/subpackage/__init__.py
from .submodule import sub_func
''', line_numbers=True)
        st.divider()
        st.subheader(f"{idx.getSubIdx()}하위 패키지 사용")
        st.code('''
# main.py
from mypackage.subpackage import submodule

print(submodule.sub_func())  # This is a subpackage function
''', line_numbers=True)
        st.divider()

        st.header(f"{idx.getHeadIdx()}모듈과 패키지의 개념")
        st.write('''모듈과 패키지를 사용하여 코드를 구조화하고, 여러 파일에 기능을 분리하여 관리합니다.''')
        st.divider()

        st.subheader(f"{idx.getSubIdx()}모듈 생성")
        st.write(''':blue-background[data_processing.py] 파일에 데이터 처리 관련 함수를 정의합니다.''')
        st.code('''
# data_processing.py

def sort_data(data):
    return sorted(data)

def calculate_average(numbers):
    total = sum(numbers)
    count = len(numbers)
    return total / count

def filter_data(data, condition):
    return list(filter(condition, data))''', line_numbers=True)
        st.divider()

        st.subheader(f"{idx.getSubIdx()}메인 스크립트")
        st.write(''':blue-background[main.py] 파일에서 모듈을 가져와서 사용합니다.''')
        st.code('''
# main.py

import data_processing

data = [5, 2, 9, 1, 5, 6]

# 정렬된 데이터 출력
sorted_data = data_processing.sort_data(data)
print(sorted_data)  # [1, 2, 5, 5, 6, 9]

# 평균 계산
average = data_processing.calculate_average(data)
print(average)  # 4.666666666666667

# 필터링된 데이터 출력
filtered_data = data_processing.filter_data(data, lambda x: x % 2 == 0)
print(filtered_data)  # [2, 6]''', line_numbers=True)
        st.divider()
        
        st.subheader(f"{idx.getSubIdx()}패키지 구성")
        st.write('''여러 모듈을 포함하는 패키지를 생성합니다.''')
        st.code('''
data_processing/
    __init__.py
    sorting.py
    statistics.py
    filtering.py''')
        st.divider()
        st.subheader(f"{idx.getSubIdx()}모듈 내용")
        st.write('''여러 모듈을 포함하는 패키지를 생성합니다.''')
        st.code('''
# sorting.py
def sort_data(data):
    return sorted(data)
''', line_numbers=True)
        st.code('''
# statistics.py
def calculate_average(numbers):
    total = sum(numbers)
    count = len(numbers)
    return total / count
''', line_numbers=True)
        st.code('''
# filtering.py
def filter_data(data, condition):
    return list(filter(condition, data))
''', line_numbers=True)
        st.divider()
        st.subheader(f"{idx.getSubIdx()}패키지 초기화")
        st.write(''':blue-background[__init__.py]파일에서 패키지의 모듈을 임포트합니다.''')
        st.code('''
# __init__.py
from .sorting import sort_data
from .statistics import calculate_average
from .filtering import filter_data
''', line_numbers=True)
        st.divider()
        st.subheader(f"{idx.getSubIdx()}메인 스크립트 수정")
        st.write('''패키지를 가져와서 사용합니다.''')
        st.code('''
# main.py

from data_processing import sort_data, calculate_average, filter_data

data = [5, 2, 9, 1, 5, 6]

# 정렬된 데이터 출력
sorted_data = sort_data(data)
print(sorted_data)  # [1, 2, 5, 5, 6, 9]

# 평균 계산
average = calculate_average(data)
print(average)  # 4.666666666666667

# 필터링된 데이터 출력
filtered_data = filter_data(data, lambda x: x % 2 == 0)
print(filtered_data)  # [2, 6]
''', line_numbers=True)
        st.divider()


    elif path == ("파이썬 기초", "파일입출력") :
        
        st.header(f"{idx.getHeadIdx()}파일 읽기 및 쓰기")
        st.write('파이썬은 파일 입출력 기능을 제공하여 파일에서 데이터를 읽고 쓸 수 있습니다. 이를 통해 외부 파일에 데이터를 저장하거나, 파일로부터 데이터를 불러올 수 있습니다. ')
        st.divider()

        st.subheader(f"{idx.getSubIdx()}파일 열기와 닫기")
        st.write('''파일을 읽거나 쓰기 위해서는 먼저 파일을 열어야 합니다. 파이썬에서는 :blue-background[open()] 함수를 사용하여 파일을 열고, 
                 파일 작업이 끝난 후에는 :blue-background[close()] 메소드를 호출하여 파일을 닫아야 합니다.''')
        
        st.code('''
# 파일 열기
file = open('example.txt', 'w')  # 쓰기 모드로 파일 열기

# 파일 닫기
file.close()
''', line_numbers=True)

        st.write(''':blue-background[open()] 함수는 파일 경로와 모드를 인자로 받습니다. 주요 파일 모드는 다음과 같습니다:''')

        st.write('''- 'r': 읽기 모드''')
        st.write('''- 'w': 쓰기 모드 (파일이 존재하면 내용을 덮어씀)''')
        st.write('''- 'a': 추가 모드 (파일 끝에 내용을 추가)''')
        st.write('''- 'b': 바이너리 모드 (예: 'rb', 'wb'))''')
        st.divider()

        st.subheader(f"{idx.getSubIdx()}파일 쓰기")

        st.write('''파일에 데이터를 쓰려면 :blue-background[write()] 메소드를 사용합니다.''')
        st.code('''
# 파일에 문자열 쓰기
with open('example.txt', 'w') as file:
    file.write("Hello, world!\n")
    file.write("This is a new line.")
''', line_numbers=True)

        st.write('''위 코드에서는 :blue-background[with] 문을 사용하여 파일을 열고, 작업이 끝난 후 자동으로 파일을 닫습니다. 
                 :blue-background[write()] 메소드는 문자열을 파일에 씁니다.''')

        st.divider()
        st.subheader(f"{idx.getSubIdx()}파일 읽기")
        
        st.write('''파일에서 데이터를 읽으려면 :blue-background[read()], :blue-background[readline()], :blue-background[readlines()] 메소드를 사용합니다.''')
        
        st.code('''# 파일 전체 읽기  
with open('example.txt', 'r', encoding='utf-8') as file:  
    content = file.read()  
    print(content)  

# 파일 한 줄씩 읽기  
with open('example.txt', 'r', encoding='utf-8') as file:  
    line = file.readline()  
    while line:  
        print(line, end='')  # 파일 내용 출력 (줄 바꿈 없이)  
  line = file.readline()  

# 파일 전체를 줄 단위로 읽기  
with open('example.txt', 'r', encoding='utf-8') as file:  
    lines = file.readlines()  
    for line in lines:  
        print(line, end='')''', line_numbers=True)
        st.divider()
        st.subheader(f"{idx.getSubIdx()}바이너리 파일 처리")
        st.write('''바이너리 모드를 사용하여 이미지나 오디오 파일과 같은 바이너리 데이터를 처리할 수 있습니다.''')
        st.code('''
# 바이너리 파일 쓰기
with open('example.bin', 'wb') as file:
    file.write(b'\x00\x01\x02\x03\x04')

# 바이너리 파일 읽기
with open('example.bin', 'rb') as file:
    data = file.read()
    print(data)  # b'\x00\x01\x02\x03\x04'
''', line_numbers=True)    
        st.divider()
        st.subheader(f"{idx.getSubIdx()}CSV 파일 처리")

        st.write('''CSV(Comma-Separated Values) 파일은 데이터를 테이블 형식으로 저장하는 데 사용됩니다. 파이썬의 :blue-background[csv] 모듈을 사용하여 CSV 파일을 읽고 쓸 수 있습니다.''')
        st.code('''
import csv

# CSV 파일 쓰기
with open('example.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Name', 'Age', 'City'])
    writer.writerow(['Alice', 30, 'New York'])
    writer.writerow(['Bob', 25, 'Los Angeles'])

# CSV 파일 읽기
with open('example.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)''', line_numbers=True)
        st.divider()
        st.subheader(f"{idx.getSubIdx()}예제: 파일 읽기 및 쓰기")
        st.write('''이번 예제에서는 학생들의 성적 데이터를 CSV 파일로 저장하고, 이를 읽어와서 처리하도록 하겠습니다.''')

        st.code('''
import csv

# 학생 성적 데이터
students = [
    {'name': 'Alice', 'math': 90, 'science': 85, 'english': 88},
    {'name': 'Bob', 'math': 78, 'science': 81, 'english': 92},
    {'name': 'Charlie', 'math': 95, 'science': 89, 'english': 85}
]

# CSV 파일에 학생 성적 데이터 쓰기
with open('students.csv', 'w', newline='') as file:
    writer = csv.DictWriter(file, fieldnames=['name', 'math', 'science', 'english'])
    writer.writeheader()
    for student in students:
        writer.writerow(student)

# CSV 파일에서 학생 성적 데이터 읽기
with open('students.csv', 'r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        print(row)
''', line_numbers=True)
        st.write('''파일 읽기 및 쓰기는 데이터를 영구적으로 저장하고 불러오는 데 필수적인 기능입니다. 파이썬의 파일 입출력 기능을 사용하면 텍스트 파일, 바이너리 파일, CSV 파일 등을 쉽게 처리할 수 있습니다. 이번 섹션에서는 다양한 파일 입출력 기법을 배우고, 이를 실제 프로젝트에 적용하여 학생 성적 데이터를 처리하는 방법을 살펴보았습니다. 이러한 파일 입출력 기법을 잘 활용하면, 다양한 형태의 데이터를 효율적으로 관리하고 처리할 수 있습니다.''')
        st.divider()
        st.header(f"{idx.getHeadIdx()}파일 작업")
        st.write('''파일과 디렉토리 작업은 파일 시스템을 조작하고 관리하는 데 필수적인 기능입니다. 파이썬은 이러한 작업을 수행하기 위해 다양한 내장 모듈과 함수를 제공합니다. 이 섹션에서는 파일과 디렉토리 작업의 기본 개념과 주요 기능을 다루고, 이를 활용하는 방법을 설명합니다.''')
        st.divider()
        

        st.subheader(f"{idx.getSubIdx()}파일 존재 여부 확인")
        st.write('''파일이 존재하는지 확인하려면 :blue-background[os.path] 모듈의 :blue-background[exists()] 함수를 사용합니다.''')
        st.code('''
import os

file_path = 'example.txt'

if os.path.exists(file_path):
    print(f"{file_path} exists.")
else:
    print(f"{file_path} does not exist.")''', line_numbers=True)
        st.divider()
        
        st.subheader(f"{idx.getSubIdx()}파일 삭제")
        st.write('''파일을 삭제하려면 :blue-background[os.remove()] 함수를 사용합니다.''')
        st.code('''
import os

file_path = 'example.txt'

if os.path.exists(file_path):
    os.remove(file_path)
    print(f"{file_path} has been deleted.")
else:
    print(f"{file_path} does not exist.")''', line_numbers=True)
        st.divider()
        st.subheader(f"{idx.getSubIdx()}파일 이름 변경")
        st.write('''파일 이름을 변경하려면 :blue-background[os.rename()] 함수를 사용합니다.''')
        st.code('''import os

old_name = 'old_example.txt'
new_name = 'new_example.txt'

if os.path.exists(old_name):
    os.rename(old_name, new_name)
    print(f"{old_name} has been renamed to {new_name}.")
else:
    print(f"{old_name} does not exist.")''', line_numbers=True)
        st.divider()
        st.header(f"{idx.getHeadIdx()}디렉토리 작업")
        st.divider()
        st.subheader(f"{idx.getSubIdx()}디렉토리 생성")
        st.write('''디렉토리를 생성하려면 :blue-background[os.makedirs()] 또는 :blue-background[os.mkdir()] 함수를 사용합니다.''')
        st.code('''
import os

directory = 'example_dir'

if not os.path.exists(directory):
    os.makedirs(directory)
    print(f"{directory} has been created.")
else:
    print(f"{directory} already exists.")''', line_numbers=True)
        st.divider()
        st.subheader(f"{idx.getSubIdx()}디렉토리 삭제")
        st.write('''디렉토리를 삭제하려면 :blue-background[os.rmdir()] 함수를 사용합니다. 디렉토리가 비어 있어야만 삭제할 수 있습니다.''')
        st.code('''
import os

directory = 'example_dir'

if os.path.exists(directory):
    os.rmdir(directory)
    print(f"{directory} has been deleted.")
else:
    print(f"{directory} does not exist.")''', line_numbers=True)
        st.divider()
        st.subheader(f"{idx.getSubIdx()}디렉토리 내용 나열")
        st.write('''디렉토리의 내용을 나열하려면 :blue-background[os.listdir()] 함수를 사용합니다.''')
        st.code('''
import os

directory = '.'

contents = os.listdir(directory)
print(f"Contents of {directory}:")
for item in contents:
    print(item)''', line_numbers=True)
        st.divider()
        st.subheader(f"{idx.getSubIdx()}디렉토리 내 파일 검색")
        st.write('''디렉토리 내에서 특정 패턴을 가진 파일을 검색하려면 glob 모듈을 사용할 수 있습니다.''')
        st.code('''
import os
import glob

directory = '.'
pattern = '*.txt'

files = glob.glob(os.path.join(directory, pattern))
print(f"Text files in {directory}:")
for file in files:
    print(file)
''', line_numbers=True)
        st.divider()
        st.header(f"{idx.getHeadIdx()}경로 작업")
        st.divider()
        st.subheader(f"{idx.getSubIdx()}경로 결합")
        st.write('''경로를 결합하려면 :blue-background[os.path.join()] 함수를 사용합니다.''')
        st.code('''
directory = 'example_dir'
filename = 'example.txt'

file_path = os.path.join(directory, filename)
print(f"Full file path: {file_path}")''', line_numbers=True)
        st.divider()
        st.subheader(f"{idx.getSubIdx()}절대 경로 얻기")
        st.write('''절대 경로를 얻으려면 :blue-background[os.abspath()] 함수를 사용합니다.''')

        st.code('''
relative_path = 'example.txt'
absolute_path = os.path.abspath(relative_path)
print(f"Absolute path: {absolute_path}")''', line_numbers=True)
        st.divider()
        st.subheader(f"{idx.getSubIdx()}경로 분리")
        st.write('''경로를 디렉토리와 파일명으로 분리하려면 :blue-background[os.path.split()] 함수를 사용합니다.''')
        st.code('''
file_path = '/path/to/example.txt'
directory, filename = os.path.split(file_path)
print(f"Directory: {directory}")
print(f"Filename: {filename}")''', line_numbers=True)
        st.divider()
        st.subheader(f"{idx.getSubIdx()}예제: 파일과 디렉토리 관리 스크립트")
        st.write('''이번 예제에서는 파일과 디렉토리를 관리하는 간단한 스크립트를 구현합니다. 이 스크립트는 파일을 생성하고, 내용을 쓰고, 디렉토리를 생성하고, 파일을 이동합니다.''')
        st.code('''
import os
import shutil

def create_file(file_path, content):
    with open(file_path, 'w') as file:
        file.write(content)
    print(f"File {file_path} created.")

def create_directory(directory_path):
    if not os.path.exists(directory_path):
        os.makedirs(directory_path)
        print(f"Directory {directory_path} created.")
    else:
        print(f"Directory {directory_path} already exists.")

def move_file(src, dst):
    if os.path.exists(src):
        shutil.move(src, dst)
        print(f"Moved {src} to {dst}.")
    else:
        print(f"Source file {src} does not exist.")

# 파일 생성
file_path = 'example.txt'
content = 'Hello, world!'
create_file(file_path, content)

# 디렉토리 생성
directory_path = 'example_dir'
create_directory(directory_path)

# 파일 이동
new_file_path = os.path.join(directory_path, 'example.txt')
move_file(file_path, new_file_path)

# 디렉토리 내용 나열
contents = os.listdir(directory_path)
print(f"Contents of {directory_path}:")
for item in contents:
    print(item)''', line_numbers=True)
        
        st.write('''파일과 디렉토리 작업은 파일 시스템을 조작하고 관리하는 데 필수적인 기능입니다. 파이썬의 다양한 내장 모듈과 함수를 사용하면 파일과 디렉토리를 쉽게 처리할 수 있습니다.''')
        st.divider()

        st.header(f"{idx.getHeadIdx()}파일 입출력 확장")
        st.divider()

        st.subheader(f"{idx.getSubIdx()}파일 포인터 조작")
        st.write('''파일 포인터를 이동시키는 방법을 다루며, :blue-background[seek()]와 :blue-background[tell()] 함수를 소개합니다.''')
        st.code('''
with open('example.txt', 'r') as file:
    file.seek(10)  # 파일 포인터를 10번째 위치로 이동
    content = file.read()
    print(content)
    position = file.tell()  # 현재 파일 포인터 위치 반환
    print(f"Current file pointer position: {position}")''', line_numbers=True)
        st.divider()
        st.subheader(f"{idx.getSubIdx()}대용량 파일 처리")
        st.write('''대용량 파일을 효율적으로 처리하는 방법을 다룹니다. 한 번에 모든 내용을 읽지 않고, 한 줄씩 읽는 방법을 소개합니다.''')
        st.code('''
with open('large_file.txt', 'r') as file:
    for line in file:
        process(line)  # 한 줄씩 읽어 처리''', line_numbers=True)
        st.divider()

        st.subheader(f"{idx.getSubIdx()}임시 파일 및 디렉토리 작업")
        st.write('''tempfile 모듈을 사용하여 임시 파일과 디렉토리를 생성하고 사용하는 방법을 설명합니다.''')
        st.code('''
import tempfile

# 임시 파일 생성
with tempfile.NamedTemporaryFile(delete=False) as temp_file:
    temp_file.write(b'This is a temporary file.')
    print(f"Temporary file created at {temp_file.name}")

# 임시 디렉토리 생성
with tempfile.TemporaryDirectory() as temp_dir:
    print(f"Temporary directory created at {temp_dir}")''', line_numbers=True)
        st.divider()

        st.subheader(f"{idx.getSubIdx()}압축 파일 처리")
        st.write('''zipfile과 tarfile 모듈을 사용하여 압축 파일을 생성하고 해제하는 방법을 다룹니다.''')
        st.code('''
import zipfile

# ZIP 파일 생성
with zipfile.ZipFile('example.zip', 'w') as zipf:
    zipf.write('example.txt')
    zipf.write('another_example.txt')

# ZIP 파일 읽기
with zipfile.ZipFile('example.zip', 'r') as zipf:
    zipf.extractall('extracted_files')''', line_numbers=True)
        st.divider()
        st.subheader(f"{idx.getSubIdx()}파일 모드와 권한")
        st.write('''파일을 열 때 사용하는 다양한 모드(r, w, a, b, x, +)와 파일 권한을 설정하는 방법을 설명합니다.''')
        data = {
    '모드': ['r', 'w', 'a', 'b', 'x', '+'],
    '설명': [
        '읽기 전용 모드로 파일을 엽니다. 파일이 존재하지 않으면 오류가 발생합니다.',
        '쓰기 전용 모드로 파일을 엽니다. 파일이 존재하면 내용을 덮어쓰고, 파일이 존재하지 않으면 새로 만듭니다.',
        '추가 모드로 파일을 엽니다. 파일이 존재하지 않으면 새로 만듭니다. 파일 끝에 내용을 추가합니다.',
        '이진 모드로 파일을 엽니다. 다른 모드와 함께 사용됩니다. 예: rb 또는 wb',
        '배타적 생성 모드로 파일을 엽니다. 파일이 존재하지 않으면 새로 만들고, 파일이 이미 존재하면 오류가 발생합니다.',
        '읽기와 쓰기 모드를 모두 허용합니다. 다른 모드와 함께 사용됩니다. 예: r+, w+, a+'
    ]
}       
        import pandas as pd
        data_df = pd.DataFrame(data)
        st.table(data_df)

        st.code('''
# 파일을 읽기 및 쓰기 모드로 열기
with open('example.txt', 'r+') as file:
    content = file.read()
    file.write('Additional content')

# 파일 권한 설정
import os
os.chmod('example.txt', 0o644)  # 읽기/쓰기 권한 설정
''', line_numbers=True)
        st.write('''파일 입출력 챕터에서는 파일과 디렉토리 작업 외에도 파일 포인터 조작, 대용량 파일 처리, 임시 파일 및 디렉토리 작업, 압축 파일 처리, 파일 모드와 권한 등의 주제를 추가로 다룰 수 있습니다. 이러한 주제들은 파일 시스템을 보다 효율적이고 유연하게 관리하는 데 도움이 되며, 다양한 상황에서 파일 입출력 작업을 더욱 강화할 수 있습니다.''')

