import os
from datetime import datetime, timedelta
from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
import whisper

# FastAPI 인스턴스 생성 (단 1회)
app = FastAPI()

# CORS 설정
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # 실제 배포 시엔 도메인 제한 필수!
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 폴더 생성
UPLOAD_DIR = './uploads'
OUTPUT_DIR = './output'
os.makedirs(UPLOAD_DIR, exist_ok=True)
os.makedirs(OUTPUT_DIR, exist_ok=True)

# Whisper 모델 로딩
model = whisper.load_model('small')

# 인덱스 라우터
@app.get('/')
def index():
    return '환영합니다.'

# 자막 생성 라우터
@app.post('/create_subtitled_video')
async def create_subtitled_video(file: UploadFile = File(...)):
    print('\n=== 비디오 처리 시작 ===')

    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    temp_video_path = os.path.join(UPLOAD_DIR, f'temp_video_{timestamp}.mp4')

    contents = await file.read()
    with open(temp_video_path, 'wb') as f:
        f.write(contents)

    print('Whisper로 텍스트 추출 시작')
    result = model.transcribe(temp_video_path)
    segments = result['segments']

    srt_filename = f'subtitle_{timestamp}.srt'
    srt_path = os.path.join(OUTPUT_DIR, srt_filename)

    with open(srt_path, 'w', encoding='utf-8') as f:
        for i, seg in enumerate(segments, 1):
            start = format_time(seg['start'])
            end = format_time(seg['end'])
            text = seg['text'].strip()

            f.write(f'{i}\n{start} --> {end}\n{text}\n\n')

    # 명확하게 JSON 응답으로 반환
    return JSONResponse(content={"segments": segments}, headers={"Access-Control-Allow-Origin": "*"})

# 시간 포맷 변환 함수
def format_time(seconds):
    td = timedelta(seconds=seconds)
    hours = int(td.total_seconds() // 3600)
    minutes = int((td.total_seconds() % 3600) // 60)
    seconds = int(td.total_seconds() % 60)
    milliseconds = int((td.total_seconds() % 1) * 1000)
    return f'{hours:02d}:{minutes:02d}:{seconds:02d},{milliseconds:03d}'
