from contextlib import asynccontextmanager
import asyncio

@asynccontextmanager
async def managed_task(name):
    print(f"starting {name}")
    try:
        await asyncio.sleep(1) # Anything before yeild -> __enter__ (setup)
        yield name
        # This will break the code, as asynccontextmanager can yield only once, 
        # Use regular generator for multiple yields
        # Everything after yield is cleanup code
        # yield name + "-1"
    finally:
        print(f"cleaning up {name}") # Anything after yield -> __exit__ (cleanup)


async def main():
    async with managed_task("database") as task:
        print(f"using {task}")


asyncio.run(main())