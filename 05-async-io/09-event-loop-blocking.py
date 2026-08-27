import asyncio
import time 


def blocking_work():
    print("Blocking work started")
    time.sleep(3)
    print("Blocking work finished")
    
async def worker(name):
    print(f"{name} started")

    await asyncio.sleep(1)

    print(f"{name} finished")
    
    
async def main():
    start = time.time()
    
    task_a = asyncio.create_task(worker("A"))
    task_b = asyncio.create_task(worker("B"))
    
    # blocking_work()
    blocker = asyncio.create_task(asyncio.to_thread(blocking_work))
    
    task_c = asyncio.create_task(worker("C"))
    
    await asyncio.gather(task_a,task_b,blocker, task_c)
    
    print(f"time taken {time.time()-start:.2f}")
    
    
asyncio.run(main())