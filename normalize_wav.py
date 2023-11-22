import os
import librosa
import librosa.display
import numpy as np
import soundfile as sf

def normalize_wav(input_path, output_path):
    # WAV 파일 로드
    y, sr = librosa.load(input_path)

    # 정규화
    normalized_y = librosa.util.normalize(y)

    # 정규화된 데이터를 WAV 파일로 저장
    sf.write(output_path, normalized_y, sr)

if __name__ == "__main__":
    # 입력 WAV 파일 경로
    input_wav_path = "your_input_wav_path.wav"

    # 출력 WAV 파일 경로 (정규화된 데이터를 저장할 파일)
    output_wav_path = "your_output_wav_path_normalized.wav"

    # WAV 파일 정규화
    normalize_wav(input_wav_path, output_wav_path)

    print(f"정규화가 완료되었습니다. 정규화된 WAV 파일은 {output_wav_path}에 저장되었습니다.")
