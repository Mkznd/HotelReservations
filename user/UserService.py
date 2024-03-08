from user.User import User
from user.UserRepository import UserRepository
from user.dto.UserCreate import UserCreate


class UserService:
    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository

    def get_all_users(self, db) -> list[User]:
        return self.user_repository.get_users(db)

    def create_user(self, db, user: UserCreate) -> User:
        return self.user_repository.create_user(db, user)
