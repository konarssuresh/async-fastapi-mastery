import asyncio

async def numbers():
    for i in range(5):
        await asyncio.sleep(1)
        yield i
        
async def background_task():
    for i in range(5):
        await asyncio.sleep(0.5)
        print(f"Background: {i}")
        
        
async def main():
    task = asyncio.create_task(background_task())
    
    async for number in numbers():
        print(f"received {number}")
        
    await task
    
asyncio.run(main())