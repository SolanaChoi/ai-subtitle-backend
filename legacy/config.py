import os

# 기본 디렉토리 

# 무좍건 절대경로로 변환해주는 함수 abspath
BASE_DIR = os.path.abspath(os.path.dirname(__file__))

# c:/Course_Video/16_ai/ai-model-development/backend/config.py
# print(__file__)  #파일 경로+파일명

# c:\Course_Video\16_ai\ai-model-development\backend
# print(os.path.dirname(__file__))  #파일 경로만

#폴더 경로
VIDEO_DIR = os.path.join(BASE_DIR, 'source', 'video')
AUDIO_DIR = os.path.join(BASE_DIR, 'source', 'audio')
SUBTITLE_DIR = os.path.join(BASE_DIR, 'source', 'subtitle')

#파일명
filename = 'test'
VIDEO_FILE = os.path.join(VIDEO_DIR, f'{filename}.mp4')
AUDIO_FILE = os.path.join(AUDIO_DIR, f'{filename}.wav')
SUBTITLE_TEXT_FILE = os.path.join(SUBTITLE_DIR, f'{filename}.txt')
SUBTITLE_JSON_FILE = os.path.join(SUBTITLE_DIR, f'{filename}.json')

# print(SUBTITLE_JSON_FILE)
# print(SUBTITLE_DIR)