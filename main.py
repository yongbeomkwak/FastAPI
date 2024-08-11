from typing import Union
from fastapi import FastAPI
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

#item_id int가 아닌 float을 전달하는 경우에 오류 발생
@app.get("/items/{item_id}")
async def read_item(item_id: int, q: Union[str,None] = None):
    return {"item_id" : item_id, "q" : q}

@app.put("/items/{item_id}")
def update_item(item_id: int, item: ItemDTO):
    return {"item_name": item.name, "item_id": item_id}

# 열거형 활용
@app.get("/models/{model_name}")
async def get_model(model_name: ModelName):
    if model_name is ModelName.alexnet:
        return {"model_name": model_name, "message": "Deep Learning FTW!"}

    elif model_name.value == "lenet":
        return {"model_name": model_name, "message": "LeCNN all the images"}

    else:
        return {"model_name": model_name, "message": "Have some residuals"}