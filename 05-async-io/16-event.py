import asyncio
import time 

async def worker(name, event):
    print(f"{name}: waiting for event")
    await event.wait()
    print(f"{name}: event received")
    await asyncio.sleep(3)
    print(f"{name} finished")
    
async def main():
    start = time.time()
    event = asyncio.Event()
    
    tasks  = [
        asyncio.create_task(worker("A",event)),
        asyncio.create_task(worker("B",event)),
        asyncio.create_task(worker("C",event))
    ]
    
    print("Workers started")
    
    await asyncio.sleep(3)
    
    print("Main: setting event")
    
    event.set()
    
    await asyncio.gather(*tasks)
    
    print("Main finished")
    print(f"time taken - {time.time()-start:.2f}seconds")
    
    event.clear()
    
    # await worker("D",event)
    asyncio.create_task(worker("D",event))
    
    
asyncio.run(main())