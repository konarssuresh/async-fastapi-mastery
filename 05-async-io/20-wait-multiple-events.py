import asyncio


async def worker(name, queue, shutdown_event):
    try:
        while True:
            # If shutdown was requested, there is no more work
            # that will be added, so finish whatever is already queued.
            if shutdown_event.is_set() and queue.empty():
                print(f"{name}: shutting down")
                break

            try:
                job = await asyncio.wait_for(
                    queue.get(),
                    timeout=0.5,
                )
            except asyncio.TimeoutError:
                continue

            try:
                print(f"{name}: processing {job}")

                await asyncio.sleep(1)

                print(f"{name}: finished {job}")

            finally:
                queue.task_done()

    except asyncio.CancelledError:
        print(f"{name}: cancelled")
        raise

    finally:
        print(f"{name}: cleanup")


async def main():
    queue = asyncio.Queue()
    shutdown_event = asyncio.Event()

    workers = [
        asyncio.create_task(
            worker("Worker-1", queue, shutdown_event)
        ),
        asyncio.create_task(
            worker("Worker-2", queue, shutdown_event)
        ),
    ]

    # Simulate incoming jobs
    for i in range(1, 7):
        await queue.put(f"Job-{i}")

    print("All jobs added")

    await asyncio.sleep(1.5)

    print("Shutdown requested")

    # Tell workers that no more jobs will arrive
    shutdown_event.set()

    # Wait for all existing jobs to finish
    await queue.join()

    # Workers should now see:
    # shutdown_event = True
    # queue = empty
    # and exit
    await asyncio.gather(*workers)

    print("Service shutdown complete")


asyncio.run(main())