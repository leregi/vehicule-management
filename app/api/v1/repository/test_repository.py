from sqlmodel.ext.asyncio.session import AsyncSession
from ..models.test_mod import People, Division, NationalCard, Team
from ..schemas.test_schemas import DeleteItem
from  sqlmodel import select
from fastapi import HTTPException


# the complexe relationship case
class PeopleTeamsRepository():
    @staticmethod
    async def create_people_teams(data, session:AsyncSession):
        
        complete_people = People(
            fullname=data['fullname'],
            email=data['email'],
            teams = [
                Team(name=data["teams"][0]['name'])
            ],
            divisions=[
                Division(name=data["divisions"][0]['name'])
            ],
            national_card=NationalCard(cin=data['national_card']['cin'])
        )
        session.add(complete_people)
        await session.commit()
        await session.refresh(complete_people)
        return complete_people






class TestRepository():
    @staticmethod
    async def create_simple_people(session:AsyncSession,data):
        simple_people = People(fullname=data["fullname"],email=data["email"])
        session.add(simple_people)
        await session.commit()
        await session.refresh(simple_people)
        return simple_people
    
    @staticmethod
    async def create_simple_team(session:AsyncSession,data):
        simple_team = Team(name=data["name"])
        session.add(simple_team)
        await session.commit()
        await session.refresh(simple_team)
        return simple_team
    
    @staticmethod
    async def get_simple_people(session:AsyncSession):
        get_all_statement = select(People)
        exec_all = await session.exec(get_all_statement)
        simple_people_all = exec_all.all()
        return simple_people_all
    
    @staticmethod
    async def get_simple_team(session:AsyncSession):
        get_all_statement = select(Team)
        texec_all = await session.exec(get_all_statement)
        simple_team_all = texec_all.all()
        return simple_team_all
    
    @staticmethod
    async def get_simple_people_by_id(people_id,session:AsyncSession):
        simple_people = await session.get(People,people_id)
        if not simple_people:
            raise HTTPException(status_code=404, detail="people not found")
        return simple_people
    
    @staticmethod
    async def get_simple_team_by_id(team_id,session:AsyncSession):
        simple_team = await session.get(Team, team_id)
        if not simple_team:
            raise HTTPException(status_code=404, detail="team not found")
        return simple_team
    
    @staticmethod
    async def update_simple_people(data,people_id,session:AsyncSession):
        the_people = await session.get(People,people_id)
        if not the_people:
            raise HTTPException(status_code=404, detail="people not found")
        for k, v in data.items():
            setattr(the_people,k,v)
        session.add(the_people)
        await session.commit()
        await session.refresh(the_people)
        return the_people
    
    @staticmethod
    async def update_simple_team(data,team_id,session:AsyncSession):
        the_team = await session.get(Team,team_id)
        if not the_team:
            raise HTTPException(status_code=404, detail="team not found")
        for k, v in data.items():
            setattr(the_team,k,v)
        session.add(the_team)
        await session.commit()
        await session.refresh(the_team)
        return the_team

    @staticmethod
    async def delete_simple_people(people_id,session:AsyncSession):
        the_people = await session.get(People,people_id)
        if not the_people:
            raise HTTPException(status_code=404, detail="people not found")
        await session.delete(the_people)
        await session.commit()
        return DeleteItem(
            id = the_people.id,
            content=the_people.fullname
        )
    
    @staticmethod
    async def delete_simple_team(team_id,session:AsyncSession):
        the_team = await session.get(Team,team_id)
        if not the_team:
            raise HTTPException(status_code=404, detail="team not found")
        await session.delete(the_team)
        await session.commit()
        return DeleteItem(
            id = the_team.id,
            content=the_team.name
        )
        


