## MoviePy: 동영상편집을 위한 라이브러리 
from moviepy import VideoFileClip
from config import VIDEO_FILE, AUDIO_FILE

# input_video_path = './source/video/test.mp4' 
# output_audio_path = './source/audio/test.wav'

print('1. [영상에서 오디오 추출] 시작')

def extract_audio_moviepy(videopath, audiopath):
    video = VideoFileClip(videopath)
    output = video.audio.write_audiofile(audiopath,fps=16000, nbytes=2, codec='pcm_s16le')
    video.close()
    return output

extract_audio_moviepy(VIDEO_FILE, AUDIO_FILE)


#비디오에서 오디오 추출
# video.audio.write_audiofile(output_audio_path, fps=16000, nbytes=2, codec='pcm_s16le')

#리소스 해제 - 오됴추출은 스트림을 사용하므로 해제가 필요..(?)
# video.close()

print('2. [영상에서 오디오 추출] 완료')
