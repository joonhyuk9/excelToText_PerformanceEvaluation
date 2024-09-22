import pandas as pd
import pyperclip

# 엑셀 파일 경로 설정
example_file_path = '수행_서식.xlsx'

# 엑셀 파일 읽기 (첫 번째 시트 기준)
df = pd.read_excel(example_file_path)

# 텍스트 형식 변환 함수
def convert_to_text(df):
    text_output = "《9월 3주 수행평가 정리》\n"
    
    # 요일 이름과 날짜 추출
    days = df.iloc[0, :]  # 첫 번째 행은 요일과 날짜 정보
    tasks_df = df.iloc[1:, :]  # 나머지 행들은 할 일 정보
    
    for i, day in enumerate(days):
        day_tasks = tasks_df.iloc[:, i].dropna().tolist()
        text_output += f"-{day}\n"
        
        if day_tasks:
            for task_num, task in enumerate(day_tasks, 1):
                text_output += f"{task}\n"
        else:
            text_output += "None\n"
    
    return text_output

# 변환된 텍스트를 클립보드에 복사 & 프린트
output_text = convert_to_text(df)
pyperclip.copy(output_text)
print(output_text)

print("복사 완료")
