from ai_engine.ml.inference.eta_inference import (
    ETAInference
)


inference = ETAInference()


def test_rule_based_eta_inference():

    result = inference.predict_eta(
        {
            "queue_size": 10,
            "available_doctors": 2,
            "patient_priority": 2,
            "symptoms_count": 1
        }
    )

    assert result["eta_minutes"] > 0
    assert result["source"] == "RULE_BASED"


def test_inference_history():

    history = inference.get_inference_history()

    assert len(history) >= 1