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

- swagger

        호스트주소:port/docs

- 다른 docs

         호스트주소:port/redocs

-- 


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




## 참고
- [fast api 공식](https://fastapi.tiangolo.com/ko/#_6)
- [fast api 참고](https://velog.io/@crosstar1228/BackendFastAPI-%EC%9E%85%EB%AC%B8-1-Uvicorn-%EC%9D%B4%ED%95%B4%ED%95%98%EA%B8%B0-%EA%B0%84%EB%8B%A8%ED%95%9C-%EC%9B%B9-%EC%84%9C%EB%B2%84-%EA%B5%AC%ED%98%84) 
- [typing 내장 모듈](https://www.daleseo.com/python-typing/)

- [Pydanic 모델](https://docs.pydantic.dev/latest/)