import asyncio

class NumberIterators:
    def __init__(self,max_number):
        self.current=0
        self.max_number = max_number
        
        
    def __aiter__(self):
        return self
    
    async def __anext__(self):
        if self.current>=self.max_number:
            raise StopAsyncIteration
        await asyncio.sleep(1)
        value = self.current
        self.current+=1
        return value
    
    
async def main():
    async for number in NumberIterators(5):
        print(f"received {number}")
        
asyncio.run(main())