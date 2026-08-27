import asyncio
import httpx
import time 

async def fetch(client,url):
    # try:
        print(f"fetching url - {url}")
        response = await client.get(url)
        print(f"Finished {url} - {response.status_code}")
        response.raise_for_status()
        return response.status_code
    # except httpx.ReadTimeout:
    #     print(f"Timeout while fetching url - {url}")
    #     return None
    
    
# async def main():
#     start = time.time()
#     async with httpx.AsyncClient(timeout=1.0) as client:
#         results = await asyncio.gather( fetch(client,"https://httpbin.org/delay/2"),
#                             fetch(client,"https://httpbin.org/delay/2"),
#                             fetch(client,"https://httpbin.org/delay/2"),
#                             return_exceptions=True)
#     print(f"Results ; {results}")
#     end= time.time()
    
#     print(f"Total time {end-start:.2f} seconds")

async def main():
    start = time.time()
    async with httpx.AsyncClient(timeout=1.0) as client:
        results = await asyncio.gather( fetch(client,"https://httpbin.org/status/200"),
                            fetch(client,"https://httpbin.org/status/404"),
                            fetch(client,"https://httpbin.org/status/500"),
                            fetch(client,"https://httpbin.org/delay/2"),
                            return_exceptions=True)
    print(f"Results ; {results}")
    end= time.time()
    
    print(f"Total time {end-start:.2f} seconds")
    
    
asyncio.run(main())