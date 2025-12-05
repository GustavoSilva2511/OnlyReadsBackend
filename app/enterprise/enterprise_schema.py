from pydantic import BaseModel, Field
from typing import Optional

class Enterprise(BaseModel):
    cnpj: str
    fantasy_name: str
    cep: str
    latitude: Optional[float] = None
    longitude : Optional[float] = None

class EnterpriseInDb(Enterprise):
    class Config:
        from_attributes = True

class EnterpriseResponse(Enterprise):
    id: int
    distance: float = None
    class Config:
        from_attributes = True