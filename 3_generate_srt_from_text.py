import json
import os
from config import SUBTITLE_JSON_FILE, SUBTITLE_DIR
from datetime import timedelta


def format_time(timecut):
    #초 단위 시간을 srt 형식으로 변환
    td = timedelta(seconds=timecut)
    hrs = int(td.total_seconds()//3600)
    min = int((td.total_seconds() % 3600) // 60)
    sec = int(td.total_seconds() % 60)
    milsec = int((td.total_seconds() % 1) * 1000)

    return f'{hrs:02d}:{min:02d}:{sec:02d},{milsec:03d}'

# segments(test.json) 불러오깅
with open(SUBTITLE_JSON_FILE, 'r', encoding='UTF-8') as f:
    segments = json.load(f)

# print(segments)
# print(format_time(segments[0]['start']))
# print(format_time(segments[0]['end']))
# print(segments[0]['text'])

def srt_from_segments():
    result ='' 
    for segment in segments:
        start_time = format_time(segment['start'])
        end_time = format_time(segment['end'])
        text = segment['text']

        result += f'{start_time}--> {end_time}\n{text}\n\n'

    return result


with open ( f'{SUBTITLE_DIR}/newtext.txt', 'w', encoding='utf-8') as f:
    f.write(srt_from_segments())