from fastapi import FastAPI, Depends
from fastapi.responses import HTMLResponse
from motor.motor_asyncio import AsyncIOMotorDatabase

from contextlib import asynccontextmanager

# from ves.api.v1 import users, events
from orcestrator.api.v1 import pipeline
from orcestrator.common import setup_logger
from orcestrator.db import connect_and_init_db, close_db_connect, get_db

from fastapi_cache import FastAPICache
from fastapi_cache.backends.redis import RedisBackend

from redis import asyncio as aioredis
import os 

env = os.environ.get("ENV", "devel")
logger = setup_logger(env)

@asynccontextmanager
async def lifespan(app: FastAPI):
    try:
        logger.info("Initializing Database Connection...")
        await connect_and_init_db()        
        logger.info("Starting application...")
        redis = aioredis.from_url("redis://redis-cache:6379")
        FastAPICache.init(RedisBackend(redis), prefix="fastapi-cache")
        yield
    finally:
        logger.info("Closing Database Connection...")
        await close_db_connect()
        print("Stopping application...")


app = FastAPI(lifespan=lifespan)

app.include_router(router=pipeline.router, prefix="/api", tags=["pipelines"])

@app.get(path="/", response_class=HTMLResponse)
async def read_root(db: AsyncIOMotorDatabase = Depends(get_db)):
    # Return a clickable link to the api docs as html
    return """
    <html>
        <head>
            <title>API Docs</title>
        </head>
        <body>
            <h1>API Docs</h1>
            <a href="/docs">API Documentation</a>
        </body> 
    </html>
    """
