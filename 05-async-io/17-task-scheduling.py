import asyncio

async def worker():
    print("worker started")
    await asyncio.sleep(1)
    print("worker finished")
    
async def main():
    print("before create task")
    task = asyncio.create_task(worker())
    print("After create task")
    
    await asyncio.sleep(0)
    
    print(f"Main: after sleep(0)")
    await task
    print("Main: finished")
    
asyncio.run(main())