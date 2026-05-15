from ai_engine.ml.preprocessing.feature_engineering import (
    FeatureEngineering
)


engine = FeatureEngineering()


def test_eta_features():

    patient = {

        "queue_size": 20,
        "available_doctors": 2,
        "priority": 2,
        "symptoms": [
            "fever",
            "headache"
        ]
    }

    features = (
        engine.build_eta_features(
            patient
        )
    )

    assert (
        features["queue_size"]
        == 20
    )

    assert (
        features["symptoms_count"]
        == 2
    )


def test_no_show_features():

    patient = {

        "previous_no_shows": 1,
        "travel_distance_km": 15,
        "waiting_time_minutes": 60
    }

    features = (
        engine.build_no_show_features(
            patient
        )
    )

    assert (
        features[
            "travel_distance_km"
        ] == 15
    )


def test_feature_set_generation():

    patient = {

        "queue_size": 10
    }

    department = {

        "patient_count": 40
    }

    features = (
        engine.generate_feature_set(
            patient,
            department
        )
    )

    assert "eta_features" in features
    assert "crowd_features" in features