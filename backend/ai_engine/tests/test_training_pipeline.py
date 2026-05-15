from ai_engine.ml.pipelines.training_pipeline import (
    TrainingPipeline
)


pipeline = TrainingPipeline()


sample_dataset = [

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


def test_training_pipeline():

    result = (
        pipeline.train_eta_model(
            sample_dataset
        )
    )

    assert (
        result["model_trained"]
        is True
    )


def test_training_history():

    history = (
        pipeline.get_training_history()
    )

    assert len(history) >= 1