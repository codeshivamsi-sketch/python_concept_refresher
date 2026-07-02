import asyncio

async def greet():
    print("hello")
    await asyncio.sleep(1)
    print("world")

greet() # Fn doesnt get called, does not, just returns a coroutine object.
asyncio.run(greet()) # Actually runs the function













async def fetch_data():
    print("fetching...")
    await asyncio.sleep(2)
    return {"data": "result"}

async def main():
    result = await fetch_data()
    print(result)

asyncio.run(main())