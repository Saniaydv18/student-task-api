import pytest
from app import app, tasks

@pytest.fixture()
def client():
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client

def test_health(client):
    response = client.get("/health")
    assert response.status_code == 200
    assert response.get_json()["status"] == "healthy"

def test_get_tasks(client):
    response = client.get("/tasks")
    assert response.status_code == 200
    assert isinstance(response.get_json(), list)

def test_create_task(client):
    response = client.post("/tasks", json={"title": "Test task"})
    assert response.status_code == 201
    assert response.get_json()["title"] == "Test task"

def test_delete_task(client):
    tasks.append({"id": 9999, "title": "Delete me", "completed": False})
    response = client.delete("/tasks/9999")
    assert response.status_code == 200

def test_invalid_task(client):
    response = client.post("/tasks", json={})
    assert response.status_code == 400
