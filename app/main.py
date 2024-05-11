from typing import Union
from fastapi import FastAPI, HTTPException,status

from .api.v1.core.settings import settings
from .basic_response import BasicResponse
from .api.v1.routers import router as v1_router

app = FastAPI(
    title= settings.project_title,
    description=settings.project_description,
    version=settings.project_version
)


@app.get("/", 
status_code=status.HTTP_202_ACCEPTED,
response_model=BasicResponse
)
def read_root():
    return BasicResponse(message="Home")


app.include_router(v1_router, prefix=settings.API_V1_STR)

