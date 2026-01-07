from pydantic import BaseModel
from datetime import datetime

class User(BaseModel):
    first_name: str
    last_name: str
    username: str
    created_at: datetime

class UserInDb(User):
    password: str
    email: str

    class Config:
        from_attributes = True
    
class UserResponse(User):
    id: int
    class Config:
        from_attributes = True