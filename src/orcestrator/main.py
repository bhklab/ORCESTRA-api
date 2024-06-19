import os
from contextlib import asynccontextmanager
from typing import AsyncGenerator

from fastapi import Depends, FastAPI
from fastapi.responses import HTMLResponse
from fastapi_cache import FastAPICache
from fastapi_cache.backends.redis import RedisBackend
from motor.motor_asyncio import AsyncIOMotorDatabase
from redis import asyncio as aioredis

from orcestrator.api.v1 import pipeline
from orcestrator.common import setup_logger
from orcestrator.db import close_db_connect, connect_and_init_db, get_db

env = os.environ.get('ENV', 'devel')
logger = setup_logger(env)


@asynccontextmanager
async def lifespan(app: FastAPI) -> AsyncGenerator:
    try:
        logger.info('Initializing Database Connection...')
        await connect_and_init_db()
        logger.info('Starting application...')
        redis = aioredis.from_url('redis://redis-cache:6379')
        FastAPICache.init(RedisBackend(redis), prefix='fastapi-cache')
        yield
    finally:
        logger.info('Closing Database Connection...')
        await close_db_connect()
        print('Stopping application...')


app = FastAPI(lifespan=lifespan)

app.include_router(router=pipeline.router, prefix='/api', tags=['Pipelines'])


@app.get(path='/', response_class=HTMLResponse, include_in_schema=False)
async def read_root(db: AsyncIOMotorDatabase = Depends(get_db)) -> HTMLResponse:
    # Return a clickable link to the api docs as html
    return HTMLResponse("""
    <html>
        <head>
            <title>API Docs</title>
        </head>
        <body>
            <h1>API Docs</h1>
            <a href="/docs">API Documentation</a>
        </body>
    </html>
    """)
