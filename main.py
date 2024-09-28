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

@app.get("/items/{item_id}")
async def update_item(item_id: int):
    return {"item_id": item_id}