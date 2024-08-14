from typing import Union
from fastapi import FastAPI , Query
from pydantic import BaseModel
from dto import *


app = FastAPI()

@app.get("/")

async def read_root():
    return {"Hello" : "Wrold" }

# 고정 경로가 항상 위에 
@app.get("/users/me")
async def read_user_me():
    return {"user_id": "the current user"}

# 열거형 활용
@app.get("/models/{model_name}")
async def get_model(model_name: ModelName):
    if model_name is ModelName.alexnet:
        return {"model_name": model_name, "message": "Deep Learning FTW!"}

    elif model_name.value == "lenet":
        return {"model_name": model_name, "message": "LeCNN all the images"}

    else:
        return {"model_name": model_name, "message": "Have some residuals"}
    

@app.get("/items/{item_id}")
async def read_user_item(
    item_id: str, needy: str, skip: int = 0, limit: Union[int, None] = None
):
    
    #needy, 필수적인 str. = 기본 값 없음
    #skip, 기본값이 0인 int. = 기본값 있음
    #limit, 선택적인 int. = 선택적 파라미터, 값이 있으면 int여야하고 없으면 None

    item = {"item_id": item_id, "needy": needy, "skip": skip, "limit": limit}
    return item



@app.put("/items/{item_id}")
async def update_item(item_id: int, item: ItemDTO, q: str | None = None):
    print(item_id, item, q)
    result = {"item_id": item_id}
    if q:
        result.update({"q": q})
    return result


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
):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results

