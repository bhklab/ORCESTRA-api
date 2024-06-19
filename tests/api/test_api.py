import pytest
from fastapi.testclient import TestClient
from orcestrator.models.Pipeline import CreatePipeline, PipelineOut
import os
import json


def test_bad_env():
    with pytest.raises(Exception):
        # This should fail because the ENV is not set for logging
        from orcestrator.main import app as bad_env_app

@pytest.fixture(scope="module")
def client_obj():
    os.environ["ENV"] = "devel"
    os.environ["MONGO_URI"] = "mongodb://localhost:27017"
    os.environ["MONGO_DB"] = "testing_database"
    from orcestrator.main import app
    with TestClient(app) as client:
        yield client

        # after everything has run, delete the test database
        response = client.delete("/api/pipelines")
        assert response.status_code == 200

        # try deleting it again
        response = client.delete("/api/pipelines")
        assert response.status_code == 200
        assert len(response.json()) == 0

@pytest.fixture()
def good_pipeline():
    return CreatePipeline(
        pipeline_name="test_pipeline_successful",
        git_url="https://github.com/bhklab-data-proc/GDSC-Pharmacoset_Snakemake",
        output_files=["results/GDSC.RDS"],
        snakefile_path="Snakefile",
        config_file_path="config/config.yaml",
        conda_env_file_path="pipeline_env.yaml",
    )


def test_read_root(client_obj):
    response = client_obj.get("/")
    assert response.status_code == 200
    assert (
        response.text
        == """
    <html>
        <head>
            <title>API Docs</title>
        </head>
        <body>
            <h1>API Docs</h1>
            <a href="/docs">API Documentation</a>
        </body>
    </html>
    """
    )


@pytest.mark.dependency()
def test_insert_pipeline(
    client_obj,
    good_pipeline,
):
    path = "/api/pipelines"
    response = client_obj.post(path, json=good_pipeline.model_dump())
    print(response.json())
    print(response)
    assert response.status_code == 200
    assert isinstance(response.json(), dict)

    pipeline = PipelineOut(**response.json())
    assert pipeline.pipeline_name == good_pipeline.pipeline_name
    
    # try inserting the same pipeline again
    response = client_obj.post(path, json=good_pipeline.model_dump())
    assert response.status_code == 400


def test_insert_bad(client_obj):
    path = "/api/pipelines"
    with pytest.raises(Exception):
        # this should raise a validation error too
        response = client_obj.post(
            path,
            json=json.loads(
                {
                    "pipeline_name": "test_pipeline_successful",
                    "git_url": "https://github.com/bhklab-data-proc/GDSC-Pharmacoset_Snakemake",
                    "output_files": ["results/GDSC.RDS"],
                    "snakefile_path": 1234,  # type: ignore
                    "config_file_path": "config/config.yaml",
                    "conda_env_file_path": "pipeline_env.yaml",
                }
            ),
        )
        assert response.status_code == 400


@pytest.mark.dependency(depends=["test_insert_pipeline"])
def test_get_pipelines(client_obj):
    response = client_obj.get("/api/pipelines")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
    assert len(response.json()) == 1


@pytest.mark.dependency(depends=["test_get_pipelines"])
def test_get_pipeline_by_name(client_obj, good_pipeline):
    response = client_obj.get(f"/api/pipelines/{good_pipeline.pipeline_name}")
    assert response.status_code == 200
    assert isinstance(response.json(), dict)


def test_get_pipline_by_name_not_found(client_obj):
    response = client_obj.get("/api/pipelines/not_found")
    assert response.status_code == 404
    assert response.json() == {"detail": "Pipeline not found"}
