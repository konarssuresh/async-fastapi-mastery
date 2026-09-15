from contextlib import asynccontextmanager
from fastapi import FastAPI


@asynccontextmanager
async def lifespan(app:FastAPI):
    print("Application starting.....")
    
    app.state.message = "Hello from application state"
    
    app.state.resource = {
        "name":"my resource",
        "status":"ready"
    }
    
    yield
    
    print("Application shutting down....")
    print("cleaning up shared resource...")
    app.state.resource = None
    
app = FastAPI(lifespan=lifespan)

@app.get("/")
async def root():
    return app.state.resource