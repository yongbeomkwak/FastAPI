from pydantic import BaseModel
from typing import Union

def add(a,b):
    return a+b

class ItemDTO(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None

