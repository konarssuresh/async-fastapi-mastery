import asyncio

async def task(name,delay):
    try:
        print(f"Starting {name}")
        await asyncio.sleep(delay)
        print(f"Finished {name}")
        
        return f"{name} result"
    except asyncio.CancelledError:
        print(f"{name} was cancelled")
        raise
    
    
async def main():
    task_a = asyncio.create_task(task("A",5))
    await asyncio.sleep(2)
    print("Cancelling A...")
    task_a.cancel()
    
    try:
        await task_a
    except asyncio.CancelledError:
        print("A cancellation reached main")
        
        
        
asyncio.run(main())