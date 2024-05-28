""" from fastapi import APIRouter, HTTPException, status, Depends
from typing import Union, List
from sqlmodel.ext.asyncio.session import AsyncSession

from ..schemas.test_schemas import SimplePeopleCreate, SimpleTeam, DeleteItem, PeopleSchema
from ..repository.test_repository import TestRepository,PeopleTeamsRepository
from ..db.connection import get_async_session

test_router = APIRouter()

# CREATE
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
    

# GET ALL
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

# GET BY ID
@test_router.get("/a_simple_people/{people_id}",
    response_model=SimplePeopleCreate,
    status_code=status.HTTP_200_OK  ,                
)
async def get_test_by_id(people_id:int,session:AsyncSession = Depends(get_async_session)):
    get_simple_people_by_id = await TestRepository.get_simple_people_by_id(people_id,session=session)
    if not get_simple_people_by_id:
            raise HTTPException(status_code=400, detail="bad request on the DB action")
    return get_simple_people_by_id

@test_router.get("/a_simple_team/{team_id}",
    response_model=SimpleTeam,
    status_code=status.HTTP_200_OK  ,                
)
async def get_test_team_by_id(team_id:int, session:AsyncSession = Depends(get_async_session)):
    get_simple_team_by_id = await TestRepository.get_simple_team_by_id(team_id,session=session)
    if not get_simple_team_by_id:
            raise HTTPException(status_code=400, detail="bad request on the DB action")
    return get_simple_team_by_id

# UPDATE
@test_router.put("/a_simple_people/{people_id}",
    response_model=SimplePeopleCreate,
    status_code=status.HTTP_200_OK  ,                
)
async def update_people(people_data:SimplePeopleCreate,people_id:int,session:AsyncSession = Depends(get_async_session)):
        a_new_people = people_data.model_dump()
        if not a_new_people:
                raise HTTPException(status_code=400, detail="bad request")
        update_people = await TestRepository.update_simple_people(a_new_people,people_id,session=session)
        if not update_people:
                raise HTTPException(status_code=400, detail="bad request on the DB action")
        return update_people

@test_router.put("/a_simple_team/{team_id}",
    response_model=SimpleTeam,
    status_code=status.HTTP_200_OK  ,                
)
async def update_team(team_data:SimpleTeam,team_id:int, session:AsyncSession = Depends(get_async_session)):
        a_new_team = team_data.model_dump()
        if not a_new_team:
                raise HTTPException(status_code=400, detail="bad request")
        update_team = await TestRepository.update_simple_team(a_new_team,team_id,session=session)
        if not update_team:
                raise HTTPException(status_code=400, detail="bad request on the DB action")
        return update_team

# DELETE
@test_router.delete("/a_simple_people/{people_id}",
    response_model=DeleteItem,
    status_code=status.HTTP_200_OK,                
)
async def delete_people(people_id:int,session:AsyncSession = Depends(get_async_session)):
        delete_people = await TestRepository.delete_simple_people(people_id,session=session)
        if not delete_people:
                raise HTTPException(status_code=400, detail="bad request on the DB action")
        return delete_people

@test_router.delete("/a_simple_team/{team_id}",
    response_model=DeleteItem,
    status_code=status.HTTP_200_OK,                
)
async def delete_team(team_id:int, session:AsyncSession = Depends(get_async_session)):
        delete_team = await TestRepository.delete_simple_team(team_id,session=session)
        if not delete_team:
                raise HTTPException(status_code=400, detail="bad request on the DB action")
        return delete_team

# PEOPLE AND TEAMS
@test_router.post("/people_teams",
    response_model=PeopleSchema,
    status_code=status.HTTP_200_OK  ,                
)
async def add_test(people_teams:PeopleSchema, session:AsyncSession = Depends(get_async_session)):
    people_teams_data = people_teams.model_dump()
    if not people_teams_data:
            raise HTTPException(status_code=400, detail="bad request")
    registered_people_teams = await PeopleTeamsRepository.create_people_teams(data=people_teams_data,session=session)
    if not registered_people_teams:
            raise HTTPException(status_code=400, detail="bad request on the DB action")
    return registered_people_teams
 """
