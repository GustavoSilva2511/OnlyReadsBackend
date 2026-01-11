from sqlalchemy import (
    String
)

from sqlalchemy.orm import (
    Mapped, 
    mapped_column
)


from models.base import Base
from datetime import datetime


class Post(Base):
    __tablename__ = 'posts'
    id: Mapped[int] = mapped_column(primary_key=True)
    owner: Mapped[int]
    title: Mapped[str] = mapped_column(String(50))
    content: Mapped[str] = mapped_column(String(1000))
    is_public: Mapped[bool] = mapped_column(default=True)
    likes: Mapped[int] = mapped_column(default=0)
    date: Mapped[datetime]
