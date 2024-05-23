from fastapi import APIRouter, HTTPException, status, Depends
from typing import Union, List
from sqlmodel.ext.asyncio.session import AsyncSession

from ..schemas.test_schemas import SimplePeopleCreate, SimpleTeam
from ..repository.test_repository import TestRepository
from ..db.connection import get_async_session

test_router = APIRouter()

# A people crud only
@test_router.post("/a_simple_people",
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

@test_router.post("/a_simple_team",
    response_model=SimpleTeam,
    status_code=status.HTTP_200_OK  ,                
)
async def add_test_team(simple_team:SimpleTeam, session:AsyncSession = Depends(get_async_session)):
    simple_team_data = simple_team.model_dump()
    if not simple_team_data:
            raise HTTPException(status_code=400, detail="bad request")
    registered_simple_team = await TestRepository.create_simple_team(data=simple_team_data,session=session)
    if not registered_simple_team:
            raise HTTPException(status_code=400, detail="bad request on the DB action")
    return registered_simple_team
    

@test_router.get("/a_simple_peoples",
    response_model=List[SimplePeopleCreate],
    status_code=status.HTTP_200_OK  ,                
)
async def get_test(session:AsyncSession = Depends(get_async_session)):
    get_simple_people = await TestRepository.get_simple_people(session=session)
    if not get_simple_people:
            raise HTTPException(status_code=400, detail="bad request on the DB action")
    return get_simple_people

@test_router.get("/a_simple_teams",
    response_model=List[SimpleTeam],
    status_code=status.HTTP_200_OK  ,                
)
async def get_test_team(session:AsyncSession = Depends(get_async_session)):
    get_simple_team = await TestRepository.get_simple_team(session=session)
    if not get_simple_team:
            raise HTTPException(status_code=400, detail="bad request on the DB action")
    return get_simple_team
