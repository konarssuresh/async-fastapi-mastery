import asyncio

async def producer(queue):
    for i in range(15):
        print(f" Producing item {i}, queue size : {queue.qsize()}")
        await queue.put(i)
        print(
            f"Put {i}, "
            f"queue size after put: {queue.qsize()}"
        )
        await asyncio.sleep(0.2)
        
async def consumer(queue, name):
    while True:
        item = await queue.get()
        print(f"Consumer {name} Consuming item {item}")
        await asyncio.sleep(2)
        queue.task_done()
        
        
# async def main():
#     queue = asyncio.Queue()
#     producer_task = asyncio.create_task(producer(queue))
#     consumer_task = asyncio.create_task(consumer(queue))
#     print(f"Main: waiting for producer")
#     await producer_task
#     print("Main: producer finished")
#     await queue.join()
#     print("Main queue completely processed")
#     consumer_task.cancel()
    
#     try:
#         await consumer_task
#     except asyncio.CancelledError:
#         pass
#     print("Main finished")


async def main():
    queue = asyncio.Queue(maxsize=2)
    producer_task = asyncio.create_task(producer(queue))
    consumer_tasks = [asyncio.create_task(consumer(queue,i)) for i in range(2)]
    await producer_task
    await queue.join()
    for task in consumer_tasks:
        task.cancel()
    
    await asyncio.gather(*consumer_tasks, return_exceptions=True)
    print("Main finished")
    
asyncio.run(main())