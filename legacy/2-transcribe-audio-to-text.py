# auido -> text 변환
import whisper
import os
import json
from config import VIDEO_FILE, AUDIO_FILE, SUBTITLE_JSON_FILE, SUBTITLE_TEXT_FILE


#위스퍼 모델 불러오기=============================
print('model 불러오깅ㅋㅋ')
model = whisper.load_model('small') #tiny, base, medium, large

#audio to text
print('2.1 오디오 to 텍스트로 변환 전 BEFORE---')
result= model.transcribe(AUDIO_FILE)

print('2.2 오디오 to 텍스트 변환 후 AFTER---')

#변환된 텍스트 출력=============================
print('3 텍스트 변환 완료 ---')

# #텍스트를 파일로 저장===========================
# output_dir = 'source\subtitle'
# output_path = os.path.join(output_dir, 'test.txt')
# output_path_json = os.path.join(output_dir, 'test.json')

# with open('경로', '쓰기읽기모드', '엔코딩')
lines = result['text'].split('. ') 
with open(SUBTITLE_TEXT_FILE, 'w', encoding='utf-8') as f:
    for line in lines:
        f.write(line.strip()+'\n') 

# #텍스트의 segments를 test.json 으로 저장===========================
with open(SUBTITLE_JSON_FILE, 'w', encoding='utf-8') as f:
    json.dump(result['segments'], f, indent=2, ensure_ascii=False)


# #디렉토리 만들기================================
'''output_path = output_dir + '/test.txt' === output_path = os.path.join(output_dir, 'test.txt') 
근데 os 쓰는게 더 안정적 

output_dir = './source/subtitle'
os.makedirs(output_dir, exist_ok=True)'''



