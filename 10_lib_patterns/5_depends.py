from fastapi import FastAPI, Depends
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine
from sqlalchemy import select
from model import User

engine = create_async_engine("sqlite+aiosqlite:///test.db")
AsyncSessionLocal = async_sessionmaker(engine, expire_on_commit=False)

app = FastAPI()

# Dependecy
async def get_db():
    async with AsyncSessionLocal() as session:
        yield session


@app.get("/users")
async def get_users(session: AsyncSession=Depends(get_db)):
    result = await session.execute(select(User))
    users = result.scalars().all()
    return [{"name": u.name, "age": u.age} for u in users]


# start server and hit http://127.0.0.1:8000/users