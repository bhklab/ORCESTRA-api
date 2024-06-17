
from orcestrator.common import get_logger
from orcestrator.models.Pipeline import (
    CreatePipeline,
    PipelineOut,
)
from motor.motor_asyncio import AsyncIOMotorDatabase

from typing import List, Optional

logger = get_logger()

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


async def get_pipeline_by_name(
    pipeline_name: str,
    db: AsyncIOMotorDatabase,
) -> Optional[PipelineOut]:
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
