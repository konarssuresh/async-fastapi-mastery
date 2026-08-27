import time
import asyncio

async def task(name,delay):
    print(f"starting execution for task {name} with delay of {delay} seconds")
    await asyncio.sleep(delay)
    print(f"finished execution for task {name}")
    return f"result {name}"
    
async def main():
    start=time.time()
    task_a = asyncio.create_task(task("A",5))
    task_b = asyncio.create_task(task("B",2))
    task_c = asyncio.create_task(task("C",3))
    res1= await task_a
    res2 = await task_b
    res3 = await task_c
    end=time.time()
    print(f"time taken for execution {end-start:.2f}")
    print(res1,res2,res3)
    

asyncio.run(main())    