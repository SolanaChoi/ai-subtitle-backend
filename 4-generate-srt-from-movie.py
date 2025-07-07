from datetime import timedelta
from moviepy import VideoFileClip
from config import VIDEO_FILE, AUDIO_FILE



def format_time(timecut):
    td = timedelta(seconds=timecut)
    hrs = int(td.total_seconds()//3600)
    min = int((td.total_seconds() % 3600) // 60)
    sec = int(td.total_seconds() % 60)
    milsec = int((td.total_seconds() % 1) * 1000)

    return f'{hrs:02d}:{min:02d}:{sec:02d},{milsec:03d}'


def extract_audio_moviepy(videopath, audiopath):
    video = VideoFileClip(videopath)
    output = video.audio.write_audiofile(audiopath,fps=16000, nbytes=2, codec='pcm_s16le')
    video.close()
    return output



def srt_from_segments(videopath, audiopath):
    audio = extract_audio_moviepy(videopath, audiopath)
    pass
    #1. 영상 > 오디오
    #2. 오디오 > 세그먼트
    #3. 세그먼트 > srt저장





# result ='' 
# for segment in segments:
#     start_time = format_time(segment['start'])
#     end_time = format_time(segment['end'])
#     text = segment['text']

#     result += f'{start_time}--> {end_time}\n{text}\n\n'

# return result