import asyncio
import time

def cpu_work(name):
    print(f"{name}: CPU work started")
    total = 0 
    
    for i in range(300_000_000):
        total += i 
        
    print(f"{name} : CPU work finished")
    
    return total

async def small_task(name):
    print(f"{name} started")
    await asyncio.sleep(1)
    print(f"{name} finished")
    
    
async def main():
    start = time.time()
    task = asyncio.create_task(small_task("Async taks"))
    
    # cpu_work("CPU task")
    blocker = asyncio.create_task(asyncio.to_thread(cpu_work,"CPU Task"))
    
    await asyncio.gather(task,blocker)
    
    print(
        f"Total time: "
        f"{time.time() - start:.2f} seconds"
    )
    
asyncio.run(main())