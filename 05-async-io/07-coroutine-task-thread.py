import asyncio
import threading
import time 


async def async_work():
    print(f"async_work running on {threading.current_thread().name}")
    await asyncio.sleep(1)
    print(f'async_work finished on thread: {threading.current_thread().name}')
    
def blocking_work():
    print(f"blocking_work running on {threading.current_thread().name}")
    time.sleep(2)
    print(f"blocking_work finished on {threading.current_thread().name}")
    
async def main():
    print(f"main running on thread {threading.current_thread().name}")
    task = asyncio.create_task(async_work())
    
    thread_task = asyncio.create_task(asyncio.to_thread(blocking_work))
    
    await asyncio.gather(task,thread_task)
    
asyncio.run(main())