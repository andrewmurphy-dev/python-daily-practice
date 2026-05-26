#so this is the basic structure of a fast api !

from fastapi import FastAPI
from pydantic import BaseModel, Field


app = FastAPI()

#error and validation !

class MenuItem(BaseModel):
    name: str = Field(Min_length=1)
    price: int = Field(gt=0)
    category: str = Field(Min_length=1)














