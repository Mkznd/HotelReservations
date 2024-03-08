from fastapi import APIRouter, Depends

from config.db_config import get_db
from user.UserRepository import UserRepository
from user.UserService import UserService
from user.dto.UserCreate import UserCreate
from user.dto.UserGet import UserGet

router = APIRouter(prefix="/user", tags=["user"])
user_service = UserService(UserRepository())


@router.get("/", response_model=list[UserGet])
async def get_all(db=Depends(get_db)):
    return user_service.get_all_users(db)


@router.post("/", response_model=UserGet)
async def create_user(user: UserCreate, db=Depends(get_db)):
    return user_service.create_user(db, user)
