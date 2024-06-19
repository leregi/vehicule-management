from sqlmodel import SQLModel
from pydantic import EmailStr, ConfigDict, Field
from typing import List, Optional
from datetime import datetime


class VehiculeBase(SQLModel):
    model_config = ConfigDict(from_attributes=True)
    mark: str
    model:str
    creation_year: int
    vin_number:str = Field(unique=True)
    number_cylinder:int
    insurance_exp_date:datetime
    vignette_exp_date:datetime
    immatriculation_number:str = Field(unique=True)

class CreateVehicule(VehiculeBase):
    pass