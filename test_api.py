from fastapi.testclient import TestClient
import os

os.environ["DB_NAME"] = "test_applications.db"
from api import app

client = TestClient(app)


def test_health():
    response = client.get("/health")

    assert response.status_code == 200
    assert response.json() == {"status": "ok"}

def test_create_application():
    response = client.post(
        "/applications",
        json={
            "company": "Test Company",
            "position": "Backend Developer",
            "status": "Saved"
        }
    )

    assert response.status_code == 200

    data = response.json()

    assert data["message"] == "Application created successfully"
    assert "application_id" in data

def test_get_applications():
    response = client.get("/applications")

    assert response.status_code == 200

    data = response.json()

    assert isinstance(data, list)

def test_get_application():
    create_response = client.post(
        "/applications",
        json={
            "company": "Get Test Company",
            "position": "Python Developer",
            "status": "Applied"
        }
    )

    application_id = create_response.json()["application_id"]

    response = client.get(
        f"/applications/{application_id}"
    )

    assert response.status_code == 200

    data = response.json()

    assert data["id"] == application_id
    assert data["company"] == "Get Test Company"
    assert data["position"] == "Python Developer"
    assert data["status"] == "Applied"

def test_update_application():
    create_response = client.post(
        "/applications",
        json={
            "company": "Patch Test Company",
            "position": "Backend Developer",
            "status": "Saved"
        }
    )

    application_id = create_response.json()["application_id"]

    response = client.patch(
        f"/applications/{application_id}",
        json={
            "status": "Interview"
        }
    )

    assert response.status_code == 200

    data = response.json()

    assert data["message"] == "Application status updated successfully"

    get_response = client.get(
        f"/applications/{application_id}"
    )

    assert get_response.status_code == 200

    application = get_response.json()

    assert application["status"] == "Interview"

def test_delete_application():
    create_response = client.post(
        "/applications",
        json={
            "company": "Delete Test Company",
            "position": "Backend Developer",
            "status": "Saved"
        }
    )

    application_id = create_response.json()["application_id"]

    response = client.delete(
        f"/applications/{application_id}"
    )

    assert response.status_code == 200

    data = response.json()

    assert data["message"] == "Application deleted successfully"

    get_response = client.get(
        f"/applications/{application_id}"
    )

    assert get_response.status_code == 404