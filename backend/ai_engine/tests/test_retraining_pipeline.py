from ai_engine.ml.pipelines.retraining_pipeline import (
    RetrainingPipeline
)


pipeline = RetrainingPipeline()


sample_training_dataset = [
    {
        "queue_size": 10,
        "available_doctors": 2,
        "patient_priority": 1,
        "wait_time": 25
    },
    {
        "queue_size": 20,
        "available_doctors": 3,
        "patient_priority": 2,
        "wait_time": 40
    }
]


def test_reference_initialization():

    mean = pipeline.initialize_reference_data(
        [10, 20, 30]
    )

    assert mean == 20


def test_retrain_if_drift_detected():

    pipeline.initialize_reference_data(
        [10, 20, 30]
    )

    result = pipeline.retrain_if_needed(
        new_values=[100, 120, 140],
        training_dataset=sample_training_dataset
    )

    assert result["retrained"] is True


def test_retraining_history():

    history = pipeline.get_retraining_history()

    assert len(history) >= 1