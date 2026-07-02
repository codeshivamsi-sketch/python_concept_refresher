# instead of creating AsyncSession(engine) everytime, 
# sessionmaker creates a resusable session factory
import asyncio
from sqlalchemy import select
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from model import User, Base

engine = create_async_engine("sqlite+aiosqlite:///test.db")

#create session factory
AsyncSessionLocal = async_sessionmaker(engine, expire_on_commit=False)
# expire_on_commit=False keeps object accesible after commit without re-querying

# use it
async def get_users():
    async with AsyncSessionLocal() as session:
        result = await session.execute(select(User))
        users = result.scalars().all()
        for u in users:
            print(u)

async def main():
    await get_users()


asyncio.run(main())


