from sqlmodel import SQLModel

class BasicResponse(SQLModel):
    message: str
