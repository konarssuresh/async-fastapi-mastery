import asyncio
import time

semaphore = asyncio.Semaphore(3)

async def task(name,delay):
    async with semaphore:
        print(f"Starting {name}")
        await asyncio.sleep(delay)
        print(f"X {name}")
        
async def main():
    start = time.time()
    
    tasks = [
        asyncio.create_task(task("A",2)),
        asyncio.create_task(task("B",3)),
        asyncio.create_task(task("C",2)),
        asyncio.create_task(task("D",3)),
        asyncio.create_task(task("E",2)),
        # asyncio.create_task(task("F",2)),
        # asyncio.create_task(task("G",2)),
        # asyncio.create_task(task("H",2)),
        # asyncio.create_task(task("I",2)),
        # asyncio.create_task(task("J",2)),
        # asyncio.create_task(task("K",2)),
        # asyncio.create_task(task("L",2))
    ]
    
    await asyncio.gather(*tasks)
    
    end = time.time()
    
    print(f"Total time taken: {end-start:.2f}")
    
    
asyncio.run(main())