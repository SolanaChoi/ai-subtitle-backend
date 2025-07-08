import logging

#log는 level을 갖는다.
'''[level]
    레벨            설명                            출력조건
    --------------------------------------------------------------
    Debug           상세한 내부상태 출력(개발단계)  level=logging.DEBUG일때만
    INFO            일반적인 정보 메시지            Info 이상 설정시 출력
    Warning         경고 사항                       warning 이상
    Error           에러 사항                       error 이상
    Critical        치명적 오류                     ALWAYS,,,,,

    [로그레벨 순서] 낮음 -> 높음 우측으로 갈수록 치명적
    Debug < info < warning < error < critical

'''

#1. 로깅 기본설정
# logging.basicConfig(level=logging.DEBUG)
# logging.basicConfig(level=logging.INFO)
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s  [%(levelname)s]  %(message)s'     #%s는 문자열 ,, log출력될당시 시간 보여주는 것 
)

#2. 로거 객체 생성
logger = logging.getLogger(__name__)

userName = '차은우'

#3. 로그 출력
logger.debug('디버깅용 메시지')
logger.info(f'{userName}, 정보 메시지')
logger.warning('경고 메시지: %s, %s', userName, '김태형') #userName은 첫번째 %s에 딸리게되고 김태형은 두번째 %s에 딸리게 됨 
logger.error('에러메시지')
logger.critical('크리티컬 메시지')

print('크리티컬 메시지')
