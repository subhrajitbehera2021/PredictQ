from ai_engine.engine import (
    AIQueueEngine
)


engine = AIQueueEngine()


def test_full_ai_engine_flow():

    boot_result = engine.boot()

    assert boot_result["status"] == "BOOTED"

    department_result = (
        engine.create_department(
            "cardiology"
        )
    )

    assert department_result["created"] is True

    doctor_result = (
        engine.register_doctor(
            "DOC001",
            "Dr. Smith",
            "cardiology"
        )
    )

    assert doctor_result["registered"] is True

    patient_data = {
        "patient_id": "PAT001",
        "name": "John",
        "age": 45,
        "severity": "high",
        "queue_size": 10,
        "available_doctors": 2
    }

    queue_result = (
        engine.register_patient(
            "cardiology",
            patient_data
        )
    )

    assert len(queue_result) >= 1

    prediction = (
        engine.predict_wait_time(
            queue_size=10,
            available_doctors=2
        )
    )

    assert prediction >= 0

    realtime_result = (
        engine.run_realtime_pipeline(
            patient_data
        )
    )

    assert "eta_prediction" in realtime_result

    monitoring = (
        engine.monitor_system(
            queue_size=10,
            available_doctors=2
        )
    )

    assert monitoring is not None

    insights = (
    engine.generate_hospital_insights(
        {
            "cardiology": {
                "queue_size": 10,
                "patients_today": 50,
                "available_doctors": 2
            },
            "neurology": {
                "queue_size": 5,
                "patients_today": 20,
                "available_doctors": 1
            }
        }
    )
)

    assert insights is not None

    analytics = (
        engine.generate_queue_analytics(
            "cardiology",
            [10, 15, 20]
        )
    )

    assert analytics is not None

    decisions = (
        engine.generate_realtime_decisions(
            {
                "cardiology": {
                    "queue_size": 20,
                    "available_doctors": 2
                },
                "neurology": {
                    "queue_size": 8,
                    "available_doctors": 3
                }
            }
        )
    )

    assert decisions is not None

    summary = engine.system_summary()

    assert summary is not None