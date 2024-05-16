from sqlmodel import SQLModel
from pydantic import EmailStr


class PeopleBase(SQLModel):
    fullname:str
    email:EmailStr

class NationalCardBase(SQLModel):
    cin:str

class DivisionBase(SQLModel):
    name:str

class TeamBase(SQLModel):
    name:str
