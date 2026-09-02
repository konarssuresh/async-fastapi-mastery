import asyncio


async def worker(name, queue):
    try:
        while True:
            job = await queue.get()

            try:
                print(f"{name}: processing {job}")

                # Simulate work
                await asyncio.sleep(2)

                print(f"{name}: finished {job}")

            finally:
                queue.task_done()

    except asyncio.CancelledError:
        print(f"{name}: cancellation received")
        raise

    finally:
        print(f"{name}: cleanup")
        
        
async def main():
    queue = asyncio.Queue()

    workers = [
        asyncio.create_task(worker("Worker-1", queue)),
        asyncio.create_task(worker("Worker-2", queue)),
    ]

    # Add jobs
    for i in range(1, 7):
        await queue.put(f"Job-{i}")

    print("All jobs added")

    # Let workers process for a little while
    await asyncio.sleep(1)

    print("Shutdown requested")
    
    try:
        # Give workers 3 seconds to finish everything
        await asyncio.wait_for(
            queue.join(),
            timeout=3,
        )

        print("All jobs completed gracefully")

    except asyncio.TimeoutError:
        print("Graceful shutdown timed out")

        # Force cancellation
        for task in workers:
            task.cancel()

        await asyncio.gather(*workers, return_exceptions=True)

        print("Workers cancelled")
        
    else:
        # Queue completely drained.
        # Now stop workers waiting on queue.get().
        for _ in workers:
            await queue.put(None)

        await asyncio.gather(*workers)

        print("Service shutdown complete")
        
asyncio.run(main())