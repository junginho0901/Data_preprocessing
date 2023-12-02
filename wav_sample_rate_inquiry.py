import os
import librosa

# 음성 파일이 들어 있는 폴더 경로
folder_path = '/path/to/your/audio/files'

# 폴더 내의 모든 WAV 파일에 대해 처리
for filename in os.listdir(folder_path):
    if filename.endswith('.wav'):
        file_path = os.path.join(folder_path, filename)

        # librosa를 사용하여 샘플레이트 확인
        try:
            audio_data, sr = librosa.load(file_path, sr=None)
            print(f'File: {filename}, Sample Rate: {sr}')
        except Exception as e:
            print(f'Error processing {filename}: {e}')

