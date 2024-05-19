from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.orm import sessionmaker
from sqlmodel.ext.asyncio.session import AsyncSession
from sqlmodel import SQLModel

from ..core.settings import settings

async_engine = create_async_engine(
    f"postgresql+asyncpg://{settings.POSTGRES_USER}:{settings.POSTGRES_PASSWORD}@{settings.DATABASE_HOST}:{settings.POSTGRES_PORT}/{settings.POSTGRES_DB}",
    echo=True,
    future=True
)


async def init_db():
    async with async_engine.begin() as postgres_conn:
        await postgres_conn.run_sync(SQLModel.metadata.create_all)

async def drop_db():
    async with async_engine.begin() as postgres_conn:
        await postgres_conn.run_sync(SQLModel.metadata.drop_all)

async def get_async_session()->AsyncSession:
    async_session = sessionmaker(
       bind=async_engine, class_=AsyncSession, expire_on_commit=False
   )
    async with async_session as session:
        yield session

