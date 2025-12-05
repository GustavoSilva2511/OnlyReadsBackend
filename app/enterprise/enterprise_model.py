from sqlalchemy import (
    String,
    Float
)

from sqlalchemy.orm import (
    Mapped, 
    mapped_column
)


from models.base import Base

class Enterprise(Base):
    __tablename__ = 'enterprises'
    id: Mapped[int] = mapped_column(primary_key=True)
    cnpj: Mapped[str] = mapped_column(String(14), unique=True)
    fantasy_name: Mapped[str] = mapped_column(String(50))
    cep: Mapped[str] = mapped_column(String(8))
    latitude: Mapped[float] = mapped_column(Float(precision=8))
    longitude: Mapped[float] = mapped_column(Float(precision=8))
