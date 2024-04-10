from .common import PyObjectId


"""
Basic pipeline model

Pipeline:
    - id
    - name
    - git_url
    - output_files


Snakemake pipeline model inheriting from the basic pipeline model

SnakemakePipeline:

    - id
    - name
    - git_url
    - output_files
    - Snakefile_path
    - config_file_path
    - conda_env_file_path

"""

from pydantic import (
    BaseModel,
    Field,
)

from typing import List


class SnakemakePipeline(BaseModel):
    id: PyObjectId = Field(alias="_id", default=None)
    name: str
    git_url: str
    output_files: List[str]
    snakefile_path: str = Field(
        default="./Snakefile",
    )
    config_file_path: str = Field(
        default="./config/config.yaml",
    )
    conda_env_file_path: str = Field(
        default="./pipeline.yaml",
    )


if __name__ == "__main__":
    # pixi run python -m src.db.models.Pipeline

    import os
    from pydantic import BaseModel, Field
    import motor.motor_asyncio
    from motor.motor_asyncio import AsyncIOMotorCollection, AsyncIOMotorDatabase
    from pydantic import ConfigDict
    from pymongo.results import InsertOneResult
    import asyncio

    client = motor.motor_asyncio.AsyncIOMotorClient(os.environ["MONGODB_URL"])
    db: AsyncIOMotorDatabase = client.get_database("pipelines")
    snakemake_pipelines: AsyncIOMotorCollection = db.get_collection(
        "snakemake_pipelines"
    )

    async def create_snakemake_pipeline(snakemake_pipeline: SnakemakePipeline):
        # Insert the student into the database
        new_snakemake_pipeline: InsertOneResult
        new_snakemake_pipeline = await snakemake_pipelines.insert_one(
            document=snakemake_pipeline.model_dump(by_alias=True, exclude=["id"])
        )

        # Return the id of the student
        return new_snakemake_pipeline.inserted_id

    def main():
        snakemake_pipeline = SnakemakePipeline(
            name="test_pipeline",
            git_url="github.com/repo",
            output_files=["results/pset.rds", "results/dnl.json"],
            snakefile_path="./Snakefile",
        )

        print(snakemake_pipeline.model_dump())

        loop: asyncio.AbstractEventLoop = asyncio.get_event_loop()

        pipeline = loop.run_until_complete(
            create_snakemake_pipeline(snakemake_pipeline)
        )

        print(f"Pipeline id: {pipeline}")

    main()
