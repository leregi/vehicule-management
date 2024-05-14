from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.orm import sessionmaker
from sqlmodel.ext.asyncio import AsyncSession

from ..core.settings import settings

async_engine = create_async_engine(
    f"postgresql+asyncpg://{settings.POSTGRES_USER}:{settings.POSTGRES_PASSWORD}@{settings.DATABASE_HOST}:{settings.POSTGRES_PORT}/{settings.POSTGRES_DB}",
    echo=True,
    future=True
)

