# from sqlmodel import Field, SQLModel, Relationship
# from datetime import datetime, timezone, timedelta
# from typing import Optional,List, Callable
# from sqlalchemy import func, Column, DateTime
# from decimal import Decimal
# from sqlalchemy.dialects.postgresql import TEXT
# from sqlalchemy import Column

# from .trip import Trip as Trip
# from .vehicule import Trip as Trip
# from .employee import Employee as Employee
# from .department import Employee , Trip 

# class TripRating(SQLModel,table=True):
#     id:Optional[int] = Field(default=None, primary_key=True)
#     rating:int
#     testimony:str = Field(sa_column=Column(TEXT))
#     employee_id: Optional[int] = Field(default=None,foreign_key="employee.id")
#     employee:Optional[Employee] = Relationship(back_populates="trip_ratings",sa_relationship_kwargs={'lazy': 'selectin'})
#     trip_id: Optional[int] = Field(default=None,foreign_key="trip.id")
#     trip:Optional[Trip] = Relationship(back_populates="trip_ratings",sa_relationship_kwargs={'lazy': 'selectin'})
#     created_at:datetime = Field(
#         #default_factory=datetime.now(tz=timezone.utc)
#          sa_column=Column(
#             DateTime(timezone=True), server_default=func.now(), nullable=True
#         )
#     )
#     updated_at:Optional[datetime] = Field(
#         default=None,
#         #sa_column_kwargs={"onupdate": datetime.now(tz=timezone.utc)}
#         sa_column=Column(
#             DateTime(timezone=True), onupdate=func.now(), nullable=True
#         )
#     )
