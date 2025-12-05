from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from dependencies.dependencies import get_db
from user.user_schema import UserInDb, UserResponse
from user.user_repository import user_repository
from fastapi.security import OAuth2PasswordBearer
from auth.auth_service import auth_service
from typing import Annotated
from jwt.exceptions import InvalidTokenError
from typing import List
from dependencies.dependencies import get_current_user

router = APIRouter(
    prefix="/users", 
    tags=["users"],
    dependencies=[Depends(get_current_user)]
)


@router.get(
    "/",
    response_model=List[UserResponse],
    status_code=status.HTTP_201_CREATED
)
async def get_users(db: Session = Depends(get_db)):
    return await user_repository.get_all_users(db)


@router.get(
    "/{id}",
    response_model=UserResponse,
    status_code=status.HTTP_201_CREATED
)
async def get_user(
    db: Session = Depends(get_db), 
    id: int = None
):
    return await user_repository.get_user_by_id(db, id)


@router.get(
    "/me/",
    response_model=UserResponse,
    status_code=status.HTTP_201_CREATED
)
async def read_users_me(
    current_user: Annotated[str, Depends(get_current_user)] = None
):
    return current_user