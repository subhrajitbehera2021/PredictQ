from ai_engine.ml.utils.prediction_utils import (
    PredictionUtils
)


def test_confidence_label():

    assert (
        PredictionUtils.get_confidence_label(
            90
        )
        == "HIGH"
    )


def test_fallback_decision():

    assert (
        PredictionUtils.should_use_fallback(
            40
        )
        is True
    )


def test_format_prediction_response():

    response = (
        PredictionUtils.format_prediction_response(
            prediction_type="ETA",
            value=30,
            confidence=90,
            source="RULE_BASED"
        )
    )

    assert response["prediction_type"] == "ETA"
    assert response["confidence_label"] == "HIGH"


def test_normalize_prediction_value():

    value = (
        PredictionUtils.normalize_prediction_value(
            150,
            minimum=0,
            maximum=100
        )
    )

    assert value == 100