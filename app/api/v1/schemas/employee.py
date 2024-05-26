from sqlmodel import SQLModel
from pydantic import EmailStr, ConfigDict
from typing import List, Optional

#from .request import RequestBase
#from .department import DepartmentBase
#from .trip_rating import TripRatingsBase

class EmployeeBase(SQLModel):
    model_config = ConfigDict(from_attributes=True)
    first_name:str
    last_name:str
    telephone:str 
    email:EmailStr


class EmployeeCompleteSchema(EmployeeBase):
    #requests:List[RequestBase]
    #departement:Optional[DepartmentBase]
    #Trip_ratings:List[TripRatings]
    pass
