from pydantic import BaseModel


class UserCreate(BaseModel):
    email: str
    username: str

    class Config:
        from_attributes = True
