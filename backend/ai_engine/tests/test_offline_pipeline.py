from ai_engine.ml.pipelines.offline_pipeline import (
    OfflinePipeline
)


pipeline = OfflinePipeline()


sample_data = [
    {
        "patient_id": "P001",
        "queue_size": 10,
        "available_doctors": 2,
        "priority": 2,
        "symptoms": ["fever"],
        "previous_no_shows": 1,
        "travel_distance_km": 12,
        "waiting_time_minutes": 60,
        "patient_count": 40,
        "room_capacity": 100,
        "doctor_count": 5
    },
    {
        "patient_id": "P001",
        "queue_size": 10,
        "available_doctors": 2,
        "priority": 2,
        "symptoms": ["fever"],
        "previous_no_shows": 1,
        "travel_distance_km": 12,
        "waiting_time_minutes": 60,
        "patient_count": 40,
        "room_capacity": 100,
        "doctor_count": 5
    }
]


def test_offline_pipeline():

    result = pipeline.process_historical_data(
        sample_data
    )

    assert result["cleaned_records"] == 1
    assert "training_dataset" in result
    assert "queue_analytics" in result


def test_offline_pipeline_history():

    history = pipeline.get_pipeline_history()

    assert len(history) >= 1