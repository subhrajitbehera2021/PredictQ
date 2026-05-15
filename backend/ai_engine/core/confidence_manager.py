from ai_engine.ml.evaluation.confidence_evaluation import (
    ConfidenceEvaluation
)

from ai_engine.utils.logging_utils import (
    get_logger
)


logger = get_logger(__name__)


class ConfidenceManager:

    def __init__(self):

        self.confidence_evaluator = (
            ConfidenceEvaluation()
        )

        self.confidence_history = []

    def evaluate_prediction(
        self,
        prediction_type: str,
        actual: float,
        predicted: float
    ):

        confidence_result = (
            self.confidence_evaluator
            .calculate_confidence(
                actual,
                predicted
            )
        )

        confidence_score = (
            confidence_result[
                "confidence_score"
            ]
        )

        trust_level = (
            self.confidence_evaluator
            .evaluate_trust_level(
                confidence_score
            )
        )

        use_fallback = (
            self.confidence_evaluator
            .should_use_fallback(
                confidence_score
            )
        )

        result = {
            "prediction_type": prediction_type,
            "actual": actual,
            "predicted": predicted,
            "confidence_score": confidence_score,
            "trust_level": trust_level,
            "use_fallback": use_fallback
        }

        self.confidence_history.append(
            result
        )

        logger.info(
            f"Prediction confidence evaluated: "
            f"{prediction_type}"
        )

        return result

    def should_accept_prediction(
        self,
        confidence_score: float
    ):

        return confidence_score >= 60

    def get_confidence_history(self):

        return self.confidence_history

    def clear_history(self):

        self.confidence_history = []

        logger.info(
            "Confidence history cleared"
        )