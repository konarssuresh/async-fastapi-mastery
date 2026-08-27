import asyncio
import time 


async def task(name,delay):
    print(f"Starting {name}")
    await asyncio.sleep(delay)
    print(f"Finished ezxecuting {name}")
    
    return f"{name} result"

async def main():
    tasks = [
        asyncio.create_task(task("A",3)),
        asyncio.create_task(task("B",1)),
        asyncio.create_task(task("C",2))
    ]
    
    start = time.time()
    
    for completed_task in asyncio.as_completed(tasks):
        print(completed_task)
        result = await completed_task
        
        print(f"Got result : {result}")

    print(f"total time - {time.time()-start:.2f}")
    
asyncio.run(main())