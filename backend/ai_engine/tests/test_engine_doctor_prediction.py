from ai_engine.engine import AIQueueEngine


engine = AIQueueEngine()
engine.boot()
engine.create_department("cardiology")


def test_engine_doctor_wait_prediction():

    engine.register_doctor(
        "D001",
        "Dr. Smith",
        "cardiology"
    )

    engine.register_patient(
        "cardiology",
        {
            "patient_id": "P200",
            "name": "Alex",
            "severity": "medium"
        }
    )

    wait_time = engine.predict_department_wait_time(
        "cardiology"
    )

    assert wait_time >= 0