from pydantic import BaseModel
from typing import Union


class Recording(BaseModel):
    member_id: str
    member_nickname: str
    file_name: str
