from sqlmodel.ext.asyncio.session import AsyncSession
from ..models.tables import Vehicule
from  sqlmodel import select
from fastapi import HTTPException
from ..utils.delete_item_schema import DeleteItem
from icecream import ic


class VehiculeRepository:
    @staticmethod
    async def create_vehicule(session: AsyncSession, data: dict):
        try:
            vehicule = Vehicule(**data)
            session.add(vehicule)
            await session.commit()
            await session.refresh(vehicule)
            return vehicule
        except Exception as e:
            ic(e)
            await session.rollback()
            raise HTTPException(status_code=500, detail="Error creating vehicule")

    @staticmethod
    async def get_vehicule(session: AsyncSession):
        try:
            get_all_statement = select(Vehicule)
            exec_all = await session.exec(get_all_statement)
            vehicule_all = exec_all.all()
            return vehicule_all
        except Exception as e:
            ic(e)
            raise HTTPException(status_code=500, detail="Error fetching vehicules")

    @staticmethod
    async def get_vehicule_by_id(vehicule_id: int, session: AsyncSession):
        try:
            vehicule = await session.get(Vehicule, vehicule_id)
            if not vehicule:
                raise HTTPException(status_code=404, detail="Vehicule not found")
            return vehicule
        except HTTPException as e:
            raise e
        except Exception as e:
            ic(e)
            raise HTTPException(status_code=500, detail="Error fetching vehicule by ID")

    @staticmethod
    async def update_vehicule(data: dict, vehicule_id: int, session: AsyncSession):
        try:
            the_vehicule = await session.get(Vehicule, vehicule_id)
            if not the_vehicule:
                raise HTTPException(status_code=404, detail="Vehicule not found")
            for k, v in data.items():
                setattr(the_vehicule, k, v)
            session.add(the_vehicule)
            await session.commit()
            await session.refresh(the_vehicule)
            return the_vehicule
        except HTTPException as e:
            raise e
        except Exception as e:
            ic(e)
            await session.rollback()
            raise HTTPException(status_code=500, detail="Error updating vehicule")

    @staticmethod
    async def delete_vehicule(vehicule_id: int, session: AsyncSession):
        try:
            the_vehicule = await session.get(Vehicule, vehicule_id)
            if not the_vehicule:
                raise HTTPException(status_code=404, detail="Vehicule not found")
            await session.delete(the_vehicule)
            await session.commit()
            return DeleteItem(
                id=the_vehicule.id,
                content=the_vehicule.fullname
            )
        except HTTPException as e:
            raise e
        except Exception as e:
            ic(e)
            await session.rollback()
            raise HTTPException(status_code=500, detail="Error deleting vehicule")
        