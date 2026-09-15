from contextlib import asynccontextmanager

import httpx
from fastapi import FastAPI


@asynccontextmanager
async def lifespan(app: FastAPI):
    print("creating http client")
    
    app.state.client = httpx.AsyncClient(
        timeout=5.0
    )
    
    yield
    
    print("cleaning up")
    await app.state.client.aclose()
    

app = FastAPI(lifespan=lifespan)

@app.get("/users")
async def get_users():
    response = await app.state.client.get("https://jsonplaceholder.typicode.com/users")
    response.raise_for_status()
    return response.json()