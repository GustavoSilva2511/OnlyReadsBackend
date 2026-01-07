from sqlalchemy import (
    String
)

from sqlalchemy.orm import (
    Mapped, 
    mapped_column
)


from models.base import Base

class Post(Base):
    __tablename__ = 'posts'
    id: Mapped[int] = mapped_column(primary_key=True)
    owner: Mapped[str] = mapped_column(String(50))
    title: Mapped[str] = mapped_column(String(50))
    content: Mapped[str] = mapped_column(String(1000))
    private: Mapped[bool] = mapped_column()
    date: Mapped[str] = mapped_column(String(30))
