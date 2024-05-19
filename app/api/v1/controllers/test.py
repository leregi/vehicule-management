from fastapi import APIRouter, HTTPException, status, Depends
from typing import Union
from sqlmodel.ext.asyncio.session import AsyncSession

from ..schemas.test_schemas import SimplePeopleCreate
from ..repository.test_repository import TestRepository
from ..db.connection import get_async_session

test_router = APIRouter()

@test_router.post("/",
    response_model=SimplePeopleCreate,
    status_code=status.HTTP_200_OK  ,                
)
async def add_test(simple_people:SimplePeopleCreate, session:AsyncSession = Depends(get_async_session)):
    simple_people_data = simple_people.model_dump()
    if not simple_people_data:
            raise HTTPException(status_code=400, detail="bad request")
    registered_simple_people = await TestRepository.create_simple_people(data=simple_people_data,session=session)
    if not registered_simple_people:
            raise HTTPException(status_code=400, detail="bad request on the DB action")
    return registered_simple_people

    
