# FastAPI

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



## 참고
- [fast api 공식](https://fastapi.tiangolo.com/ko/#_6)
- [fast api 참고](https://velog.io/@crosstar1228/BackendFastAPI-%EC%9E%85%EB%AC%B8-1-Uvicorn-%EC%9D%B4%ED%95%B4%ED%95%98%EA%B8%B0-%EA%B0%84%EB%8B%A8%ED%95%9C-%EC%9B%B9-%EC%84%9C%EB%B2%84-%EA%B5%AC%ED%98%84) 
- [typing 내장 모듈](https://www.daleseo.com/python-typing/)