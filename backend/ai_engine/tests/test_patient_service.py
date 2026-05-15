from ai_engine.services.patient_service import (
    PatientService
)


service = PatientService()


def test_register_patient():

    result = (
        service.register_patient(
            {
                "patient_id": "P100",
                "name": "Rahul",
                "department": "cardiology",
                "priority": 2
            }
        )
    )

    assert (
        result["registered"]
        is True
    )


def test_get_patient():

    result = (
        service.get_patient(
            "P100"
        )
    )

    assert (
        result["found"]
        is True
    )


def test_update_patient_status():

    result = (
        service.update_patient_status(
            "P100",
            "IN_PROGRESS"
        )
    )

    assert (
        result["updated"]
        is True
    )


def test_department_patients():

    result = (
        service.get_department_patients(
            "cardiology"
        )
    )

    assert (
        result["count"]
        >= 1
    )


def test_delete_patient():

    result = (
        service.delete_patient(
            "P100"
        )
    )

    assert (
        result["deleted"]
        is True
    )