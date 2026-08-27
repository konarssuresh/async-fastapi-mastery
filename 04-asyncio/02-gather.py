import asyncio
import time 

async def task(name, delay):
    print(f"starting {name}")
    await asyncio.sleep(delay)
    print(f"finished {name}")
    return f"{name} completed"

async def main():
    start = time.time()
    results = await asyncio.gather(
        task("A",5),
        task("B", 2),
        task("C" ,3)
    )
    
    end = time.time()
    print(f"Results: {results}")
    print(f"Total time: {end-start:.2f}")
    

asyncio.run(main())