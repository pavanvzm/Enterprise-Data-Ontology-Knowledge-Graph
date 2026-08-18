"""Integration tests for REST API endpoints"""

import pytest
from fastapi.testclient import TestClient
from src.api.app import app, populate_sample_data

# Create TestClient without deprecated kwargs
client = TestClient(app)

@pytest.fixture(autouse=True)
def reset_data():
    populate_sample_data()

def test_health_check():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json()["status"] == "healthy"

def test_get_entities():
    response = client.get("/api/v1/entities")
    assert response.status_code == 200
    data = response.json()
    assert "entities" in data
    assert data["count"] >= 8

def test_get_entities_filter():
    response = client.get("/api/v1/entities?type=Customer")
    assert response.status_code == 200
    data = response.json()
    assert data["count"] == 2
    for entity in data["entities"]:
        assert entity["type"] == "Customer"

def test_get_entity_by_id():
    response = client.get("/api/v1/entities/E-001")
    assert response.status_code == 200
    data = response.json()
    assert data["entity"]["id"] == "E-001"
    assert "neighbors" in data

def test_create_and_delete_entity():
    new_entity = {
        "id": "E-999",
        "type": "Warehouse",
        "properties": {"city": "Chicago"}
    }
    create_res = client.post("/api/v1/entities", json=new_entity)
    assert create_res.status_code == 201
    assert create_res.json()["entity"]["id"] == "E-999"

    get_res = client.get("/api/v1/entities/E-999")
    assert get_res.status_code == 200

    del_res = client.delete("/api/v1/entities/E-999")
    assert del_res.status_code == 200

    get_again = client.get("/api/v1/entities/E-999")
    assert get_again.status_code == 404

def test_get_relationships():
    response = client.get("/api/v1/relationships")
    assert response.status_code == 200
    data = response.json()
    assert "relationships" in data
    assert data["count"] >= 6

def test_create_relationship():
    new_rel = {
        "source": "E-001",
        "target": "E-005",
        "type": "INTERESTED_IN",
        "id": "R-999",
        "properties": {"priority": "High"}
    }
    response = client.post("/api/v1/relationships", json=new_rel)
    assert response.status_code == 201
    assert response.json()["relationship"]["id"] == "R-999"

def test_get_stats():
    response = client.get("/api/v1/stats")
    assert response.status_code == 200
    data = response.json()
    assert "total_nodes" in data
    assert "total_edges" in data
    assert "node_type_counts" in data

def test_dashboard_html():
    response = client.get("/dashboard")
    assert response.status_code == 200
    assert "text/html" in response.headers["content-type"]
    assert "Enterprise Data Ontology" in response.text
