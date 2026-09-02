import asyncio
import time 

async def worker(name,delay):
    print(f"{name} started")
    await asyncio.sleep(delay)
    print(f"{name} finished")
    return f"{name} result"

async def main():
    tasks=[
        asyncio.create_task(worker("A",1)),
        asyncio.create_task(worker("B",3)),
        asyncio.create_task(worker("C",5))
    ]
    
    start = time.time()
    
    done,pending = await asyncio.wait(tasks,timeout=2)
    
    print(f"wait finished after {time.time()-start:.2f} seconds")
    
    print(f" Done tasks: {len(done)}")
    print(f"pending tasks: {len(pending)}")
    
    for task in done:
        print(f"Result: {task.result()}")
        
    for task in pending:
        print(f"Still pending {task}")
        task.cancel()
        
    for task in pending:
        try:
            await task
        except asyncio.CancelledError:
            print("pending task cancelled")
        
    print(f"Main finished after {time.time()-start:.2f} seconds")
    
asyncio.run(main())

# wait does not automatically cancel pending tasks 

# If your program simply ends immediately afterward, asyncio.run() will clean up the remaining tasks when the event loop shuts down. 
# But in a real application, you often need to explicitly decide what to do with them.