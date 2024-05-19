from sqlmodel.ext.asyncio.session import AsyncSession
from ..models.test_mod import People, Division, NationalCard, Team
from  sqlmodel import select


class TestRepository():
    @staticmethod
    async def create_simple_people(session:AsyncSession,data):
        simple_people = People(fullname=data["fullname"],email=data["email"])
        session.add(simple_people)
        session.commit()
        await session.refresh(simple_people)
        return simple_people
    
    # people -> national_card (CRUD)


    # people -< divisions (CRUD)

    # peoples >-< teams (CRUD)
    @staticmethod
    async def create_people_with_teams(session:AsyncSession,data):
        people_and_teams = People(
            fullname= data.fullname,
            email= data.email,
            teams= [Team(name=data.name) for data in data.teams]        
        )
        session.add(people_and_teams)
        session.commit()
        session.refresh(people_and_teams)
        return people_and_teams

    @staticmethod
    async def update_people_teams(session:AsyncSession, data):
        people = session.exec(
            select(People).where(People.id == data.people_id)
        ).first()


