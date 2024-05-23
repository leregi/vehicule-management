from sqlmodel.ext.asyncio.session import AsyncSession
from ..models.test_mod import People, Division, NationalCard, Team
from  sqlmodel import select


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

    


