from sqlalchemy.orm import Session
from sqlalchemy import Select
from user.user_model import User
from user.user_schema import UserInDb, UserResponse
from typing import List
from auth.auth_service import auth_service

class UserRepository:

    async def get_all_users(self, db: Session) -> List[UserResponse]:
        stmt = (
            Select(User)
        )
        return db.scalars(stmt).all()


    async def get_user_by_id(self, db: Session, id: int) -> UserResponse:
        stmt = (
            Select(User)
            .where(User.id==id)
        )
        return db.scalars(stmt).first()


    async def get_user_by_email(self, db: Session, email: str) -> UserResponse:
        stmt = (
            Select(User)
            .where(User.email==email)
        )
        return db.scalars(stmt).first()     


    async def add_user(self, db: Session, user: UserInDb) -> UserResponse:
        if user:
            user.password = auth_service.password_to_hash(user.password)
            user = User(**user.model_dump())
            db.add(user)
            db.commit()
            db.refresh(user)
        return UserResponse.model_validate(user) 

user_repository = UserRepository()