# Maps python classes to database tables - no raw SQL needed
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy import select
import asyncio
from model import Base, User




# Create engine and session, creates connection to the DB.
# Use sqlite+aiosqlite  with async support
engine = create_async_engine("sqlite+aiosqlite:///test.db")

async def main():
    # Create tables
    # Open connection and strat Tx.
    # engine.begin() is an async context manager, conn closes automatically when block ends.
    async with engine.begin() as conn:
        # Create all tables defined in models (User etc) in DB.
        # run_sync is needed cz create_all is not async 
        await conn.run_sync(Base.metadata.create_all)


    # Insert
    # Open new database session - to insert/query.
    async with AsyncSession(engine) as session:
        user = User(name="Shivam", age=32)  # Creates a user object
        session.add(user)                   # Add it to session (staging)
        await session.commit()              # Write/commit it to the DB

    # Query
    async with AsyncSession(engine) as session:
        result = await session.execute(select(User)) # Run select * from users
        # SQLalchemy by default returns Row object. scalars() unwraps it to give us the actual User object
        # all() returns them as a list.
        users = result.scalars().all()               
        for u in users:                     
            print(u.name, u.age)


asyncio.run(main())
