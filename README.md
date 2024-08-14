# 시작하기 전 알아야할 것 


## install 

    pip install fastapi 'uvicorn[standard]'


## 서버 실행
```shell
uvicorn main:app --reload

main: main.py 파일 (파이썬 "모듈").

app: the object created inside of main.py with the line app = FastAPI().

--reload: 코드가 변경된 후 서버 재시작하기. 개발환경에서만 사용하십시오.

```

## docs

### swagger

    호스트주소:port/docs

### 다른 docs

    호스트주소:port/redocs


<br><br>

# FastAPI 기능과 특징

## 1. 고정경로는 항상 위에 

```python
@app.get("/users/me") # 고정경로 

@app.get("/items/{item_id}") # 매개변수가 들어간 경로
```

`users/{user_id}`는 `/users/me` 요청 또한 매개변수 user_id의 값이 "me"인 것으로 "생각하게" 됩니다.

<br>

## 2. 데이터 파싱

```python
@app.get("/items/{item_id}")
async def read_item(item_id: int, q: Union[str,None] = None):
    return {"item_id" : item_id, "q" : q}
```

들어온 `item_id`가 `int`로 변환이 불가능하면 에러가 발생한다.

<br>

## 3. 쿼리 파라미터

쿼리는 URL에서 ? 후에 나오고 &으로 구분되는 키-값 쌍의 집합입니다.

```
http://127.0.0.1:8000/items/?skip=0&limit=10
```

함수의 매개변수 형태로 사용하며, `기본값 유무`를 통해 필수 파라미터 또는 기본파라미터로 나누며
`Union`을 사용하여 선택적 파라미터로 사용할 수 도 있다.

```python
@app.get("/items/{item_id}")
async def read_user_item(
    item_id: str, needy: str, skip: int = 0, limit: Union[int, None] = None
):
    
    #needy, 필수적인 str. = 기본 값 없음
    #skip, 기본값이 0인 int. = 기본값 있음
    #limit, 선택적인 int. = 선택적 파라미터, 값이 있으면 int여야하고 없으면 None

    item = {"item_id": item_id, "needy": needy, "skip": skip, "limit": limit}
    return item

```

다양한 검증 예시

```
http://127.0.0.1:8000/items/?item-query=fixedquery&size=1
```

```python
## 쿼리 파라미터 다양한 검증
@app.get("/items/")
async def read_items(
    q: Union[str, None] = Query(
        default=None, # 기본 값 
        alias="item-query", # 유저가 요청할 때 쓰일 별칭 값 
        title="임시 타이틀", # 
        description="Query string for the items to search in the database that have a good match", # 설명
        min_length=3, # 최소 길이
        max_length=50, # 최대 길이
        pattern="^fixedquery$", # 패턴 설정
        # deprecated=True, # swagger에 deprecated 표시
    ),
    size: float = Query(gt=0, lt=10.5)  # gt, ge, lt, le

):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results
```





## 4. Request Body 

Path + Body + Query Parameter 

```python

@app.put("/items/{item_id}")
async def update_item(item_id: int, item: ItemDTO, q: str | None = None):
    print(item_id, item, q)
    result = {"item_id": item_id}
    if q:
        result.update({"q": q})
    return result

```




## 참고
- [fast api 공식](https://fastapi.tiangolo.com/ko/#_6)
- [fast api 참고](https://velog.io/@crosstar1228/BackendFastAPI-%EC%9E%85%EB%AC%B8-1-Uvicorn-%EC%9D%B4%ED%95%B4%ED%95%98%EA%B8%B0-%EA%B0%84%EB%8B%A8%ED%95%9C-%EC%9B%B9-%EC%84%9C%EB%B2%84-%EA%B5%AC%ED%98%84) 
- [typing 내장 모듈](https://www.daleseo.com/python-typing/)

- [Pydanic 모델](https://docs.pydantic.dev/latest/)