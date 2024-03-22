import logging
from typing import Optional

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Task(BaseModel):
    id: int
    title: str
    description: Optional[str] = None
    status: str
