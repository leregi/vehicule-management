from sqlmodel import Field, SQLModel, Relationship
from datetime import datetime, timezone, timedelta
from typing import Optional,List, Callable
from sqlalchemy import func, Column, DateTime
from sqlalchemy.dialects.postgresql import TEXT
from sqlalchemy.dialects.postgresql import INTERVAL
from decimal import Decimal



from .linked_tables import  DriverLicence, AdditionalPassenger

class Departement(SQLModel, table=True):
    id:Optional[int] = Field(default=None,primary_key=True)
    department_name:str = Field(unique=True)
    # Departement has many employee
    employees:List["Employee"] = Relationship(back_populates="departement",sa_relationship_kwargs={'lazy': 'selectin'})
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

class Employee(SQLModel, table=True):
    id:Optional[int] = Field(default=None,primary_key=True)
    first_name:str
    last_name:str
    telephone:str = Field(unique=True)
    email:str = Field(unique=True)
    department_id: Optional[int] = Field(default=None,foreign_key="departement.id")
    department:Optional[Departement] = Relationship(back_populates="employees",sa_relationship_kwargs={'lazy': 'selectin'})
    trip_ratings:List['TripRating'] = Relationship(back_populates="employee",sa_relationship_kwargs={'lazy': 'selectin'})
    requests:List['Request'] = Relationship(back_populates="employees",sa_relationship_kwargs={'lazy': 'selectin'}, link_model=AdditionalPassenger)
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
    request_trip_points:list["RequestTripPoint"] = Relationship(back_populates="request",sa_relationship_kwargs={'lazy': 'selectin'})
    trips:List["Trip"] = Relationship(back_populates="request",sa_relationship_kwargs={'lazy': 'selectin'})
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
    trips:List["Trip"] = Relationship(back_populates="vehicule",sa_relationship_kwargs={'lazy': 'selectin'})
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


class RequestTripPoint(SQLModel,table=True):
    id:Optional[int] = Field(default=None,primary_key=True)
    point_type: str
    latitude:Decimal = Field(default=0, max_digits=8, decimal_places=6)
    longitude:Decimal= Field(default=0, max_digits=9, decimal_places=6)
    request_id: Optional[int] = Field(default=None,foreign_key="request.id")
    request:Optional["Request"] = Relationship(back_populates="request_trip_points",sa_relationship_kwargs={'lazy': 'selectin'})
    
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



class StartingTripPoint(SQLModel,table=True):
    id:Optional[int] = Field(default=None,primary_key=True)
    latitude:Decimal = Field(default=0, max_digits=8, decimal_places=6)
    longitude:Decimal= Field(default=0, max_digits=9, decimal_places=6)
    trip_id:Optional[int] = Field(default=None,foreign_key="trip.id", unique=True)
    trip_starting_point: Optional["Trip"] = Relationship(back_populates="starting_trip_point", sa_relationship_kwargs={'lazy': 'selectin'})
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


class EndTripPoint(SQLModel,table=True):
    id:Optional[int] = Field(default=None,primary_key=True)
    latitude:Decimal = Field(default=0, max_digits=8, decimal_places=6)
    longitude:Decimal= Field(default=0, max_digits=9, decimal_places=6)
    trip_id:Optional[int] = Field(default=None,foreign_key="trip.id", unique=True)
    trip_end_point: Optional["Trip"] = Relationship(back_populates="end_trip_point", sa_relationship_kwargs={'lazy': 'selectin'})
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

    

class Trip(SQLModel,table=True):
    id:Optional[int] = Field(default=None,primary_key=True)
    start_time:datetime 
    finish_time:Optional[datetime] 
    start_odometer_km:Decimal 
    finish_odometer_km:Optional[Decimal] 
    distance_traveled_km: Optional[Decimal]
    trip_duration: Optional[timedelta] = Field(sa_column=Column(INTERVAL))
    status: str
    vehicule_id: Optional[int] = Field(default=None,foreign_key="vehicule.id")
    vehicule:Optional[Vehicule] = Relationship(back_populates="trips",sa_relationship_kwargs={'lazy': 'selectin'})
    request_id: Optional[int] = Field(default=None,foreign_key="request.id")
    request:Optional[Request] = Relationship(back_populates="trips",sa_relationship_kwargs={'lazy': 'selectin'})
    driver_id: Optional[int] = Field(default=None,foreign_key="driver.id")
    driver:Optional["Driver"] = Relationship(back_populates="trips",sa_relationship_kwargs={'lazy': 'selectin'})
    trip_ratings:List["TripRating"] = Relationship(back_populates="trip",sa_relationship_kwargs={'lazy': 'selectin'})
    starting_trip_point:Optional[StartingTripPoint] = Relationship(
        sa_relationship_kwargs={
            'uselist': False,
            'lazy': 'selectin'
        },
        back_populates="trip_starting_point"    
    )
    end_trip_point:Optional[EndTripPoint] = Relationship(
        sa_relationship_kwargs={
            'uselist': False,
            'lazy': 'selectin'
        },
        back_populates="trip_end_point"    
    )
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


class TripRating(SQLModel,table=True):
    id:Optional[int] = Field(default=None, primary_key=True)
    rating:int
    testimony:str = Field(sa_column=Column(TEXT))
    employee_id: Optional[int] = Field(default=None,foreign_key="employee.id")
    employee:Optional[Employee] = Relationship(back_populates="trip_ratings",sa_relationship_kwargs={'lazy': 'selectin'})
    trip_id: Optional[int] = Field(default=None,foreign_key="trip.id")
    trip:Optional[Trip] = Relationship(back_populates="trip_ratings",sa_relationship_kwargs={'lazy': 'selectin'})
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

class Licence(SQLModel,table=True):
    id:Optional[int] = Field(default=None,primary_key=True)
    licence_number: str
    licence_exp_date: datetime
    drivers: List["Driver"] = Relationship(back_populates="licences",sa_relationship_kwargs={'lazy': 'selectin'}, link_model=DriverLicence)
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

class Driver(SQLModel,table=True):
    id:Optional[int] = Field(default=None,primary_key=True)
    firstname:str
    lastname: str
    email:str = Field(unique=True)
    password:str
    telephone:str
    licences: List[Licence] = Relationship(back_populates="drivers",sa_relationship_kwargs={'lazy': 'selectin'}, link_model=DriverLicence)
    trips: List[Trip] = Relationship(back_populates="driver",sa_relationship_kwargs={'lazy': 'selectin'})
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
