import pytest
from orcestrator.crud import crud_pipeline
from orcestrator.models.Pipeline import CreatePipeline
from orcestrator.db import DataBase
import asyncio

pipelines = [
    {
        "pipeline_name": "example_pipeline",
        "git_url": "https://github.com/example/repo",
        "output_files": ["file1.txt", "file2.txt"],
        "snakefile_path": "Snakefile",
        "config_file_path": "config/config.yaml",
        "conda_env_file_path": "pipeline_env.yaml",
    }
]
    

@pytest.fixture
def test_client():
    db = DataBase.init_test_db()
    yield db
    # delete all test data
    # db['pipelines'].delete_many({}) 
    asyncio.run(db['pipelines'].delete_many({}))

@pytest.mark.asyncio
async def test_create_pipeline(test_client):
    pipeline = CreatePipeline(
        **pipelines[0]
    )
    new_pipeline = await crud_pipeline.create_pipeline(pipeline)
    assert new_pipeline.pipeline_name == pipeline.pipeline_name
    assert new_pipeline.pipeline_description == pipeline.pipeline_description
    assert new_pipeline.pipeline_steps == pipeline.pipeline_steps