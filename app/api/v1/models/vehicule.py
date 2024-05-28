# from sqlmodel import Field, SQLModel, Relationship
# from datetime import datetime, timezone
# from typing import Optional,List, Callable
# from sqlalchemy import func, Column, DateTime
# from decimal import Decimal
# from sqlalchemy.dialects.postgresql import INTERVAL
# from sqlalchemy import Column

# from .trip import Trip as Trip
# from .starting_trip_point import StartingTripPoint as StartingTripPoint
# from .end_trip_point import EndTripPoint as EndTripPoint
# from .department import Request as Request
# from .driver import Driver as  Driver
# from .trip_rating import TripRating as TripRating

# class Vehicule(SQLModel,table=True):
#     id:Optional[int] = Field(default=None,primary_key=True)
#     mark: str
#     model:str
#     creation_year: int
#     vin_number:str = Field(unique=True)
#     number_cylinder:int
#     insurance_exp_date:datetime
#     vignette_exp_date:datetime
#     immatriculation_number:str = Field(unique=True)
#     trips:List[Trip] = Relationship(back_populates="vehicule",sa_relationship_kwargs={'lazy': 'selectin'})
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


# class StartingTripPoint(SQLModel,table=True):
#     id:Optional[int] = Field(default=None,primary_key=True)
#     latitude:Decimal = Field(default=0, max_digits=8, decimal_places=6)
#     longitude:Decimal= Field(default=0, max_digits=9, decimal_places=6)
#     trip_id:Optional[int] = Field(default=None,foreign_key="trip.id", unique=True)
#     trip_starting_point: Optional[Trip] = Relationship(back_populates="starting_trip_point", sa_relationship_kwargs={'lazy': 'selectin'})
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


# class EndTripPoint(SQLModel,table=True):
#     id:Optional[int] = Field(default=None,primary_key=True)
#     latitude:Decimal = Field(default=0, max_digits=8, decimal_places=6)
#     longitude:Decimal= Field(default=0, max_digits=9, decimal_places=6)
#     trip_id:Optional[int] = Field(default=None,foreign_key="trip.id", unique=True)
#     trip_end_point: Optional[Trip] = Relationship(back_populates="end_trip_point", sa_relationship_kwargs={'lazy': 'selectin'})
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

    

# class Trip(SQLModel,table=True):
#     id:Optional[int] = Field(default=None,primary_key=True)
#     start_time:datetime 
#     finish_time:Optional[datetime] 
#     start_odometer_km:Decimal 
#     finish_odometer_km:Optional[Decimal] 
#     distance_traveled_km: Optional[Decimal]
#     trip_duration: Optional[timedelta] = Field(sa_column=Column(INTERVAL))
#     status: str
#     vehicule_id: Optional[int] = Field(default=None,foreign_key="vehicule.id")
#     vehicule:Optional[Vehicule] = Relationship(back_populates="trips",sa_relationship_kwargs={'lazy': 'selectin'})
#     request_id: Optional[int] = Field(default=None,foreign_key="request.id")
#     request:Optional[Request] = Relationship(back_populates="trips",sa_relationship_kwargs={'lazy': 'selectin'})
#     driver_id: Optional[int] = Field(default=None,foreign_key="driver.id")
#     driver:Optional[Driver] = Relationship(back_populates="trips",sa_relationship_kwargs={'lazy': 'selectin'})
#     trip_ratings:List[TripRating] = Relationship(back_populates="trip",sa_relationship_kwargs={'lazy': 'selectin'})
#     starting_trip_point:Optional[StartingTripPoint] = Relationship(
#         sa_relationship_kwargs={
#             'uselist': False,
#             'lazy': 'selectin'
#         },
#         back_populates="trip_starting_point"    
#     )
#     end_trip_point:Optional[EndTripPoint] = Relationship(
#         sa_relationship_kwargs={
#             'uselist': False,
#             'lazy': 'selectin'
#         },
#         back_populates="trip_end_point"    
#     )
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