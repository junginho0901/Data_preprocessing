import os

def count_files_in_folder(folder_path):
    try:
        # 폴더 내의 파일 목록을 얻음
        files = os.listdir(folder_path)
        
        # 폴더 내 파일 개수 출력
        print(f"Number of files in {folder_path}: {len(files)}")
        
        return len(files)
    except FileNotFoundError:
        print(f"The folder {folder_path} does not exist.")
        return 0

# 폴더 경로 설정 (필요에 따라 수정)
folder_path = '/content/drive/MyDrive/inho/데이터/합성 파일,잡음+아이(npy)2'

# 함수 호출
file_count = count_files_in_folder(folder_path)
