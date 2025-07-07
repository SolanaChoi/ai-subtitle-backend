import os
from datetime import timedelta

'''
- 초 단위 시간을 SRT 형식(hh:mm:ss:mmm)으로 변환
- datetime.timedelta()
    : float 초 반환
    : 내부적으로 days, seconds, microseconds 등을 관리 
    : ex) 3662.567초 -> 0 days, 1hour, 1minute, 2seconds + 567milliseconds
- 312.92
'''

timecut = 141.923

td = timedelta(seconds=timecut)
print(td)

 
# 전체 초를 3600(1시간)으로 나눠 시간만 추출
# //는 나눗셈 후 소수점 버림요
 
hours = int(td.total_seconds() // 3600)
print(hours)

# 전체 초에서 시간 부분을 뺀 나머지에서 그 나머지를 60으로 나눈 몫 = 분 
min = int((td.total_seconds() % 3600) // 60)
print('minutes는~~', min)

# 전체 초에서 시간 부분을 뺀 나머지 = '초'만 추출
seconds = int(td.total_seconds() % 60)
print('seconds는.....!', seconds)


# 소수점 아래(1초미만) 부분 추출: 밀리초로 변환 
# 3662.567 % 1 = 0.567 -> 0.567 * 1000 = 567
# milliseconds

milliseconds = int((td.total_seconds() % 1) * 1000)
print('milliseconds는.....!', milliseconds)

result = f'{hours:02d}:{min:02d}:{seconds:02d}:{milliseconds:03d}'

'''print('subtitle 폴더 생성 시작')

os.makedirs('./subtitle', exist_ok=True)       #얘는 이미 만들었으면 똑같은 실행 안됨, 근데 그 에러 막으려면 exist_ok파라미터 트루로 설정해주셈 
print('subtitle 폴더 생성 완료')'''

