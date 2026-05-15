from api.routes.patient_routes import (
    PatientRoutes
)


routes = PatientRoutes()


def test_register_patient_route():

    response = routes.register_patient(
        {
            "patient_id": "P500",
            "name": "Amit",
            "department": "cardiology",
            "priority": 2
        }
    )

    assert response["registered"] is True


def test_get_patient_route():

    response = routes.get_patient(
        "P500"
    )

    assert response["found"] is True


def test_update_patient_status_route():

    response = routes.update_patient_status(
        "P500",
        "COMPLETED"
    )

    assert response["updated"] is True


def test_department_patients_route():

    response = routes.get_department_patients(
        "cardiology"
    )

    assert response["count"] >= 1


def test_delete_patient_route():

    response = routes.delete_patient(
        "P500"
    )

    assert response["deleted"] is True