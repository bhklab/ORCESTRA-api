from motor.motor_asyncio import AsyncIOMotorClient, AsyncIOMotorDatabase
from orcestrator.common.config import settings
import logging


class Database:
    _client: AsyncIOMotorClient | None = None
    _db: AsyncIOMotorDatabase | None = None

    def __init__(self) -> None:
        pass

    @staticmethod
    def connect() -> 'Database':
        mongo = Database()
        try:
            mongo._client = AsyncIOMotorClient(settings.MONGO_URI)
            logging.info("Connected to mongo.")
        except Exception as e:
            logging.exception(f"Could not connect to mongo: {e}")
            raise
        return mongo


    @staticmethod
    def get_db(dbname: str | None = None) -> AsyncIOMotorDatabase:
        if Database._client is None:
            raise ValueError("Mongo has not been connected")
        if settings.MONGO_DB is None:
                raise ValueError("MONGO_DB is not set")
        if Database._db is None:
            Database._db = Database._client[dbname if dbname is not None else settings.MONGO_DB]
        return Database._db

    @staticmethod
    def close() -> None:
        if Database._client is not None:
            Database._client.close()
            logging.info("Disconnected from mongo.")
        else:
            raise ValueError("Mongo has not been connected")
