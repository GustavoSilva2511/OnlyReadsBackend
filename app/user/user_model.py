from sqlalchemy import (
    String
)

from sqlalchemy.orm import (
    Mapped, 
    mapped_column
)

from datetime import datetime

from models.base import Base

class User(Base):
    __tablename__ = 'users'
    id: Mapped[int] = mapped_column(primary_key=True)
    first_name: Mapped[str] = mapped_column(String(50))
    last_name: Mapped[str] = mapped_column(String(50))
    username: Mapped[str] = mapped_column(String(50), unique=True)
    email: Mapped[str] = mapped_column(String(100), unique=True)
    password: Mapped[str] = mapped_column(String(150))
    created_at: Mapped[datetime]
