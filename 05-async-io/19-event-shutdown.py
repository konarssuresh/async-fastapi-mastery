import asyncio


async def worker(name,queue,shutdown_event):
    try:
        while True:
            if shutdown_event.is_set() and queue.empty():
                print(f"{name}: shutting down")
                break
            try:
                job = await asyncio.wait_for(
                    queue.get(),
                    timeout=0.5
                )
            except asyncio.TimeoutError:
                continue
            
            try:
                print(f"{name}: processing {job}")
                await asyncio.sleep(1)
                print(f"{name}: finished {job}")
            finally:
                queue.task_done()
            
    except asyncio.CancelledError:
        print(f"{name}: cancelled")
        raise
    
    
async def main():
    queue = asyncio.Queue()
    shutdown_event = asyncio.Event()
    
    workers = [
        asyncio.create_task(
            worker("Worker-1", queue, shutdown_event)
        ),
        asyncio.create_task(
            worker("Worket-2",queue, shutdown_event)
        )
    ]
    
    for i in range(1,7):
        await queue.put(f"Job-{i}")
    
    print("All jobs added")
    
    await asyncio.sleep(2)
    
    print("Shutdown requested")
    
    shutdown_event.set()
    
    await queue.join()
    
    await asyncio.gather(*workers)
    
    print("Shutdown complete")
    
asyncio.run(main())