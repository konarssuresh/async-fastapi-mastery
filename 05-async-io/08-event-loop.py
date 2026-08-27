import asyncio
import time

async def worker(name, delay):
    print(f"{time.time():.2f} - {name}: started")
    await asyncio.sleep(delay)
    print(f"{time.time():.2f} - {name}: resumed")
    await asyncio.sleep(delay)
    print(f"{time.time():.2f} - {name}: finished")
    
async def main():
    print(f"{time.time():.2f} - main started")
    
    task_a = asyncio.create_task(worker("A",1))
    task_b = asyncio.create_task(worker("B",2))
    task_c = asyncio.create_task(worker("C",3))
    
    print(f"{time.time():.2f} - Tasks created")
    
    await asyncio.gather(task_a,task_b,task_c)
    
    print(f"{time.time():.2f} - Main finished")
    
asyncio.run(main())