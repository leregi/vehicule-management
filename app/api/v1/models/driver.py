from sqlmodel import Field, SQLModel, Relationship
from datetime import datetime, timezone
from typing import Optional,List, Callable
from sqlalchemy import func, Column, DateTime
from decimal import Decimal

from .licence import Licence
from .driver_licence import DriverLicence

class Driver(SQLModel,table=True):
    id:Optional[int] = Field(default=None,primary_key=True)
    firstname:str
    lastname: str
    email:str = Field(unique=True)
    password:str
    telephone:str
    licences: List[Licence] = Relationship(back_populates="drivers",sa_relationship_kwargs={'lazy': 'selectin'}, link_model=DriverLicence)
    created_at:datetime = Field(
        #default_factory=datetime.now(tz=timezone.utc)
         sa_column=Column(
            DateTime(timezone=True), server_default=func.now(), nullable=True
        )
    )
    updated_at:Optional[datetime] = Field(
        default=None,
        #sa_column_kwargs={"onupdate": datetime.now(tz=timezone.utc)}
        sa_column=Column(
            DateTime(timezone=True), onupdate=func.now(), nullable=True
        )
    )
