import asyncio
import time 

async def slow_operation():
    print("Slow operation started")
    await asyncio.sleep(5)
    print("Slow operation")
    
async def main():
    start = time.time()
    
    try:
        async with asyncio.timeout(4):
            print("Operation 1")
            await asyncio.sleep(1)

            print("Operation 2")
            await asyncio.sleep(1)

            print("Operation 3")
            await asyncio.sleep(5)
            
            print("All operations completed")

    except TimeoutError:
        raise
    
    finally:
        print("cleanup is running ")
    print(f"total time {time.time()-start:.2f} seconds")
    
asyncio.run(main())