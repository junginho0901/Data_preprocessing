import os
import random
import shutil

# 데이터셋이 있는 폴더 경로
original_dataset_path = '/content/drive/MyDrive/inho/데이터/합성 파일,잡음+아이(npy)'

# 새로운 폴더 생성 (저장할 위치)
new_dataset_path = '/content/drive/MyDrive/inho/데이터/합성 파일,잡음+아이(npy)2'
os.makedirs(new_dataset_path, exist_ok=True)

# 데이터셋에서 무작위로 100개 파일 선택
random.seed(42)  # 재현성을 위한 시드 설정
selected_files = random.sample(os.listdir(original_dataset_path), 6000)

# 선택된 파일을 새로운 폴더로 이동
for file_name in selected_files:
    file_path = os.path.join(original_dataset_path, file_name)
    destination_path = os.path.join(new_dataset_path, file_name)
    shutil.move(file_path, destination_path)

print(f"Moved {len(selected_files)} files to {new_dataset_path}.")
