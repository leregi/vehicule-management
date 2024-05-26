from sqlmodel import Field, SQLModel, Relationship
from datetime import datetime, timezone
from typing import Optional,List, Callable
from sqlalchemy import func, Column, DateTime
from decimal import Decimal

from .trip import Trip as Trip

class EndTripPoint(SQLModel,table=True):
    id:Optional[int] = Field(default=None,primary_key=True)
    latitude:Decimal = Field(default=0, max_digits=8, decimal_places=6)
    longitude:Decimal= Field(default=0, max_digits=9, decimal_places=6)
    trip_id:Optional[int] = Field(default=None,foreign_key="trip.id", unique=True)
    trip_end_point: Optional[Trip] = Relationship(back_populates="end_trip_point", sa_relationship_kwargs={'lazy': 'selectin'})
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

