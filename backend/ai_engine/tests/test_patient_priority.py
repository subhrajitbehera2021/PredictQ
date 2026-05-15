from ai_engine.patient_ai.patient_priority_engine import (
    PatientPriorityEngine
)


engine = PatientPriorityEngine()


def test_patient_priority():

    patient = {
        "patient_id": "P100",
        "severity": "critical"
    }

    enriched = (
        engine.enrich_patient_priority(
            patient
        )
    )

    assert enriched["priority"] == 5