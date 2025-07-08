from  fastapi import FastAPI

#1. FastAPI 앱 객체 생성
app = FastAPI()

#2. get 요청 : index page
@app.get('/')  #API
def index() :
    return 'welcome! 😙'  #API+함수 = 라우트(handler핸들러)

#3. get요청
@app.get('/info')
def info():
    return {'message':'hellow😎'}

#4. get요청: URL 경로에 매개변수 사용 (계층구조)
@app.get('/products/{id}')   # 패스에(url경로에) 설정한 파라미터
def info_production(id:int):
    return f'상품번호:{id}'

#5. get요청: URL 경로에 매개변수 사용 
@app.get('/hello/{name}')
def greet_user_name(name:str):
    return {'name':f'Hello, {name}!'}

#6. post요청 : JSON 데이터 받기 - 무려 class를 사용해야함! ㄷㄷ
from pydantic import BaseModel

# BaseModel: Json 데이터 받을 떄 구조 정의 
class User(BaseModel):   # BaseModel을 상속받은 자식 클래스 생성
    userName: str
    age: int

@app.post('/user')
def create_user(user: User):
    print('user는', user)
    print('키값은', user.userName, user.age)
    return {
        'message': '사용자 정보가 등록되었습니다.',
        'user_info': user
    }

### 상품정보 저장
items = {}

# 상품 등록 (서버에 변경 일어남 데이터 수정or생성)======================
# 상품 정보: 상품번호(itemID) = 키, 상품명(itemName), 가격(price)
# Route: API
# 요청 URL: /item
# 요청방식: post

class Item(BaseModel):
    itemID: int
    itemName: str
    price: int

@app.post('/item')
def create_item(item: Item):
    print('상품 등록 전 items 는', items)
    items[item.itemID] = item.model_dump()     #DB에서 형태 그대로 뜰 때 주로 dump!
    print('상품 등록 후우 items 는', items)
    return '[post]/ item처리됨'

# 전체 데이터 조회 (서버에 변경x just read)==========================
# 저장된 모든 상품의 정보를 리턴: type list
# 요청 URL: /items
# 요청 method: get
@app.get('/items')
def read_items():
    return list(items.values())