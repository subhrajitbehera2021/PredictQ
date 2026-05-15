from ai_engine.ml.inference.crowd_inference import (
    CrowdInference
)


inference = CrowdInference()


def test_rule_based_crowd_critical():

    result = inference.predict_crowd(
        {
            "patient_count": 95,
            "room_capacity": 100,
            "doctor_count": 5
        }
    )

    assert result["crowd_level"] == "CRITICAL"
    assert result["source"] == "RULE_BASED"


def test_rule_based_crowd_low():

    result = inference.predict_crowd(
        {
            "patient_count": 20,
            "room_capacity": 100,
            "doctor_count": 5
        }
    )

    assert result["crowd_level"] == "LOW"