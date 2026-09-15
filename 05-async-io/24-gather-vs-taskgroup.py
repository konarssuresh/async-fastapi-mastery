import asyncio


async def worker(name,delay):
    try:
        print(f"{name}: started")
        await asyncio.sleep(delay)
        
        if name == "worker-2":
            raise ValueError("Worker-2 failed!")
        print(f"{name} finished")
        return f"{name} result"
    except asyncio.CancelledError:
        print(f"{name}: cancelled")
        raise
    
    
async def main():
    try:
        
        tasks = [asyncio.create_task(worker("worker-1",2)),asyncio.create_task(worker("worker-2",1)),asyncio.create_task(worker("worker-3",3))]
        results = await asyncio.gather(
            *tasks
        )
        
        print(results)
        
    except ValueError as exc:
        print(f"Caught error: {exc}")
        await asyncio.sleep(3)
        print(f"Main finished")
        
        
asyncio.run(main())