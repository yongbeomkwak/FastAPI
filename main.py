from typing import Union
from fastapi import FastAPI , Query
from pydantic import BaseModel
from dto import *


app = FastAPI()

@app.get("/") #클라이언트가 HTTP METHOD중 GET을 통해 localhost: 8000에 접속햇을 때 담당할 함수
async def read_root():
    return {"Hello" : "Wrold" }

@app.get("/sat") #클라이언트가 HTTP METHOD중 GET을 통해 localhost: 8000/sat에 접속했을 때 담당하는 함수
async def read_sat():
    return {"Hello" : "토요일" }

# 고정되있는 경로가 파라미터가 있는 경로보다 항상 위에  있어야한다.

@app.get("/items/me")
async def update_item():
    return {"item_id": "내 유저정보"}

@app.get("/items/{item_id}")
async def update_item(item_id: str):
    return {"item_id": item_id}

tmp = [1,2,4,10,6,7,3,100,1,1,23,3,4,5,6,] # 조회수  -> [1,2,3,4,6,7,10]  , [10,7,6,4,3,2,1]

# 쿼리파라미터는 순서가 크게 상관이 없다. 
@app.get("/videos")
async def read_videos(isDesc: bool, length: int = 3, a: Union[int, None] = None): # 내림차순으로 주냐? 오름 차순으로 주냐 

    # 필수값은 기본값 or Union 사용 x
    # 기본값은 a = 10 꼴로 기본값 할당
    # 선택적인 값은 Union사용
    if isDesc:
        return  {"videos": sorted(tmp, reverse = True)[:length]}
    else:
         return {"videos": sorted(tmp)[:length]}


a_all_mails = [1,2,3,4,5,6,8,48]
b_all_mails = [-1,-1,-4,-2,-3,-4]

@app.get("/mail/{user_id}/all")
async def read_all_mail(user_id: int, isDesc: bool):
    if user_id == 0:
        #a의 메일을 보여줌
        if isDesc:
            return {"mail:" : sorted(a_all_mails, reverse = True)}
        else: 
             return {"mail:" : sorted(a_all_mails)}

    elif user_id ==1:
        if isDesc:
            return {"mail:" : sorted(b_all_mails, reverse = True)}
        else: 
             return {"mail:" : sorted(b_all_mails)}
    else:
        return {"mail" : "아무 메일도 없습니다."}


