from pydantic import BaseModel
from typing import List, Dict


class –°ouriersPost(BaseModel):
    data: List = None


class –°ouriersPatch(BaseModel):
    data: Dict = None


class OrdersPost(BaseModel):
    data: List = None


class OrdersAssignPost(BaseModel):
    courier_id: int