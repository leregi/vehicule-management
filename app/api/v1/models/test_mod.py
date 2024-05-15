from sqlmodel import Field, SQLModel
from datetime import datetime
from typing import Optional

class People(SQLModel, table=True):
    id: int = Field(primary_key=True,nullable=False)
    fullname:str
    email:str = Field(unique=True)
    created_at:Optional[datetime] = Field(default_factory=datetime.UTC)
    updated_at:Optional[datetime] = Field(default_factory=datetime.UTC,
                                          sa_column_kwargs={"onupdate": datetime.UTC}
                                          )

