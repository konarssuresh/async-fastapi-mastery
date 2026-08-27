import asyncio
import time 


def blocking_task(name):
    print(f"Starting blocking task {name}")
    time.sleep(3)
    print(f"Finished blocking task {name}")
    
async def async_task(name):
    print(f"Starting async {name}")
    await asyncio.sleep(3)
    print(f"Finished async {name}")
    
    
async def main():
    start = time.time()
    
    task1 = asyncio.create_task(asyncio.to_thread(blocking_task,"A"))
    task2 = asyncio.create_task(async_task("B"))
    
    await asyncio.gather(task1,task2)
    
    end = time.time()
    
    print(f"Total time {end-start:.2f} seconds")
    
asyncio.run(main())