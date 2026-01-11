from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from dependencies.dependencies import get_db
from post.post_schema import PostInDb, PostResponse
from post.post_repository import post_repository
from fastapi.security import OAuth2PasswordBearer
from auth.auth_service import auth_service
from typing import Annotated
from jwt.exceptions import InvalidTokenError
from typing import List
from dependencies.dependencies import get_current_user
from user.user_model import User

router = APIRouter(
    prefix="/posts", 
    tags=["posts"],
    dependencies=[Depends(get_current_user)]
)

@router.get(
    "/recommended",
    response_model=List[PostResponse],
    status_code=status.HTTP_200_OK
)
async def get_recommended_posts(db: Session = Depends(get_db)):
    return await post_repository.get_recomended_posts(db)

@router.get(
    "/my",
    response_model=List[PostResponse],
    status_code=status.HTTP_200_OK
)
async def get_my_posts(
    db: Session = Depends(get_db),
    current_user: Annotated[User, Depends(get_current_user)] = None
):
    return await post_repository.get_post_by_user(db, current_user.id)

@router.get("/search")
async def search_posts(
    db: Session = Depends(get_db),
    search: str = ""
):
    if search:
        return await post_repository.search_posts(db, search)
    
    return await post_repository.get_recomended_posts(db)

@router.post(
    "/",
    response_model=PostResponse,
    status_code=status.HTTP_201_CREATED
)
async def create_post(
    db: Session = Depends(get_db),
    post: PostInDb = None
):
    return await post_repository.create_post(db, post)


@router.put(
    "/{id}/like",
    status_code=status.HTTP_204_NO_CONTENT
)
async def like_post(
    id: int = None,
    db: Session = Depends(get_db)
):
    res = await post_repository.anonymous_like_post(db, id)
    print(res)
    return res

