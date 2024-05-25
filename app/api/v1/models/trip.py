from sqlmodel import Field, SQLModel, Relationship
from datetime import datetime, timezone, timedelta
from typing import Optional,List, Callable
from sqlalchemy import func, Column, DateTime
from decimal import Decimal

from .vehicule import Vehicule

class Trip(SQLModel,table=True):
    #request_id integer [ref: > Request.id]
    #driver_id integer [ref: > Drivers.id]
    start_time:datetime 
    finish_time:Optional[datetime] 
    start_odometer_km:Decimal 
    finish_odometer_km:Optional[Decimal] 
    distance_traveled_km: Optional[Decimal]
    trip_duration: Optional[timedelta]
    status: str
    vehicule_id: Optional[int] = Field(default=None,foreign_key="vehicule.id")
    vehicule:Optional[Vehicule] = Relationship(back_populates="trips",sa_relationship_kwargs={'lazy': 'selectin'})
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
