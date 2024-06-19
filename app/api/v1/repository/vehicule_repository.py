from sqlmodel.ext.asyncio.session import AsyncSession
from ..models.tables import Vehicule
from  sqlmodel import select
from fastapi import HTTPException



class VehiculeRepository():
    @staticmethod
    async def create_vehicule(session:AsyncSession,data:dict):
        vehicule = Vehicule(**data)
        session.add(vehicule)
        await session.commit()
        await session.refresh(vehicule)
        return vehicule
    
    
    """ @staticmethod
    async def get_vehicule(session:AsyncSession):
        get_all_statement = select(Vehicule)
        exec_all = await session.exec(get_all_statement)
        vehicule_all = exec_all.all()
        return vehicule_all
    
 
    
    @staticmethod
    async def get_vehicule_by_id(vehicule_id,session:AsyncSession):
        vehicule = await session.get(Vehicule,vehicule_id)
        if not vehicule:
            raise HTTPException(status_code=404, detail="vehicule not found")
        return vehicule
    

    
    @staticmethod
    async def update_vehicule(data,vehicule_id,session:AsyncSession):
        the_vehicule = await session.get(Vehicule,vehicule_id)
        if not the_vehicule:
            raise HTTPException(status_code=404, detail="vehicule not found")
        for k, v in data.items():
            setattr(the_vehicule,k,v)
        session.add(the_vehicule)
        await session.commit()
        await session.refresh(the_vehicule)
        return the_vehicule
    


    @staticmethod
    async def delete_vehicule(vehicule_id,session:AsyncSession):
        the_vehicule = await session.get(Vehicule,vehicule_id)
        if not the_vehicule:
            raise HTTPException(status_code=404, detail="vehicule not found")
        await session.delete(the_vehicule)
        await session.commit()
        return DeleteItem(
            id = the_vehicule.id,
            content=the_vehicule.fullname
        ) """
    
