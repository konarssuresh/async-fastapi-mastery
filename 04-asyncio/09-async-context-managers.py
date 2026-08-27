import asyncio

class AsyncResource:
    async def __aenter__(self):
        print("Connecting to resource.....")
        await asyncio.sleep(1)
        print("Connected!")
        return self
    
    async def __aexit__(self,exc_type,exc_value,traceback):
        print(f"Exception type: {exc_type}")
        print(f"Exception value: {exc_value}")
        print(f"traceback {traceback}")
        print("Closing resource....")
        await asyncio.sleep(1)
        print("Resource closed!")
        return True
        
async def main():
    
    async with AsyncResource() as resource:
        print("Using resource...")
        raise ValueError("Something went wrong")
        
        await asyncio.sleep(2)
        
asyncio.run(main())