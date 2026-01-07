from sqlalchemy.orm import Session
from sqlalchemy import Select
from post.post_model import Post
from post.post_schema import PostInDb, PostResponse
from typing import List

class PostRepository:
    async def get_recomended_posts(self, db: Session) -> List[PostResponse]:
        stmt = (
            Select(Post)
        )
        return db.scalars(stmt).all()


    async def get_post_by_user(self, db: Session, user_id: int) -> PostResponse:
        stmt = (
            Select(Post)
            .where(Post.owner==user_id)
        )
        return db.scalars(stmt).first()


    async def create_post(self, db: Session, post: PostInDb) -> PostResponse:
        if Post:
            post = Post(**post.model_dump())
            db.add(post)
            db.commit()
            db.refresh(post)
        return PostResponse.model_validate(post) 

post_repository = PostRepository()