from pydantic import BaseModel

class Post(BaseModel):
    owner: int
    title: str
    content: str
    private: bool
    date: str

class PostInDb(Post):
    class Config:
        from_attributes = True
    
class PostResponse(Post):
    id: int
    class Config:
        from_attributes = True