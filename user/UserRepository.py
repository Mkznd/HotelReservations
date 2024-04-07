from fastapi import Depends
from sqlalchemy.orm import Session

from config.db_config import get_db
from user.User import User
from user.dto.UserCreate import UserCreate


class UserRepository:
    def get_by_id(self, db: Session, user_id: int) -> User | None:
        return db.query(User).filter(User.id == user_id).first()

    def get_by_email(self, db: Session, email: str) -> list[User]:
        return db.query(User).filter(User.email == email).first()

    def get_by_username(self, db: Session, username: str) -> list[User]:
        return db.query(User).filter(User.email == username).first()

    def get_byt_role(self, db: Session, role: str) -> list[User]:
        return db.query(User).filter(User.role == role).first()

    def get_all(self, db: Session, skip: int = 0, limit: int = 100) -> list[User]:
        return db.query(User).offset(skip).limit(limit).all()

    def create(self, db: Session, user: UserCreate) -> User:
        db_user = User(email=user.email, username=user.username)
        db.add(db_user)
        db.commit()
        db.refresh(db_user)
        return db_user

    def update(self, db: Session, user_id: int, user: UserCreate) -> User | None:
        db_user = db.query(User).filter(User.id == user_id).first()
        db_user.email = user.email
        db_user.username = user.username
        db.commit()
        db.refresh(db_user)
        return db_user

    def partial_update(
        self, db: Session, user_id: int, user: UserCreate
    ) -> User | None:
        db_user = db.query(User).filter(User.id == user_id).first()
        if user.email is not None:
            db_user.email = user.email
        if user.username is not None:
            db_user.username = user.username
        db.commit()
        db.refresh(db_user)
        return db_user

    def delete(self, db: Session, user_id: int):
        db_user = db.query(User).filter(User.id == user_id).first()
        db.delete(db_user)
        db.commit()
