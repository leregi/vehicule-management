from sqlmodel import Field, SQLModel, Relationship
from datetime import datetime, timezone
from typing import Optional,List, Callable
from sqlalchemy import func, Column, DateTime

from .trip import Trip as Trip

class Vehicule(SQLModel,table=True):
    id:Optional[int] = Field(default=None,primary_key=True)
    mark: str
    model:str
    creation_year: int
    vin_number:str = Field(unique=True)
    number_cylinder:int
    insurance_exp_date:datetime
    vignette_exp_date:datetime
    immatriculation_number:str = Field(unique=True)
    trips:List[Trip] = Relationship(back_populates="vehicule",sa_relationship_kwargs={'lazy': 'selectin'})
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
