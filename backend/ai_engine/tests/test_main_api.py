from fastapi.testclient import TestClient

from main import app


client = TestClient(app)


def test_root_endpoint():

    response = client.get("/")

    assert response.status_code == 200
    assert response.json()["status"] == "ACTIVE"


def test_health_endpoint():

    response = client.get("/health")

    assert response.status_code == 200
    assert response.json()["status"] == "HEALTHY"


def test_register_patient_api():

    response = client.post(
        "/patients/register",
        json={
            "patient_id": "P900",
            "name": "Amit",
            "department": "cardiology",
            "priority": 2
        }
    )

    assert response.status_code == 200
    assert response.json()["registered"] is True


def test_get_patient_api():

    response = client.get("/patients/P900")

    assert response.status_code == 200
    assert response.json()["found"] is True


def test_update_patient_status_api():

    response = client.put(
        "/patients/P900/status",
        json={
            "status": "COMPLETED"
        }
    )

    assert response.status_code == 200
    assert response.json()["updated"] is True


def test_department_patients_api():

    response = client.get(
        "/departments/cardiology/patients"
    )

    assert response.status_code == 200
    assert response.json()["count"] >= 1


def test_delete_patient_api():

    response = client.delete("/patients/P900")

    assert response.status_code == 200
    assert response.json()["deleted"] is True