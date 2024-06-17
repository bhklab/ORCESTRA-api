from orcestrator.db.models.common import PyObjectId

from pydantic import (
    BaseModel,
    Field,
)

from typing import List


class SnakemakePipeline(BaseModel):
    id: PyObjectId = Field(alias="_id", default=None)
    pipeline_name: str
    git_url: str
    output_files: List[str]
    snakefile_path: str = Field(
        default="Snakefile",
    )
    config_file_path: str = Field(
        default="config/config.yaml",
    )
    conda_env_file_path: str = Field(
        default="pipeline_env.yaml",
    )
    jobs: int = Field(
        default=1,
    )


def main():
    # pixi run python -m src.db.models.Pipeline
    """
    This main area is to test the implementation of the model
    """

    import os
    from pydantic import BaseModel, Field
    import motor.motor_asyncio
    from motor.motor_asyncio import AsyncIOMotorCollection, AsyncIOMotorDatabase
    from pymongo.results import InsertOneResult
    import asyncio
    from rich import print

    client = motor.motor_asyncio.AsyncIOMotorClient(os.environ["MONGO_URI"])
    db: AsyncIOMotorDatabase = client.get_database("pipelines")
    snakemake_pipelines: AsyncIOMotorCollection = db.get_collection(
        name="snakemake_pipelines"
    )

    async def create_snakemake_pipeline(snakemake_pipeline: SnakemakePipeline):
        # Insert the student into the database
        new_snakemake_pipeline: InsertOneResult
        new_snakemake_pipeline = await snakemake_pipelines.insert_one(
            document=snakemake_pipeline.model_dump(by_alias=True, exclude={"id"})
        )

        # Return the id of the student
        return new_snakemake_pipeline.inserted_id

    async def get_all_pipeline_names() -> list[str]:
        pipeline_names: list[str] = await snakemake_pipelines.distinct("pipeline_name")

        return pipeline_names

    def main():
        import datetime

        today_pipeline: str = (
            f"pipeline_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}"
        )

        snakemake_pipeline = SnakemakePipeline(
            pipeline_name=today_pipeline,
            git_url="github.com/repo",
            output_files=["results/pset.rds", "results/dnl.json"],
            snakefile_path="Snakefile",
        )

        print(snakemake_pipeline.model_dump())

        loop: asyncio.AbstractEventLoop = asyncio.get_event_loop()

        pipeline = loop.run_until_complete(
            create_snakemake_pipeline(snakemake_pipeline)
        )

        print(f"Pipeline id: {pipeline}")

        pipeline_names = loop.run_until_complete(get_all_pipeline_names())

        print(f"Pipeline names: {pipeline_names}")

    main()

    # function to get the names of all pipelines


if __name__ == "__main__":
    main()
