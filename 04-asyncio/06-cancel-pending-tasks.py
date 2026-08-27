import asyncio


async def task(name, delay):
    try:
        print(f"Starting {name}")
        await asyncio.sleep(delay)
        print(f"Finished {name}")
        return f"{name} result"

    except asyncio.CancelledError:
        print(f"{name} was cancelled")
        raise
    
    
async def main():
    tasks={
        asyncio.create_task(task("A",5)),
        asyncio.create_task(task("B",2)),
        asyncio.create_task(task("C",4))
    }
    
    done, pending = await asyncio.wait(tasks,timeout=3)
    
    print(f"Done :- {len(done)}")
    print(f"pending :- {len(pending)}")
    
    for currenttask in pending:
        currenttask.cancel()
        
    result = await asyncio.gather(*pending, return_exceptions=True)
    
    print(result)
    
    
asyncio.run(main())