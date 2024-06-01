from typing import Union
from fastapi import FastAPI, HTTPException,status
from contextlib import asynccontextmanager

from .basic_response import BasicResponse
from .api.v1.core.settings import settings
from .api.v1.routers import router as v1_router
from .api.v1.db.connection import drop_db, init_db

@asynccontextmanager
async def lifespan(app:FastAPI):
    #on startup
    await init_db()
    yield
    print("SHUTDOWN")
    #on shutdown
    #await drop_db()


app = FastAPI(
    title= settings.project_title,
    description=settings.project_description,
    version=settings.project_version,
    lifespan=lifespan
)



@app.get("/", 
status_code=status.HTTP_202_ACCEPTED,
response_model=BasicResponse
)
def read_root():
    return BasicResponse(message="Home")


#app.include_router(v1_router, prefix=settings.API_V1_STR)

