from sqlmodel import SQLModel
from pydantic import EmailStr, ConfigDict
from typing import List, Optional


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


# simple
class SimplePeopleCreate(PeopleBase):
    pass


class SimpleNationalCard(NationalCardBase):
    pass

class SimpleDivision(DivisionBase):
    pass

class SimpleTeam(TeamBase):
    pass

# with relationships
class TeamSchema(TeamBase):
    peoples: List[PeopleBase]


class PeopleSchema(PeopleBase):
    teams: List[TeamBase]
    divisions: List[DivisionBase]
    national_card: Optional[NationalCardBase] = None


class DeleteItem(SQLModel):
    id: int
    ok: bool = True
    content: str

