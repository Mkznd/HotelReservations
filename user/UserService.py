from user.User import User
from user.UserRepository import UserRepository
from user.dto.UserCreate import UserCreate


class UserService:
    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository

    def create_user(self, db, user: UserCreate):
        return self.user_repository.create(db, user)

    def get_user_by_id(self, db, id: int) -> User:
        return self.user_repository.get_by_id(db, id)

    def get_user_by_username(self, db, username: str) -> User:
        return self.user_repository.get_by_username(db, username)

    def get_user_by_email(self, db, email: str) -> User:
        return self.user_repository.get_by_email(db, email)

    def get_users_by_role(self, db, role: str) -> list[User]:
        return self.user_repository.get_by_role(db, role)

    def get_all_users(self, db) -> list[User]:
        return self.user_repository.get_all(db)

    def update_user(self, db, id: int, user: UserCreate) -> User:
        return self.user_repository.update(db, id, user)

    def partial_update_user(self, db, id: int, user: UserCreate) -> User:
        return self.user_repository.partial_update(db, id, user)

    def delete_user(self, db, id: int) -> None:
        return self.user_repository.delete(db, id)
