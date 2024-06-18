import time
from functools import wraps
from typing import Callable, List

from fastapi import (
    APIRouter,
    Body,
    Depends,
    HTTPException,
    Path,
)
from fastapi_cache.decorator import cache
from motor.motor_asyncio import AsyncIOMotorDatabase

from orcestrator.common import get_logger
from orcestrator.crud import crud_pipeline
from orcestrator.db import get_db
from orcestrator.models.Pipeline import (
    CreatePipeline,
    PipelineOut,
    UpdatePipeline,
)

router = APIRouter()

logger = get_logger()


def log_execution_time(func: Callable) -> Callable:
    @wraps(func)
    async def wrapper(*args, **kwargs):  # noqa
        start_time = time.time()
        result = await func(*args, **kwargs)
        end_time = time.time()
        execution_time = end_time - start_time
        logger.info(f"Time taken for {func.__name__}: {execution_time:.3f} seconds")
        return result

    return wrapper

###############################################################################
# CREATE
@router.post("/pipelines", response_model=PipelineOut)
@log_execution_time
async def create_pipeline(
    pipeline: CreatePipeline,
    db: AsyncIOMotorDatabase = Depends(get_db),
) -> PipelineOut:
    try:
        new_pipeline = await crud_pipeline.create_pipeline(pipeline, db)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    else:
        return new_pipeline


###############################################################################
# READ


@router.get("/pipelines/{pipeline_name}", response_model=PipelineOut)
@log_execution_time
@cache(expire=60)
async def get_pipeline_by_name(
    pipeline_name: str = Path(..., title="The name of the pipeline to retrieve"),
    db: AsyncIOMotorDatabase = Depends(get_db),
) -> PipelineOut:
    pipeline = await crud_pipeline.get_pipeline_by_name(pipeline_name, db)
    if pipeline is None:
        raise HTTPException(status_code=404, detail="Pipeline not found")
    return pipeline


@router.get("/pipelines", response_model=list[PipelineOut])
@log_execution_time
@cache(expire=60)
async def get_pipelines(
    db: AsyncIOMotorDatabase = Depends(get_db),
) -> List[PipelineOut]:
    pipelines = await crud_pipeline.get_all_pipelines(db)
    if not pipelines:
        raise HTTPException(status_code=404, detail="No pipelines found")
    return pipelines


###############################################################################
# UPDATE

@router.put("/pipelines/{pipeline_name}", response_model=PipelineOut)
async def update_pipeline(
    pipeline_name: str = Path(..., title="The name of the pipeline to update"),
    updated_pipeline: UpdatePipeline = Body(None),
    db: AsyncIOMotorDatabase = Depends(get_db),
) -> PipelineOut:
    if updated_pipeline is None:
        raise HTTPException(status_code=400, detail="No fields to update")

    try:
        resolved_pipeline_update = await crud_pipeline.update_pipeline_fields(
            pipeline_name, updated_pipeline, db
        )
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    else:
        return resolved_pipeline_update


###############################################################################
# DELETE

@router.delete("/pipelines/{pipeline_name}", response_model=PipelineOut)
@log_execution_time
@cache(expire=60)
async def delete_pipeline(
    pipeline_name: str,
    db: AsyncIOMotorDatabase = Depends(get_db),
) -> PipelineOut:
    pipeline = await crud_pipeline.get_pipeline_by_name(pipeline_name, db)
    if pipeline is None:
        raise HTTPException(status_code=404, detail="Pipeline not found")
    await db["pipelines"].delete_one({"pipeline_name": pipeline_name})
    return pipeline
