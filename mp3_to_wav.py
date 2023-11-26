import os
import ffmpeg
from pydub import AudioSegment

# 현재 노트북 파일이 위치한 경로를 얻습니다.
notebook_folder = os.path.abspath('.')

# 변환할 MP3 파일이 있는 폴더 경로 (상대 경로)
mp3_folder = 'Downloads/174.자연 및 인공적 발생 非언어적 소리 데이터/01.데이터/1.Training/원천데이터/1.기상/1.비'

# 변환된 WAV 파일을 저장할 폴더 경로 (상대 경로)
wav_folder = 'Downloads/174.자연 및 인공적 발생 非언어적 소리 데이터/01.데이터/1.Training/원천데이터/1.기상/mp3비'

# 절대 경로로 변환
mp3_folder = os.path.join(notebook_folder, mp3_folder)
wav_folder = os.path.join(notebook_folder, wav_folder)

# MP3 파일을 WAV 파일로 변환하는 함수
def convert_mp3_to_wav(mp3_file, wav_file):
    sound = AudioSegment.from_mp3(mp3_file)
    sound.export(wav_file, format="wav")

# MP3 파일이 있는 폴더를 탐색하고 변환
for filename in os.listdir(mp3_folder):
    if filename.endswith(".mp3"):
        mp3_file = os.path.join(mp3_folder, filename)
        wav_file = os.path.join(wav_folder, filename.replace(".mp3", ".wav"))
        convert_mp3_to_wav(mp3_file, wav_file)

print("MP3 파일을 WAV 파일로 변환 완료!")
