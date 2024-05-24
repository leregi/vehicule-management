from sqlmodel import Field, SQLModel, Relationship
from datetime import datetime, timezone
from typing import Optional,List, Callable
from sqlalchemy import func, Column, DateTime

class Departement(SQLModel, table=True):
    id:Optional[int] = Field(default=None,primary_key=True)

