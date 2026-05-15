from ai_engine.ml.evaluation.drift_detector import (
    DriftDetector
)


detector = DriftDetector()


def test_set_reference_data():

    mean = detector.set_reference_data(
        [10, 20, 30]
    )

    assert mean == 20


def test_detect_drift():

    detector.set_reference_data(
        [10, 20, 30]
    )

    result = detector.detect_drift(
        [100, 120, 140]
    )

    assert (
        result["drift_detected"]
        is True
    )


def test_drift_history():

    history = (
        detector.get_drift_history()
    )

    assert len(history) >= 1