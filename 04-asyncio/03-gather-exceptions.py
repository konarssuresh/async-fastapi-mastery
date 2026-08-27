# import asyncio

# async def task(name,delay,should_fail=False):
#     print(f"Starting {name}")
#     await asyncio.sleep(delay)
#     if should_fail:
#         raise ValueError(f"{name} failed")
#     print(f"Finsihed {name}")
#     return f"{name} result"

# async def main():
#     results = await asyncio.gather(
#         task("A",2),
#         task("B",1,True),
#         task("C",3)
#     )
    
#     print(results)
    
# asyncio.run(main())


# import asyncio

# async def task(name,delay,should_fail=False):
#     print(f"Starting {name}")
#     await asyncio.sleep(delay)
#     if should_fail:
#         raise ValueError(f"{name} failed")
#     print(f"Finsihed {name}")
#     return f"{name} result"

# async def main():
#    tasks= [asyncio.create_task(task("A",2)),
#            asyncio.create_task(task("B",1,True)),
#            asyncio.create_task(task("C",3))]
#    try:
#        results=await asyncio.gather(*tasks)
#        print(results)
#    except ValueError as e:
#        print(f"Caught error: {e}")
    
#    await asyncio.sleep(4)
    
    
    
# asyncio.run(main())



import asyncio

async def task(name,delay,should_fail=False):
    print(f"Starting {name}")
    await asyncio.sleep(delay)
    if should_fail:
        raise ValueError(f"{name} failed")
    print(f"Finsihed {name}")
    return f"{name} result"

async def main():
   tasks= [asyncio.create_task(task("A",2)),
           asyncio.create_task(task("B",1,True)),
           asyncio.create_task(task("C",3))]

   results=await asyncio.gather(*tasks,return_exceptions=True)
   print(results)

    
#    await asyncio.sleep(4)
    
    
    
asyncio.run(main())