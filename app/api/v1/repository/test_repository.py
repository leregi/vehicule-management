from sqlmodel.ext.asyncio.session import AsyncSession
from ..models.test_mod import People


class TestRepository():
    @staticmethod
    async def create_simple_people(session:AsyncSession,data):
        simple_people = People(fullname=data.fullname,email=data.email)
        session.add(simple_people)
        session.commit()
        return simple_people
    
    # people -> national_card (CRUD)


    # people -< divisions (CRUD)

    # peoples >-< teams (CRUD)
