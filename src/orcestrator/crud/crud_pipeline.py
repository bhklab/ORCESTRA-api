from typing import List, Optional

from motor.motor_asyncio import AsyncIOMotorDatabase

from orcestrator.common import get_logger
from orcestrator.models.Pipeline import CreatePipeline, PipelineOut, UpdatePipeline

logger = get_logger()


###############################################################################
# CREATE
async def create_pipeline(
    pipeline: CreatePipeline,
    db: AsyncIOMotorDatabase,
) -> PipelineOut:
    if await get_pipeline_by_name(
        pipeline.pipeline_name,
        db,
    ):
        raise ValueError("Pipeline with this name already exists")

    logger.info(f"Creating pipeline {pipeline.pipeline_name}")
    logger.debug(f"{pipeline.model_dump_json()}")

    new_pipeline = pipeline.model_dump()
    result = await db["pipelines"].insert_one(new_pipeline)
    new_pipeline["id"] = result.inserted_id

    return PipelineOut(**new_pipeline)


###############################################################################
# READ
async def get_pipeline_by_name(
    pipeline_name: str,
    db: AsyncIOMotorDatabase,
) -> Optional[PipelineOut]:
    """Query the database for a pipeline by name and return it if found."""
    pipeline = await db["pipelines"].find_one(
        filter={"pipeline_name": pipeline_name},
    )
    if pipeline:
        return PipelineOut(**pipeline)
    return None


async def get_all_pipelines(
    db: AsyncIOMotorDatabase,
) -> List[PipelineOut]:
    pipelines = await db["pipelines"].find().to_list(length=None)
    return [PipelineOut(**pipeline) for pipeline in pipelines]


###############################################################################
# UPDATE
async def update_pipeline_fields(
    pipeline_name: str,
    updated_pipeline: UpdatePipeline,
    db: AsyncIOMotorDatabase,
) -> PipelineOut:
    existing_pipeline = await get_pipeline_by_name(pipeline_name, db)

    if not existing_pipeline:
        raise ValueError("Pipeline not found")
    logger.debug(f"Updating pipeline {pipeline_name}")
    updated_pipeline_data = updated_pipeline.model_dump()
    new_pipeline_data = {**existing_pipeline.model_dump(), **updated_pipeline_data}

    result = await db["pipelines"].update_one(
        filter={"pipeline_name": pipeline_name},
        update={"$set": updated_pipeline_data},
    )

    if result.modified_count == 0:
        raise ValueError("Pipeline not updated")
    return PipelineOut(**new_pipeline_data)


###############################################################################
# DELETE


async def delete_pipeline(
    pipeline_name: str,
    db: AsyncIOMotorDatabase,
) -> None:
    result = await db["pipelines"].delete_one(
        filter={"pipeline_name": pipeline_name},
    )
    if result.deleted_count == 0:
        raise ValueError("Pipeline not found")
    logger.info(f"Deleted pipeline {pipeline_name}")
