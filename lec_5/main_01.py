import logging  # логгирование
from typing import Optional

from fastapi import FastAPI
from pydantic import BaseModel

logging.basicConfig(level=logging.INFO) # логгирование
logger = logging.getLogger(__name__)  # логгирование

app = FastAPI()

class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    tax: Optional[float] = None

#1)
@app.get("/")
async def root():
    return {"Hello":"World"}

#2)
@app.get("/items/{item_id}")
async def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}

#3)GET запрос:
@app.get("/")
async def read_root():
    logger.info('Отработал GET запрос.') # логгирование - можно без него,просто с print,
    # но тогда надо закомментить строки с логгированием и вместо logger.info поставить print
    return {"Hello": "World"}

#4) POST запрос:
@app.post("/items/")
async def create_item(item: Item):
    logger.info('Отработал POST запрос.')
    return item

#5) PUT запрос - изменение существующих данных на сервере:
@app.put("/items/{item_id}")
async def update_item(item_id: int, item: Item):
    logger.info(f'Отработал PUT запрос для item id = {item_id}.')
    return {"item_id": item_id, "item": item}

#6) DELETE запрос:
@app.put("/items/{item_id}")
async def update_item(item_id: int, item: Item):
    logger.info(f'Отработал PUT запрос для item id = {item_id}.')
    return {"item_id": item_id, "item": item}