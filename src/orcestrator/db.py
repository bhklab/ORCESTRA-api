from motor.motor_asyncio import AsyncIOMotorClient, AsyncIOMotorDatabase

from orcestrator.common import get_logger
from orcestrator.common.config import settings

logger = get_logger()

db_client: AsyncIOMotorClient | None = None


async def get_db() -> AsyncIOMotorDatabase:
    global db_client

    db_name = settings.MONGO_DB
    if db_name is None:
        raise ValueError("MONGO_DB is not set")

    if db_client is None:
        raise ValueError("Mongo has not been connected")

    return db_client[db_name]


async def connect_and_init_db() -> None:
    global db_client
    try:
        db_client = AsyncIOMotorClient(settings.MONGO_URI)
        logger.info("Connected to mongo.")
    except Exception as e:
        logger.exception(f"Could not connect to mongo: {e}")
        raise


async def close_db_connect() -> None:
    global db_client
    if db_client is None:
        logger.warning("Connection is None, nothing to close.")
        return
    db_client.close()
    db_client = None
    logger.info("Mongo connection closed.")
