import asyncio

async def main():
    print("hello")
    await asyncio.sleep(1)
    print("world")

asyncio.run(main()) # starts event loop, runs main, shut down


# Rules
# 1. Call it only once, at top level of your script
# 2. Never call it inside another async function - use await there instead