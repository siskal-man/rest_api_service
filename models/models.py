from pydantic import BaseModel
from typing import List, Optional, Dict


class Сouriers_post(BaseModel):
    data: List = None


class Сouriers_patch(BaseModel):
    data: Dict = None