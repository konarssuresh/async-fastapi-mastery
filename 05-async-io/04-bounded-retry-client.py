import asyncio
import httpx
import time 


async def fetch_with_retry(client,semaphore,url,retries=3):
    for attempt in range(1,retries+1):
        try:
            async with semaphore:
                print(f"Starting {url} - attempt {attempt}")
                response = await client.get(url)
                response.raise_for_status()
                
                print(f"Finished {url} - {response.status_code}")
                return response.status_code
        except httpx.TimeoutException:
            print(f"timeout - {url} - Attempt no -{attempt} ")
            
        except httpx.HTTPStatusError as e:
            status = e.response.status_code
            print(f"Httpx status error {status} attempt - {attempt}")
            if status not in {500,502,503,504}:
                return None
        if attempt < retries:
            delay = 2**(attempt-1)
            print(f"retrying {url} in {delay} seconds")
            await asyncio.sleep(delay)
    print("Failed url - {url}")
    
    return None

async def main():
    urls = [
        'https://httpbin.org/delay/2',
        'https://httpbin.org/delay/2',
        'https://httpbin.org/delay/2',
        'https://httpbin.org/delay/2',
        'https://httpbin.org/delay/2',
        'https://httpbin.org/delay/2',
    ]
    
    semaphore = asyncio.Semaphore(2)
    
    start = time.time()
    async with httpx.AsyncClient(timeout=1.0) as client:
        results = await asyncio.gather(*[fetch_with_retry(client,semaphore,url) for url in urls])
        
    print(f"results - {results}")
    print(
        f"Total time: "
        f"{time.time() - start:.2f} seconds"
    )
    
asyncio.run(main())