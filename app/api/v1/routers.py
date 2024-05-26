from fastapi import APIRouter
from .controllers import test_router

router = APIRouter()


#router.include_router(test_router,prefix="/tests",tags=["Tests"])
