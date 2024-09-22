import pandas as pd


# 엑셀 파일 경로 설정
example_file_path = '수행_예시.xlsx'

# 엑셀 파일 읽기 (첫 번째 시트 기준)
df = pd.read_excel(example_file_path)

# 텍스트 형식 변환 함수
def convert_to_text(df):
    text_output = "《9월 3주 수행평가 정리》\n"
    
    # 요일 이름과 날짜 추출
    days = df.iloc[0, :]  # 첫 번째 행은 요일과 날짜 정보
    tasks_df = df.iloc[1:, :]  # 나머지 행들은 할 일 정보
    
    for i, day in enumerate(days):
        day_tasks = tasks_df.iloc[:, i].dropna().tolist()  # 해당 열에서 결측치(NaN) 제외하고 리스트로 변환
        text_output += f"-{day}\n"
        
        if day_tasks:
            for task_num, task in enumerate(day_tasks, 1):
                text_output += f"{task}\n"
        else:
            text_output += "None\n"
    
    text_output += "\n⬇️더 자세히 보기(Notion)\nhwasu206.kro.kr"
    return text_output

# 변환된 텍스트 출력
output_text = convert_to_text(df)
print(output_text)
