from pydantic import BaseModel
from typing import List, Dict


class СouriersPost(BaseModel):
    data: List = None


class СouriersPatch(BaseModel):
    data: Dict = None


class OrdersPost(BaseModel):
    data: List = None


class OrdersAssignPost(BaseModel):
    courier_id: int