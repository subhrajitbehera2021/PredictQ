from ai_engine.monitoring.prediction_monitor import (
    PredictionMonitor
)


monitor = PredictionMonitor()


def test_record_prediction():

    log = monitor.record_prediction(
        "WAIT_TIME",
        35,
        confidence=0.9
    )

    assert log["prediction_type"] == "WAIT_TIME"
    assert log["confidence"] == 0.9


def test_low_confidence_detection():

    result = monitor.check_low_confidence(
        0.4
    )

    assert result is True


def test_prediction_failure():

    log = monitor.record_prediction_failure(
        "ETA",
        "Model timeout"
    )

    assert log["status"] == "FAILED"