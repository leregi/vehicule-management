from sqlmodel import Field, SQLModel, Relationship
from datetime import datetime, timezone
from typing import Optional,List, Callable
from sqlalchemy import func, Column, DateTime
from sqlalchemy.dialects.postgresql import TEXT

from .employee import Employee as Employee
from .additional_passenger import AdditionalPassenger as AdditionalPassenger
from .request_trip_point import RequestTripPoint as RequestTripPoint
from .trip import Trip as Trip


class Request(SQLModel, table=True):
    id:Optional[int] = Field(default=None,primary_key=True)
    is_requester_messenger: Optional[bool] =  Field(default=None)
    trip_date:datetime
    trip_title: str
    trip_description:str = Field(sa_column=Column(TEXT))
    start_hour:datetime
    arrival_hour:datetime
    status:str
    non_approval_reason: str = Field(sa_column=Column(TEXT))
    #employee_id: Optional[int] = Field(default=None,foreign_key="employee.id")
    #employee:Optional[Employee] = Relationship(back_populates="requests",sa_relationship_kwargs={'lazy': 'selectin'})
    employees:List[Employee] = Relationship(back_populates="requests",sa_relationship_kwargs={'lazy': 'selectin'}, link_model=AdditionalPassenger)
    request_trip_points:list[RequestTripPoint] = Relationship(back_populates="request",sa_relationship_kwargs={'lazy': 'selectin'})
    trips:List[Trip] = Relationship(back_populates="request",sa_relationship_kwargs={'lazy': 'selectin'})
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
