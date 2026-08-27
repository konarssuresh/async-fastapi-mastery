import asyncio
import httpx


async def fetch_with_retry(client, url, retries=3):
    for attempt in range(1,retries+1):
        try:
            print(f"Attempt {attempt}: {url}")
            response = await client.get(url)
            response.raise_for_status()
            print(f"Success {url}")
        except httpx.HTTPStatusError as e:
            print(f"Error on attempt {attempt}:{e.response.status_code}")
            status = e.response.status_code
            
            if status not in {500,502,503,504}:
                print("Mpm retryable http error")
                return None
            
            await asyncio.sleep(1*attempt*retries)
        except httpx.TimeoutException:
            print(
                f"Timeout on attempt {attempt}"
            )
            await asyncio.sleep(1*attempt*2)
            
    print(f"Failed after {retries} attempts")
    return None


async def main():
    async with httpx.AsyncClient(timeout=1.0) as client:
        result = await fetch_with_retry(client,"https://httpbin.org/delay/2")
        print(f" Final Result :{result}")
        
        
asyncio.run(main())