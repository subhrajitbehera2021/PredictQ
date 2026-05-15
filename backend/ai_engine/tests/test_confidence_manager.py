from ai_engine.core.confidence_manager import (
    ConfidenceManager
)


manager = ConfidenceManager()


def test_prediction_confidence():

    result = manager.evaluate_prediction(
        prediction_type="ETA",
        actual=100,
        predicted=90
    )

    assert (
        result["confidence_score"]
        > 0
    )

    assert (
        result["trust_level"]
        in ["HIGH", "MEDIUM", "LOW"]
    )


def test_accept_prediction():

    assert (
        manager.should_accept_prediction(
            80
        )
        is True
    )


def test_confidence_history():

    history = (
        manager.get_confidence_history()
    )

    assert len(history) >= 1