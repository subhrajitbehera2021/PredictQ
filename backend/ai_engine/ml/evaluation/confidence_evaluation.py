from ai_engine.utils.logging_utils import (
    get_logger
)


logger = get_logger(__name__)


class ConfidenceEvaluation:

    def __init__(self):

        self.evaluation_history = []

    # =====================================================
    # CALCULATE CONFIDENCE
    # =====================================================

    def calculate_confidence(
        self,
        actual: float,
        predicted: float
    ):

        if actual == 0:
            confidence = 0

        else:

            error_percentage = abs(
                (
                    actual
                    - predicted
                ) / actual
            ) * 100

            confidence = max(
                0,
                100 - error_percentage
            )

        result = {
            "actual": actual,
            "predicted": predicted,
            "confidence_score": round(
                confidence,
                2
            )
        }

        self.evaluation_history.append(
            result
        )

        logger.info(
            f"Confidence evaluated: "
            f"{confidence:.2f}%"
        )

        return result

    # =====================================================
    # DECIDE TRUST LEVEL
    # =====================================================

    def evaluate_trust_level(
        self,
        confidence_score: float
    ):

        if confidence_score >= 85:

            return "HIGH"

        elif confidence_score >= 60:

            return "MEDIUM"

        return "LOW"

    # =====================================================
    # SHOULD USE FALLBACK
    # =====================================================

    def should_use_fallback(
        self,
        confidence_score: float
    ):

        return confidence_score < 60

    # =====================================================
    # GET HISTORY
    # =====================================================

    def get_evaluation_history(self):

        return self.evaluation_history