from fastapi import APIRouter, HTTPException, status, Depends
from typing import Union, List
from sqlmodel.ext.asyncio.session import AsyncSession

from ..schemas.vehicule_schemas import CreateVehicule
from ..repository.vehicule_repository import VehiculeRepository
from ..db.connection import get_async_session

vehicule_router = APIRouter()

# CREATE
@vehicule_router.post("/add_vehicule",
    response_model=CreateVehicule,
    status_code=status.HTTP_200_OK  ,                
)
async def add_vehicule(vehicule:CreateVehicule, session:AsyncSession = Depends(get_async_session)):
    vehicule_data = vehicule.model_dump()
    if not vehicule_data:
            raise HTTPException(status_code=400, detail="bad request")
    registered_vehicule = await VehiculeRepository.create_vehicule(data=vehicule_data,session=session)
    if not registered_vehicule:
            raise HTTPException(status_code=400, detail="bad request on the DB action")
    return registered_vehicule


""" 
# GET ALL
@vehicule_router.get("/",
    response_model=List[SimplePeopleCreate],
    status_code=status.HTTP_200_OK  ,                
)
async def get_test(session:AsyncSession = Depends(get_async_session)):
    get_simple_people = await TestRepository.get_simple_people(session=session)
    if not get_simple_people:
            raise HTTPException(status_code=400, detail="bad request on the DB action")
    return get_simple_people

# GET BY ID
@vehicule_router.get("/vehicule/{vehicule_id}",
    response_model=SimplePeopleCreate,
    status_code=status.HTTP_200_OK  ,                
)
async def get_test_by_id(vehicule_id:int,session:AsyncSession = Depends(get_async_session)):
    get_simple_people_by_id = await TestRepository.get_simple_people_by_id(vehicule_id,session=session)
    if not get_simple_people_by_id:
            raise HTTPException(status_code=400, detail="bad request on the DB action")
    return get_simple_people_by_id



# UPDATE
@vehicule_router.put("/vehicule/{vehicule_id}",
    response_model=SimplePeopleCreate,
    status_code=status.HTTP_200_OK  ,                
)
async def update_people(people_data:SimplePeopleCreate,vehicule_id:int,session:AsyncSession = Depends(get_async_session)):
        a_new_people = people_data.model_dump()
        if not a_new_people:
                raise HTTPException(status_code=400, detail="bad request")
        update_people = await TestRepository.update_simple_people(a_new_people,vehicule_id,session=session)
        if not update_people:
                raise HTTPException(status_code=400, detail="bad request on the DB action")
        return update_people

@vehicule_router.put("/a_simple_team/{team_id}",
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
@vehicule_router.delete("/a_simple_people/{vehicule_id}",
    response_model=DeleteItem,
    status_code=status.HTTP_200_OK,                
)
async def delete_people(vehicule_id:int,session:AsyncSession = Depends(get_async_session)):
        delete_people = await TestRepository.delete_simple_people(vehicule_id,session=session)
        if not delete_people:
                raise HTTPException(status_code=400, detail="bad request on the DB action")
        return delete_people

 """