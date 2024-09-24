import pandas as pd
import pyperclip
import tkinter as tk
from tkinter import messagebox

# 엑셀 파일 경로 설정
example_file_path = '수행_예시.xlsx'

# 엑셀 파일 읽기 (첫 번째 시트 기준)
df = pd.read_excel(example_file_path)

# F1 셀의 값을 가져옴 (제목에 사용할 값)
header_value = df.columns[0]  # F1 셀의 값은 첫 번째 컬럼의 헤더로 저장됨

# 텍스트 형식 변환 함수 (한주 버튼용)
def convert_to_text_week(df, header_value):
    text_output = f"《{header_value} 수행평가 정리》\n"
    days = df.iloc[0, :]
    tasks_df = df.iloc[1:, :]
    
    for i, day in enumerate(days):
        day_tasks = tasks_df.iloc[:, i].dropna().tolist()
        text_output += f"-{day}\n"
        
        if day_tasks:
            for task in day_tasks:
                text_output += f"{task}\n"
        else:
            text_output += "None\n"
    
    text_output += "\n⬇️더 자세히 보기(Notion)\nhwasu206.kro.kr"
    return text_output

# 특정 요일의 텍스트 변환 함수
def convert_to_text_day(df, day_index, day_name):
    date_info = df.iloc[0, day_index]  # 날짜 정보 가져오기
    tasks = df.iloc[1:, day_index].dropna().tolist()  # 요일별 할 일
    
    # {월}.{날짜} 정보 추출
    date = date_info.split("(")[1].strip(")")  # 괄호 안의 날짜만 추출
    
    # 텍스트 형식화
    text_output = f"《{date} ({day_name})》\n-수행\n"
    if tasks:
        for task in tasks:
            text_output += f"{task}\n"
    else:
        text_output += "None\n"
    
    text_output += "\n⬇️ 자세히 보기(Notion)\nhwasu206.kro.kr"
    return text_output

# 클립보드에 텍스트 복사 및 화면에 표시
def copy_to_clipboard(text, label):
    pyperclip.copy(text)
    label.config(text=text)
    messagebox.showinfo("클립보드", "클립보드로 복사되었습니다!")

# GUI 설정
def create_gui():
    window = tk.Tk()
    window.title("수행평가 관리")
    window.geometry("900x500")

    # 버튼 아래에 텍스트를 표시할 Label 생성
    result_label = tk.Label(window, text="", wraplength=500, justify="left", padx=10, pady=10)
    result_label.pack(pady=20)

    # 버튼을 클릭했을 때 실행할 함수
    def on_button_click(button_type):
        if button_type == '한주':
            text = convert_to_text_week(df, header_value)
        else:
            day_mapping = {'월': 0, '화': 1, '수': 2, '목': 3, '금': 4}
            day_index = day_mapping[button_type]
            text = convert_to_text_day(df, day_index, button_type)
        
        copy_to_clipboard(text, result_label)

    # 버튼 생성 ('한주', '월', '화', '수', '목', '금')
    button_names = ['한주', '월', '화', '수', '목', '금']
    for name in button_names:
        button = tk.Button(window, text=name, width=10, command=lambda n=name: on_button_click(n))
        button.pack(side=tk.LEFT, padx=5)

    # 메인 루프 실행
    window.mainloop()

# GUI 실행
create_gui()
