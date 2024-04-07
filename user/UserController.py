from fastapi import APIRouter, Depends

from config.db_config import get_db
from user.User import Role
from user.UserRepository import UserRepository
from user.UserService import UserService
from user.dto.UserCreate import UserCreate
from user.dto.UserGet import UserGet

router = APIRouter(prefix="/user", tags=["user"])
user_service = UserService(UserRepository())


@router.post("/", response_model=UserGet)
async def create_user(user: UserCreate, db=Depends(get_db)):
    return user_service.create_user(db, user)


@router.get("/", response_model=UserGet)
async def get_user_by_username_email_role(
    username: str = None, email: str = None, role: Role = None, db=Depends(get_db)
):
    if username is not None:
        return user_service.get_user_by_username(db, username)
    elif email is not None:
        return user_service.get_user_by_email(db, email)
    elif role is not None:
        return user_service.get_users_by_role(db, role)
    else:
        return user_service.get_all_users(db)


@router.get("/{id}", response_model=UserGet)
async def update_user(id: int, db=Depends(get_db)):
    return user_service.get_user_by_id(db, id)


@router.put("/{id}", response_model=UserGet)
async def update_user(id: int, user: UserCreate, db=Depends(get_db)):
    return user_service.update_user(db, id, user)


@router.patch("/{id}", response_model=UserGet)
async def partial_update_user(id: int, user: UserCreate, db=Depends(get_db)):
    return user_service.partial_update_user(db, id, user)


@router.delete("/{id}", response_model=UserGet)
async def delete_user(id: int, db=Depends(get_db)):
    return user_service.delete_user(db, id)
