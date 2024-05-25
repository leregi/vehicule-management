from sqlmodel import Field, SQLModel, Relationship
from datetime import datetime, timezone
from typing import Optional,List, Callable
from sqlalchemy import func, Column, DateTime
from decimal import Decimal

from .request import Request

class RequestTripPoint(SQLModel,table=True):
    id:Optional[int] = Field(default=None,primary_key=True)
    point_type: str
    latitude:Decimal = Field(default=0, max_digits=8, decimal_places=6)
    longitude:Decimal= Field(default=0, max_digits=9, decimal_places=6)
    request_id: Optional[int] = Field(default=None,foreign_key="request.id")
    request:Optional[Request] = Relationship(back_populates="request_trip_points",sa_relationship_kwargs={'lazy': 'selectin'})
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

