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
        async with asyncio.TaskGroup() as group:
            task1 = group.create_task(worker("worker-1",2))
            task2 = group.create_task(worker("worker-2",1))
            task3 = group.create_task(worker("worker-3",3))
            print("All tasks created")
        
        print("All tasks completed")
        print(task1.result())
        print(task2.result())
        print(task3.result())
    except* ValueError as exc:
        print("Caught value error from taskgroup")
        print(exc)
    
    
asyncio.run(main())