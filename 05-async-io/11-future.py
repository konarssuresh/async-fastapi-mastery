import asyncio

async def main():
    loop = asyncio.get_running_loop()
    future = loop.create_future()
    
    print(f"Future done? {future.done()}")
    
    async def complete_future():
        print("waiting before complete future ...")
        await asyncio.sleep(2)
        # future.set_result("future completed")
        future.set_exception(
            ValueError("Something went wrong")
        )
        
    asyncio.create_task(complete_future())
    
    print("Waiting for future result ...")
    
    result = await future
    
    print(f"Result =- {result}")
    print(f"Future done -  {future.done()}")
    
asyncio.run(main())