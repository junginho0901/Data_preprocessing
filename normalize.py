import os
import librosa
import numpy as np

def normalize_frequency(frequencies):
    min_freq = np.min(frequencies)
    max_freq = np.max(frequencies)

    normalized_freq = (frequencies - min_freq) / (max_freq - min_freq)
    return normalized_freq

def normalize_decibels(decibels):
    mean_db = np.mean(decibels)
    std_db = np.std(decibels)

    normalized_db = (decibels - mean_db) / std_db
    return normalized_db

def get_audio_features(file_path):
    y, sr = librosa.load(file_path)
    frequencies = np.abs(librosa.fft_frequencies(sr=sr))
    decibels = librosa.amplitude_to_db(np.abs(librosa.stft(y)), ref=np.max)
    return frequencies, decibels

def save_normalized_features(file_name, normalized_frequencies, normalized_decibels, output_folder):
    output_file_path = os.path.join(output_folder, f"normalized_{file_name}.txt")
    
    with open(output_file_path, "w") as f:
        f.write("Normalized Frequencies:\n")
        np.savetxt(f, normalized_frequencies, fmt="%f")

        f.write("\nNormalized Decibels:\n")
        np.savetxt(f, normalized_decibels, fmt="%f")

if __name__ == "__main__":
    # 입력 폴더: 오디오 파일이 저장된 폴더 경로
    input_folder = "input_folder"

    # 출력 폴더: 정규화된 결과를 저장할 폴더 경로
    output_folder = "output_folder"

    # 출력 폴더가 없다면 생성
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for file_name in os.listdir(input_folder):
        if file_name.endswith(".wav"):
            file_path = os.path.join(input_folder, file_name)
            frequencies, decibels = get_audio_features(file_path)

            # 주파수 정규화
            normalized_frequencies = normalize_frequency(frequencies)

            # 데시벨 정규화
            normalized_decibels = normalize_decibels(decibels)

            # 정규화된 결과를 저장
            save_normalized_features(file_name, normalized_frequencies, normalized_decibels, output_folder)

            print(f"File: {file_name} - Normalized features saved.")
