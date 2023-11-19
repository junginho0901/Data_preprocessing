import os
import librosa
import numpy as np

def extract_mfcc(file_path):
    y, sr = librosa.load(file_path)
    mfccs = librosa.feature.mfcc(y=y, sr=sr)
    return mfccs

def compare_mfccs(mfccs_list):
    avg_mfcc = np.mean(mfccs_list, axis=0)

    print("Average MFCCs:")
    print(avg_mfcc)

    for i, mfccs in enumerate(mfccs_list):
        diff = np.mean(np.abs(avg_mfcc - mfccs))
        print(f"File {i + 1}: {diff}")

if __name__ == "__main__":
    # 오디오 파일이 들어있는 폴더 경로를 지정합니다.
    folder_path = "your_folder_path"

    # 폴더 안의 모든 오디오 파일 경로를 가져옵니다.
    audio_files = [os.path.join(folder_path, file) for file in os.listdir(folder_path) if file.endswith(".wav")]

    # 각 파일의 MFCC를 추출하여 리스트에 저장합니다.
    mfccs_list = [extract_mfcc(file_path) for file_path in audio_files]

    # 추출된 MFCC를 비교합니다.
    compare_mfccs(mfccs_list)
