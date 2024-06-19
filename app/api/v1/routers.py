from fastapi import APIRouter
from .controllers.vehicule import  vehicule_router

router = APIRouter()


router.include_router(vehicule_router,prefix="/vehicules",tags=["Vehicules"])
