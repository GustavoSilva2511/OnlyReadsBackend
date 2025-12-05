from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from auth.auth_service import auth_service
from sqlalchemy.orm import Session
from dependencies.dependencies import get_db
from user.user_repository import user_repository
from auth.auth_schema import Token
from user.user_schema import UserInDb, UserResponse

router = APIRouter(prefix="/auth")

@router.post("/login")
async def auth_token(db: Session = Depends(get_db), form_data: OAuth2PasswordRequestForm = Depends()):
    user = await user_repository.get_user_by_email(db, form_data.username)
    if not user or not auth_service.verify_password(form_data.password, user.password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )

    access_token = auth_service.create_access_token(
        data={"sub": user.email}
    )
    
    return Token(access_token=access_token, token_type="bearer")

# ADD: REGISTAR USUARIO COM VERIFICACAO DE EMAIL TOKEN
@router.post(
    "/register",
    response_model=UserResponse,
    status_code=status.HTTP_201_CREATED
)
async def post_user(
    db: Session = Depends(get_db),
    user: UserInDb = None
):
    return await user_repository.add_user(db, user)
