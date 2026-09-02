import asyncio

async def worker(name,delay):
    print(f"{name} started")
    await asyncio.sleep(delay)
    print(f"{name} finished")
    return f"{name} result"

def task_completed(task):
    print(f"Callback received: {task.result()}")
    
async def main():
    task = asyncio.create_task(
        worker("A",2)
    )
    tasks = [
        asyncio.create_task(worker("A",3)),
        asyncio.create_task(worker("B",1)),
        asyncio.create_task(worker("C",2))
    ]
    
    for task in tasks:
        task.add_done_callback(task_completed)
    
    
    
    print("Task Scheduled")
    
    await asyncio.gather(*tasks)
    
    print("Main finished")
    
asyncio.run(main())