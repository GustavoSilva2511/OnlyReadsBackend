from pydantic import BaseModel

class User(BaseModel):
    first_name: str
    last_name: str
    email: str

class UserInDb(User):
    password: str

    class Config:
        from_attributes = True
    
class UserResponse(User):
    id: int
    class Config:
        from_attributes = True