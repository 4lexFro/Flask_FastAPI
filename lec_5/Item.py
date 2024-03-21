from typing import Optional
from pydantic import BaseModel



class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    tax: Optional[float] = None

# так выглядит создание класса Item. Это все печатается в main_01, этот файл отдельно
#создан просто для примера