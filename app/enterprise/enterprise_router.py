from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from dependencies.dependencies import get_db
from enterprise.enterprise_schema import EnterpriseInDb, EnterpriseResponse
from enterprise.enterprise_repository import enterprise_repository
from auth.auth_service import auth_service
from typing import List
from dependencies.dependencies import get_current_user

router = APIRouter(
    prefix="/enterprises", 
    tags=["enterprises"],
    dependencies=[Depends(get_current_user)]
)


@router.get(
    "/",
    response_model=List[EnterpriseResponse],
    status_code=status.HTTP_200_OK
)
async def get_all_enterprises(db: Session = Depends(get_db)):
    return await enterprise_repository.get_all_enterprises(db)


@router.get(
    "/{id}",
    response_model=EnterpriseResponse,
    status_code=status.HTTP_200_OK
)
async def get_enterprise_by_id(
    db: Session = Depends(get_db), 
    id: int = None
):
    return await enterprise_repository.get_enterprise_by_id(db, id)

@router.get(
    "/around/{cep}/{distance}",
    response_model=List[EnterpriseResponse],
    status_code=status.HTTP_200_OK
)
async def get_enterprise_around(
    db: Session = Depends(get_db), 
    cep: str = None,
    distance: int = 5
):
    return await enterprise_repository.get_enterprise_around(db, cep, distance)

@router.post(
    "/",
    response_model=EnterpriseResponse,
    status_code=status.HTTP_201_CREATED
)
async def add_enterprise(
    db: Session = Depends(get_db),
    enterprise: EnterpriseInDb = None
):
    return await enterprise_repository.add_enterprise(db, enterprise)
