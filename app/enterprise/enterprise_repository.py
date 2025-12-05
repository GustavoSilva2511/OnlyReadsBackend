from sqlalchemy.orm import Session
from sqlalchemy import Select
from enterprise.enterprise_model import Enterprise
from enterprise.enterprise_schema import EnterpriseInDb, EnterpriseResponse
from dependencies.dependencies import get_coodinates
from typing import List
from geopy.distance import geodesic

class EnterpriseRepository:

    async def get_all_enterprises(self, db: Session) -> List[EnterpriseResponse]:
        stmt = (
            Select(Enterprise)
        )
        return db.scalars(stmt).all()


    async def get_enterprise_by_id(self, db: Session, id: int) -> EnterpriseResponse:
        stmt = (
            Select(Enterprise)
            .where(Enterprise.id==id)
        )
        return db.scalars(stmt).first()


    async def get_enterprise_by_cnpj(self, db: Session, cnpj: str) -> EnterpriseResponse:
        stmt = (
            Select(Enterprise)
            .where(Enterprise.cnpj==cnpj)
        )
        return db.scalars(stmt).first()     


    async def get_enterprise_around(self, db: Session, cep: str, distance: int) -> List[EnterpriseResponse]:
        coordinates = await get_coodinates(cep)
        latitude, longitude = coordinates[0], coordinates[1]
        request_coords = (latitude, longitude)
        enterprises = await self.get_all_enterprises(db)
        proximas = []
        for enterprise in enterprises:
            curr_coords = (enterprise.latitude, enterprise.longitude)
            current_distance = geodesic(request_coords, curr_coords)
            if current_distance.kilometers <= distance:
                enterprise.distance = float(current_distance.kilometers)
                proximas.append(enterprise)
        
        return proximas


    async def add_enterprise(self, db: Session, enterprise: EnterpriseInDb):
        if enterprise:
            enterprise = Enterprise(**enterprise.model_dump())
            coordinates = await get_coodinates(enterprise.cep)
            enterprise.latitude, enterprise.longitude = coordinates[0], coordinates[1]
            db.add(enterprise)
            db.commit()
            db.refresh(enterprise)
        return EnterpriseResponse.model_validate(enterprise) 



enterprise_repository = EnterpriseRepository()