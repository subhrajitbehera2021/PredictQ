from ai_engine.patient_ai.no_show_predictor import (
    NoShowPredictor
)


predictor = NoShowPredictor()


def test_high_no_show_risk():

    result = predictor.predict_no_show(
        previous_no_shows=3,
        travel_distance_km=25,
        waiting_time_minutes=150
    )

    assert result["risk_level"] == "HIGH"


def test_low_no_show_risk():

    result = predictor.predict_no_show(
        previous_no_shows=0,
        travel_distance_km=2,
        waiting_time_minutes=15
    )

    assert result["risk_level"] == "LOW"