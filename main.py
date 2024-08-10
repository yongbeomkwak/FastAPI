from typing import Union
from fastapi import FastAPI
from pydantic import BaseModel
from dto import *


app = FastAPI()

@app.get("/")

async def read_root():
    return {"Hello" : "Wrold" }

@app.get("/items/{item_id}")
async def read_item(item_id: int, q: Union[str,None] = None):
    return {"item_id" : item_id, "q" : q}

@app.put("/items/{item_id}")
def update_item(item_id: int, item: ItemDTO):
    return {"item_name": item.name, "item_id": item_id}