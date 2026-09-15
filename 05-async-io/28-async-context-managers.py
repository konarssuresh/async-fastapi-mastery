import asyncio
from contextlib import asynccontextmanager


@asynccontextmanager
async def database_connection():
    print("Opening database connection")
    await asyncio.sleep(1)
    
    try:
        yield "DB connection"
    finally:
        print("closing database connection")
        await asyncio.sleep(1)
        
        
async def main():
    async with database_connection() as connection:
        print(f"using connection - {connection}")
        # await asyncio.sleep(2)
        raise ValueError("Something went wrong!")
        
asyncio.run(main())
        
        
        
        