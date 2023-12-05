from sqlalchemy.ext.asyncio import (
    create_async_engine, AsyncSession, async_sessionmaker
)

import settings

# create async engine for interaction with database
engine = create_async_engine(settings.DATABASE_URL, echo=True)

# create session for the interaction with database
async_session = async_sessionmaker(engine, expire_on_commit=False)


async def get_db():
    try:
        session: AsyncSession = async_session()
        yield session
    finally:
        await session.close()
