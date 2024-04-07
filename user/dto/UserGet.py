from pydantic import BaseModel


class UserGet(BaseModel):
    id: int
    email: str
    username: str

    class Config:
        from_attributes = True
