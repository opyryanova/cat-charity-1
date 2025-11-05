from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import declarative_base, sessionmaker


DATABASE_URL = 'sqlite+aiosqlite:///./fastapi.db'

engine = create_async_engine(DATABASE_URL)
async_session_maker = sessionmaker(
    engine,
    class_=AsyncSession,
    expire_on_commit=False,
)

Base = declarative_base()


async def get_async_session():
    async with async_session_maker() as session:
        yield session


SYNC_DATABASE_URL = DATABASE_URL.replace('+aiosqlite', '')
