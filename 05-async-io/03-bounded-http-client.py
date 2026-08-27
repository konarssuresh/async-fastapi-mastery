import asyncio
import httpx
import time


async def fetch(client,semaphore,url):
    async with semaphore:
        print(f"Starting {url}")
        response = await client.get(url)
        
        print(f"Finished {url} - {response.status_code}")
        return response.status_code
    
    
async def main():
    urls = [
        "https://httpbin.org/delay/2",
        "https://httpbin.org/delay/2",
        "https://httpbin.org/delay/2",
        "https://httpbin.org/delay/2",
        "https://httpbin.org/delay/2",
        "https://httpbin.org/delay/2",
        "https://httpbin.org/delay/2",
        "https://httpbin.org/delay/2",
        "https://httpbin.org/delay/2",
    ]
    
    semaphore = asyncio.Semaphore(2)
    start = time.time()
    
    async with httpx.AsyncClient() as client:
        results = await asyncio.gather(*[fetch(client,semaphore,url) for url in urls],return_exceptions=True)
        print(f"Results: {results}")
    end = time.time()
    
    print(f"Total time taken {end-start:.2f} seconds")
    
asyncio.run(main())