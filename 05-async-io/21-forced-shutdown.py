import asyncio

async def worker():
    try:
        print("worjker started")
        while True:
            print("worker doing work")
            await asyncio.sleep(1)
    except asyncio.CancelledError:
        print("worker: cancellation received")
        raise
    finally:
        print("Worker: cleanup")
        
async def main():
    task = asyncio.create_task(worker())
    await asyncio.sleep(2.5)
    print("Main: forcing shitdown")
    task.cancel()
    
    try:
        await task
    except asyncio.CancelledError:
        print("Main: worker was cancelled")
        
    print("Main: shutdown complete")
    
    
asyncio.run(main())