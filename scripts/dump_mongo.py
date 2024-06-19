"""This script is used to dump the data from the MongoDB database to a JSON file"""

import json
from bson.json_util import dumps
import os
from datetime import datetime
from typing import List
import dotenv
import pymongo
from pymongo.database import Database
from orcestrator.common.logging.logging_config import get_logger

dotenv.load_dotenv()

logger = get_logger()


def get_mongo_client() -> pymongo.MongoClient:
    return pymongo.MongoClient(os.environ.get("MONGO_URI"))


def get_mongo_db(client: pymongo.MongoClient) -> Database:
    db = os.environ.get("MONGO_DB")

    if db is None:
        logger.error("MONGO_DB not set")
        raise ValueError("MONGO_DB not set")
    return client[db]


def dump_data_to_json(data: List[dict], file_name: str) -> None:
    with open(file_name, "w") as file:
        json.dump(json.loads(dumps(data)), file, indent=4)
    logger.info(f"Data dumped to {file_name}")


if __name__ == "__main__":
    client = get_mongo_client()
    db = get_mongo_db(client)

    collection_names = db.list_collection_names()
    logger.info(f"Collection names: {collection_names}")
    for collection_name in collection_names:
        collection = db[collection_name]
        data = list(collection.find())
        logger.info(f"Data count for {collection_name}: {len(data)}")
        file_name = f"data/{collection_name}_{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.json"
        dump_data_to_json(data, file_name)

    client.close()
