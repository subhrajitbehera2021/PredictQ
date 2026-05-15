from ai_engine.ml.pipelines.realtime_pipeline import (
    RealtimePipeline
)


pipeline = RealtimePipeline()


sample_patient_data = {
    "queue_size": 20,
    "available_doctors": 3,
    "patient_priority": 2,
    "appointment_time": "10:00 AM"
}


def test_realtime_pipeline():

    result = (
        pipeline.process_realtime_data(
            sample_patient_data
        )
    )

    assert (
        "eta_prediction"
        in result
    )

    assert (
        "crowd_prediction"
        in result
    )

    assert (
        "no_show_prediction"
        in result
    )


def test_pipeline_history():

    history = (
        pipeline.get_pipeline_history()
    )

    assert len(history) >= 1