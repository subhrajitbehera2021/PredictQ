from ai_engine.ml.inference.no_show_inference import (
    NoShowInference
)


inference = NoShowInference()


def test_rule_based_no_show_high_risk():

    result = inference.predict_no_show(
        {
            "previous_no_shows": 3,
            "travel_distance_km": 25,
            "waiting_time_minutes": 150
        }
    )

    assert result["risk_level"] == "HIGH"
    assert result["source"] == "RULE_BASED"


def test_rule_based_no_show_low_risk():

    result = inference.predict_no_show(
        {
            "previous_no_shows": 0,
            "travel_distance_km": 2,
            "waiting_time_minutes": 10
        }
    )

    assert result["risk_level"] == "LOW"