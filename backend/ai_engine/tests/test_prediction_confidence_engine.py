from ai_engine.prediction_ai.prediction_confidence_engine import (
    PredictionConfidenceEngine
)


engine = (
    PredictionConfidenceEngine()
)


def test_eta_prediction_confidence():

    result = (
        engine.evaluate_eta_prediction(
            actual_wait_time=100,
            predicted_wait_time=90
        )
    )

    assert (
        result["confidence_score"]
        > 0
    )


def test_crowd_prediction_confidence():

    result = (
        engine.evaluate_crowd_prediction(
            actual_density=80,
            predicted_density=70
        )
    )

    assert (
        result["trust_level"]
        in ["HIGH", "MEDIUM", "LOW"]
    )


def test_no_show_prediction_confidence():

    result = (
        engine.evaluate_no_show_prediction(
            actual_value=1,
            predicted_value=1
        )
    )

    assert (
        result["use_fallback"]
        is False
    )


def test_prediction_history():

    history = (
        engine.get_prediction_history()
    )

    assert len(history) >= 1