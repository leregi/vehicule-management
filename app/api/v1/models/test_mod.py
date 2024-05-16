from sqlmodel import Field, SQLModel, Relationship
from datetime import datetime
from typing import Optional,List

# Many to Many
class PeopleTeam(SQLModel,table=True):
    people_id: Optional[int] = Field(default=None, foreign_key="people.id",primary_key=True)
    team_id: Optional[int] = Field(default=None, foreign_key="team.id",primary_key=True)
    created_at:Optional[datetime] = Field(default_factory=datetime.UTC)
    updated_at:Optional[datetime] = Field(
                                            default_factory=datetime.UTC,
                                            sa_column_kwargs={"onupdate": datetime.UTC}
                                        )

class People(SQLModel, table=True):
    id: int = Field(primary_key=True,nullable=False)
    fullname:str
    email:str = Field(unique=True)
    # People has one National Card
    national_card:Optional['NationalCard'] = Relationship(
        sa_relationship_kwargs={'uselist': False},
        back_populates="people"
    )
    # People has many Division
    divisions:List["Division"] = Relationship(back_populates="people")
    # Many to Many
    teams:List["Team"] =Relationship(back_populates="peoples",link_model=PeopleTeam)
    # TimeStamp
    created_at:Optional[datetime] = Field(default_factory=datetime.UTC)
    updated_at:Optional[datetime] = Field(default_factory=datetime.UTC,
                                            sa_column_kwargs={"onupdate": datetime.UTC}
                                        )

# one to one relationships
class NationalCard(SQLModel,table=True):
    id: int = Field(primary_key=True,nullable=False)
    cin: str = Field(unique=True)
    # People has one National Card
    people_id:Optional[int] = Field(default=None,foreign_key="people.id")
    people: Optional['People'] = Relationship(back_populates="national_card")
        # TimeStamp
    created_at:Optional[datetime] = Field(default_factory=datetime.UTC)
    updated_at:Optional[datetime] = Field(
                                            default_factory=datetime.UTC,
                                            sa_column_kwargs={"onupdate": datetime.UTC}
                                        )

# one to many relationships
class Division(SQLModel,table=True):
    id:int = Field(primary_key=True,nullable=False)
    name:str
    # People has many division
    people_id:Optional[int] = Field(default=None,foreign_key="people.id")
    people:Optional["People"] = Relationship(back_populates="divisions")
    # TimeStamp
    created_at:Optional[datetime] = Field(default_factory=datetime.UTC)
    updated_at:Optional[datetime] = Field(
                                            default_factory=datetime.UTC,
                                            sa_column_kwargs={"onupdate": datetime.UTC}
                                        )

# many to many relationship
class Team(SQLModel,table=True):
    id:int = Field(nullable=False, primary_key=True)
    name:str
    # many to many
    peoples:Optional["People"] = Relationship(back_populates="teams",link_model=PeopleTeam)
    # TimeStamp
    created_at:Optional[datetime] = Field(default_factory=datetime.UTC)
    updated_at:Optional[datetime] = Field(
                                            default_factory=datetime.UTC,
                                            sa_column_kwargs={"onupdate": datetime.UTC}
                                        )

