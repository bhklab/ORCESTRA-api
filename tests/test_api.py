import pytest
from src.api import app  # Assuming the API app is defined here

@pytest.fixture
def client():
    from fastapi.testclient import TestClient
    return TestClient(app)

def test_root(client):
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Welcome to the Snakemake Orchestrator API!"}