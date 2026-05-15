from ai_engine.ml.pipelines.inference_pipeline import (
    InferencePipeline
)


pipeline = InferencePipeline()


def test_run_complete_pipeline():

    result = pipeline.run_pipeline(
        {
            "eta_features": {
                "queue_size": 10,
                "available_doctors": 2,
                "patient_priority": 2,
                "symptoms_count": 1
            },

            "no_show_features": {
                "previous_no_shows": 2,
                "travel_distance_km": 15,
                "waiting_time_minutes": 90
            },

            "crowd_features": {
                "patient_count": 80,
                "room_capacity": 100,
                "doctor_count": 5
            }
        }
    )

    assert (
        "eta_prediction"
        in result
    )

    assert (
        "no_show_prediction"
        in result
    )

    assert (
        "crowd_prediction"
        in result
    )


def test_pipeline_history():

    history = (
        pipeline.get_pipeline_history()
    )

    assert len(history) >= 1