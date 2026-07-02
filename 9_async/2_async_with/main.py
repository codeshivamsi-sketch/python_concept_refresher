import asyncio
import aiofiles

async def main():
    async with aiofiles.open("notes.txt") as f:
        content = await f.read()
        print(content)

    
asyncio.run(main())