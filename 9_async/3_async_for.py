import asyncio

async def get_numbers():
    for i in range(5):
        await asyncio.sleep(1)
        yield i


async def main():
    async for num in get_numbers():
        print(num)


asyncio.run(main())



