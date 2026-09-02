import asyncio

counter = 0

async def increment(name,lock):
    global counter
    
    for _ in range(1000):
        async with lock:
            current = counter
            await asyncio.sleep(0)
            counter = current + 1
    print(f"{name} finished")
    
async def main():
    lock = asyncio.Lock()
    await asyncio.gather(
        increment("A",lock),
        increment("B",lock),
        increment("C",lock)
    )
    
    print(f"Final counter = {counter}")
    
    
asyncio.run(main())