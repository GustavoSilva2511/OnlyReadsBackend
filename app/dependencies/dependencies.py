from typing import Annotated
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jwt import InvalidTokenError
from pytest import Session
from auth.auth_service import auth_service
from user.user_repository import user_repository
from db.session import local_session
from user.user_schema import UserResponse
from requests import get

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/login")

def get_db():
    with local_session() as session:
        yield session

async def get_current_user(
    db: Session = Depends(get_db),
    token: Annotated[str, Depends(oauth2_scheme)] = None
) -> HTTPException | UserResponse:
    credentials_exception = HTTPException(

        status_code=status.HTTP_401_UNAUTHORIZED,

        detail="Could not validate credentials",

        headers={"WWW-Authenticate": "Bearer"},

    )
    try:
        decoded_token = auth_service.decode_access_token(token)
        email = decoded_token.get("sub")
        user = await user_repository.get_user_by_email(db, email)
    
    except InvalidTokenError:
        raise credentials_exception
    
    except:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid token")


    if user is None:
        raise credentials_exception
    
    return user 


async def get_coodinates(cep: str) -> tuple:
    api_url = f"https://brasilapi.com.br/api/cep/v2/{cep}"
    response = get(api_url).json()
    coordinates = response.get("location", {}).get("coordinates", {})
    latitude = coordinates.get("latitude", None)
    longitude = coordinates.get("longitude", None)
    return (latitude, longitude)
    