import asyncio

async def task1():
    await asyncio.sleep(2)
    print("task 1 done")

async def task2():
    await asyncio.sleep(1)
    print("task 2 done")

async def main():
    # Without create task, run one after another, total 3 seconds.
    await task1()
    await task2()

# asyncio.run(main())


async def main2():
    # With create task, run at same time, 2 seconds total.
    t1 = asyncio.create_task(task1()) 
    t2 = asyncio.create_task(task2())

    await t1
    await t2

asyncio.run(main2())