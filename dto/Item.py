from pydantic import BaseModel
from typing import Union

def add(a,b):
    return a+b

class ItemDTO(BaseModel):
    name: str
    price: float
    is_offer: Union[bool, None] = None

