from fastapi import FastAPI, UploadFile, File
from datetime import datetime, timedelta
import whisper
import os

# 디렉토리 생성
# 동영상 저장되는 폴더: uploads
# srt 파일 저장 폴더: output
UPLOAD_DIR = './uploads'
OUTPUT_DIR = './output'

os.makedirs(UPLOAD_DIR, exist_ok=True)
os.makedirs(OUTPUT_DIR, exist_ok=True)

# whisper 모델 로드
model = whisper.load_model('small')

# Fast API 실행
app = FastAPI()

@app.get('/')
def index():
    return '환영함다 '

# 요청 url: /create_subtitled_video 
# 요청메서드: get  
# 리턴:요청처리됨
@app.post('/create_subtitled_video')
async def create_subtitled_video(file: UploadFile = File(...)):  # file의 타입은 UpFi인데 File어쩌구로 필수 입력해야한다. 란뜻
    print('\n=====비디오 처리 시작=====')

    #video 파일명 지정
    #temp_video_250707_1720.mp4
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    temp_video_path = os.path.join(UPLOAD_DIR, f'temp_video_{timestamp}.mp4')

    #업로드한 영상 저장 
    contents = await file.read()
    #with문 사용해 쓰기 작업 : 모드= wb, 저장경로= temp_v_p
    with open (temp_video_path, 'wb') as f:
        f.write(contents)

    print('whisper로 자막 추출 시작')
    result = model.transcribe(temp_video_path)

    segments = result['segments']

    #srt 파일 : 파읾 지정
    srt_filename = f'subtitle_{timestamp}.srt'
    srt_path = os.path.join(OUTPUT_DIR, srt_filename)

    #srt 파일 생성
    with open(srt_path, 'w', encoding='utf-8') as file:
        for i, seg in enumerate(segments, 1):
            start = format_time(seg['start'])
            end = format_time(seg['end'])
            text = seg['text'].strip()

            file.write(f'{i}\n')
            file.write(f'{start} --> {end}\n')
            file.write(f'{text}\n\n')

    return '요청 처리됨 ㅋ'

def format_time(timecut):
    td = timedelta(seconds=timecut)
    hrs = int(td.total_seconds()//3600)
    min = int((td.total_seconds() % 3600) // 60)
    sec = int(td.total_seconds() % 60)
    milsec = int((td.total_seconds() % 1) * 1000)

    return f'{hrs:02d}:{min:02d}:{sec:02d},{milsec:03d}'