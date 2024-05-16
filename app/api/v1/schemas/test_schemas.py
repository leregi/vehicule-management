from sqlmodel import SQLModel
from pydantic import EmailStr, ConfigDict


class PeopleBase(SQLModel):
    model_config = ConfigDict(from_attributes=True)
    fullname:str
    email:EmailStr

class NationalCardBase(SQLModel):
    model_config = ConfigDict(from_attributes=True)
    cin:str

class DivisionBase(SQLModel):
    model_config = ConfigDict(from_attributes=True)
    name:str

class TeamBase(SQLModel):
    model_config = ConfigDict(from_attributes=True)
    name:str


class SimplePeopleCreate(PeopleBase):
    pass
