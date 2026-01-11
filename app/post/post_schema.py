from pydantic import BaseModel
from datetime import datetime
class Post(BaseModel):
    owner: int
    title: str
    content: str
    is_public: bool
    likes: int
    date: datetime

class PostInDb(Post):
    class Config:
        from_attributes = True
    
class PostResponse(Post):
    id: int
    class Config:
        from_attributes = True