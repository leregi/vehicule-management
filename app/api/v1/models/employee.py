from sqlmodel import Field, SQLModel, Relationship
from datetime import datetime, timezone
from typing import Optional,List, Callable
from sqlalchemy import func, Column, DateTime

class Employee(SQLModel, table=True):
    id:Optional[int] = Field(default=None,primary_key=True)
    first_name:str
    last_name:str
    telephone:str = Field(unique=True)
    email:str = Field(unique=True)
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
