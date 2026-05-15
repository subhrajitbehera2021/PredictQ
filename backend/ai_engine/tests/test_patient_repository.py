from ai_engine.database.patient_repository import (
    PatientRepository
)


repo = PatientRepository()


def test_add_patient():

    result = repo.add_patient(
        {
            "patient_id": "P001",
            "name": "Rahul",
            "department": "cardiology",
            "priority": 2,
            "status": "WAITING"
        }
    )

    assert result["saved"] is True


def test_get_patient_by_id():

    patient = repo.get_patient_by_id(
        "P001"
    )

    assert patient["name"] == "Rahul"


def test_get_patients_by_department():

    patients = repo.get_patients_by_department(
        "cardiology"
    )

    assert len(patients) >= 1


def test_update_patient_status():

    patient = repo.update_patient_status(
        "P001",
        "IN_PROGRESS"
    )

    assert patient["status"] == "IN_PROGRESS"


def test_delete_patient():

    deleted = repo.delete_patient(
        "P001"
    )

    assert deleted is True