from sqlmodel import Field, SQLModel, Relationship
from datetime import datetime, timezone
from typing import Optional,List, Callable
from sqlalchemy import func, Column, DateTime

from .department import Departement
from .request import Request
from .additional_passenger import AdditionalPassenger

class Employee(SQLModel, table=True):
    id:Optional[int] = Field(default=None,primary_key=True)
    first_name:str
    last_name:str
    telephone:str = Field(unique=True)
    email:str = Field(unique=True)
    department_id: Optional[int] = Field(default=None,foreign_key="departement.id")
    department:Optional[Departement] = Relationship(back_populates="employees",sa_relationship_kwargs={'lazy': 'selectin'})
    #requests:List[Request] = Relationship(back_populates="employee",sa_relationship_kwargs={'lazy': 'selectin'})
    requests:List[Request] = Relationship(back_populates="employees",sa_relationship_kwargs={'lazy': 'selectin'}, link_model=AdditionalPassenger)
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
    