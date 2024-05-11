from fastapi import APIRouter, HTTPException, status
from typing import Union


test_router = APIRouter()

@test_router.post("/")
async def add_test():
    pass
