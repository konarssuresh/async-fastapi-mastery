import asyncio
import time

async def task(name,delay):
    print(f"Starting {name}")
    await asyncio.sleep(delay)
    print(f"Finished {name}")
    
    return f"{name} result"

async def main():
    start = time.time()
    
    tasks = {
        asyncio.create_task(task("A",5)),
        asyncio.create_task(task("B",2)),
        asyncio.create_task(task("C",3))
    }
    
    done,pending = await asyncio.wait(tasks)
    
    end = time.time()
    
    print(f"Done: {done}")
    print(f"Pending: {pending}")
    print(f"Time: {end-start:.2f}")
    
asyncio.run(main())