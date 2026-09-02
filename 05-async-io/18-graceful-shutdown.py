import asyncio

async def worker(name,queue):
    try:
        while True:
            job = await queue.get()
            if job is None:
                queue.task_done()
                print(f"{name} shutting down")
                break
            
            try:
                print(f"{name}: processing {job}")
                await asyncio.sleep(1)
                print(f"{name} : finished {job}")
            finally:
                queue.task_done()
            
    except asyncio.CancelledError:
        print(f"{name}: cancelled")
        raise
    
async def main():
    queue = asyncio.Queue()
    
    workers = [
        asyncio.create_task(worker("worker-1",queue)),
        asyncio.create_task(worker("worker-2",queue))
    ]
    
    for i in range(1,7):
        await queue.put(f"Job-{i}")
    
    print("All jobs added")
    
    # wait for all jobs to be processed
    await queue.join()
    
    await queue.put(None)
    await queue.put(None)
    
    await asyncio.gather(*workers)
    
    print("Service shutdown complete")
    
    
asyncio.run(main())