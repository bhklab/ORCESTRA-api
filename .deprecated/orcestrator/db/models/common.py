from typing import Annotated

from pydantic.functional_validators import BeforeValidator

# Note:
# MongoDB stores data as BSON. FastAPI encodes and decodes data as JSON strings.
# BSON has support for additional non-JSON-native data types, including ObjectId
# which can't be directly encoded as JSON. Because of this, we convert ObjectIds
# to strings before storing them as the id field.


# Create a new type called PyObjectId
# - type is a string
# - before pydantic validates if the string is a valid ObjectId, the BeforeValidator `func` is called on it
#  which in this case will convert the string to a string
#     - It will be represented as a `str` on the model so that it can be serialized to JSON.

PyObjectId = Annotated[str, BeforeValidator(str)]

if __name__ == "__main__":
    # pixi run python -m src.db.models.common

    import os

    import motor.motor_asyncio
    from motor.motor_asyncio import AsyncIOMotorCollection, AsyncIOMotorDatabase
    from pydantic import BaseModel, ConfigDict, Field
    from pymongo.results import InsertOneResult

    client = motor.motor_asyncio.AsyncIOMotorClient(os.environ["MONGODB_URL"])
    db: AsyncIOMotorDatabase = client.get_database("college")
    student_collection: AsyncIOMotorCollection = db.get_collection("students")

    class DemoModel(BaseModel):
        # This will be aliased to `_id` when sent to MongoDB (mongo stores it as `_id`)
        # but provided as `id` in the API requests and responses.
        id: PyObjectId = Field(alias="_id", default=None)
        model_config = ConfigDict(
            populate_by_name=True,
        )

    async def create_student(student: DemoModel):
        # Insert the student into the database
        new_student: InsertOneResult
        new_student = await student_collection.insert_one(
            document=student.model_dump(by_alias=True, exclude={"id"})
        )

        # Return the id of the student
        return new_student.inserted_id

    def main():
        demo_model = DemoModel()

        import asyncio

        loop = asyncio.get_event_loop()

        student_id = loop.run_until_complete(create_student(demo_model))

        print(f"Student id: {student_id}")

    main()
