from ai_engine.ml.evaluation.confidence_evaluation import (
    ConfidenceEvaluation
)


evaluation = (
    ConfidenceEvaluation()
)


def test_confidence_calculation():

    result = (
        evaluation.calculate_confidence(
            actual=100,
            predicted=90
        )
    )

    assert (
        result["confidence_score"]
        > 0
    )


def test_trust_level():

    level = (
        evaluation.evaluate_trust_level(
            90
        )
    )

    assert level == "HIGH"


def test_fallback_decision():

    decision = (
        evaluation.should_use_fallback(
            40
        )
    )

    assert decision is True


def test_evaluation_history():

    history = (
        evaluation.get_evaluation_history()
    )

    assert len(history) >= 1