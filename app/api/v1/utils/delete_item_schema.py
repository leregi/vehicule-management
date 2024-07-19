from pydantic import BaseModel

class DeleteItem(BaseModel):
    id:int
    content:str