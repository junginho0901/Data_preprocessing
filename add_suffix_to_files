import os

folder_path = '폴더의_경로'  # 여기에 폴더의 실제 경로를 입력하세요.

# 폴더 내의 모든 파일 목록을 가져옵니다.
file_list = os.listdir(folder_path)

# 파일 이름에 "_1"을 붙이고 새로운 이름으로 저장합니다.
for file_name in file_list:
    new_file_name = file_name.replace(".", "_1.")  # 파일 확장자 앞에 "_1"을 추가합니다.
    old_file_path = os.path.join(folder_path, file_name)
    new_file_path = os.path.join(folder_path, new_file_name)
    os.rename(old_file_path, new_file_path)

print("모든 파일 이름에 '_1'을 추가하였습니다.")
