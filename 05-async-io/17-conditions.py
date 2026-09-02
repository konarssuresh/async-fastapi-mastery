import asyncio

items = []

async def consumer(condition):
    print("Consumer waiting for an item")
    async with condition:
        while not items:
            await condition.wait()
            
        item = items.pop()
        print(f"Consumer: consumed {item}")
        
async def producer(condition):
    await asyncio.sleep(3)
    async with condition:
        items.append("Item A")
        items.append("item B")
        items.append("Item C")
        print("Producer: added item A")
        condition.notify_all()
        
        
async def main():
    condition = asyncio.Condition()
    tasks = [asyncio.create_task(consumer(condition)),asyncio.create_task(consumer(condition)),asyncio.create_task(consumer(condition)),asyncio.create_task(producer(condition))]
    
    await asyncio.gather(*tasks)
    
    print("Main finished")
    
    
asyncio.run(main())
    
    
    