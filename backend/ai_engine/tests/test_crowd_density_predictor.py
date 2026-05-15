from ai_engine.crowd_ai.crowd_density_predictor import (
    CrowdDensityPredictor
)


predictor = CrowdDensityPredictor()


def test_high_crowd_density():

    result = predictor.predict_density(
        patient_count=90,
        waiting_area_capacity=100
    )

    assert result["crowd_level"] == "CRITICAL"


def test_low_crowd_density():

    result = predictor.predict_density(
        patient_count=20,
        waiting_area_capacity=100
    )

    assert result["crowd_level"] == "LOW"