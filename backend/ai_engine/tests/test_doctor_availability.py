from ai_engine.doctor_ai.doctor_availability_engine import (
    DoctorAvailabilityEngine
)


engine = DoctorAvailabilityEngine()


def test_doctor_registration():

    doctor = engine.register_doctor(
        "D001",
        "Dr. Smith",
        "cardiology"
    )

    assert doctor["doctor_id"] == "D001"
    assert doctor["available"] is True


def test_available_doctors():

    doctors = engine.get_available_doctors(
        "cardiology"
    )

    assert len(doctors) >= 1