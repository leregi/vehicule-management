from sqlmodel import Field, SQLModel, Relationship
from datetime import datetime, timezone
from typing import Optional,List, Callable
from sqlalchemy import func, Column, DateTime

class Employee(SQLModel, table=True):
    pass
