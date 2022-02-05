from pydantic import BaseModel
from typing import List


class klargest(BaseModel):
    nums: List[int]
    k: int
