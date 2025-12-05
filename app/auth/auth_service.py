from fastapi import Depends

from datetime import datetime, timedelta
from user.user_model import User
from core.config import settings
from pwdlib import PasswordHash
from typing import Optional
from auth.auth_schema import TokenData
from sqlalchemy.orm import Session
import jwt
from jwt.exceptions import DecodeError

class AuthService:
    def __init__(self):
        self.password_hash = PasswordHash.recommended()

    def password_to_hash(self, password: str):
        return self.password_hash.hash(password)
    
    def verify_password(self, password: str, hash_password: str):
        return self.password_hash.verify(password, hash_password)
        

    def create_access_token(self, data: dict, expires_delta: Optional[timedelta] = None):
        """Creates a signed JWT access token."""
        to_encode = data.copy()
        if expires_delta:
            expire = datetime.utcnow() + expires_delta
        else:
            expire = datetime.utcnow() + timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
        
        # Add standard claims: 'exp' (expiration time) and 'iat' (issued at time)
        to_encode.update({"exp": expire, "iat": datetime.utcnow()})

        encoded_jwt = jwt.encode(to_encode, settings.SECRET_KEY, algorithm=settings.ALGORITHM)
        return encoded_jwt
    
    
    def decode_access_token(self, token: str):
        """Decodes and verifies a JWT access token."""
        try:
            payload = jwt.decode(token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM])
            return payload
        except jwt.PyJWTError as e:
            raise e


auth_service = AuthService()