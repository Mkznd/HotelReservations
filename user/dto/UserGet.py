from datetime import datetime

from pydantic import BaseModel


class UserGet(BaseModel):
    id: int
    email: str
    is_active: bool
    time_created: datetime

    class Config:
        from_attributes = True
