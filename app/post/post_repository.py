from sqlalchemy.orm import Session
from sqlalchemy import select, update, desc
from post.post_model import Post
from post.post_schema import PostInDb, PostResponse
from typing import List

class PostRepository:
    async def get_recomended_posts(self, db: Session) -> List[PostResponse]:
        stmt = (
            select(Post)
            .where(Post.is_public==True)
            .order_by(desc(Post.likes))
        )
        return db.scalars(stmt).all()


    async def get_post_by_user(self, db: Session, user_id: int) -> List[PostResponse]:
        stmt = (
            select(Post)
            .where(Post.owner==user_id)
            .order_by(desc(Post.date))
        )
        return db.scalars(stmt).all()


    async def create_post(self, db: Session, post: PostInDb) -> PostResponse:
        if Post:
            post = Post(**post.model_dump())
            db.add(post)
            db.commit()
            db.refresh(post)
        return PostResponse.model_validate(post) 


    async def anonymous_like_post(self, db: Session, id: int) -> bool:
        stmt = (
            update(Post)
            .where(Post.id == id)
            .values(likes=Post.likes+1)
        )
        print(stmt)
        db.execute(stmt)
        db.commit()
        return True


    async def search_posts(self, db: Session, search: str) -> List[PostResponse]:
        stmt = (
            select(Post)
            .where(Post.is_public==True)
            .where(Post.title.startswith(search) or Post.title.contains(search))
            .order_by(desc(Post.likes))
        )
        return db.scalars(stmt).all()

post_repository = PostRepository()