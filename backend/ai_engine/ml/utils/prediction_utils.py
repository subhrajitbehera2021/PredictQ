from ai_engine.utils.logging_utils import (
    get_logger
)


logger = get_logger(__name__)


class PredictionUtils:

    @staticmethod
    def format_prediction_response(
        prediction_type: str,
        value,
        confidence: float,
        source: str = "RULE_BASED"
    ):

        response = {
            "prediction_type": prediction_type,
            "value": value,
            "confidence": confidence,
            "confidence_label": (
                PredictionUtils.get_confidence_label(
                    confidence
                )
            ),
            "source": source,
            "use_fallback": (
                PredictionUtils.should_use_fallback(
                    confidence
                )
            )
        }

        logger.info(
            f"Prediction response formatted: {prediction_type}"
        )

        return response

    @staticmethod
    def get_confidence_label(
        confidence: float
    ):

        if confidence >= 85:
            return "HIGH"

        if confidence >= 60:
            return "MEDIUM"

        return "LOW"

    @staticmethod
    def should_use_fallback(
        confidence: float
    ):

        return confidence < 60

    @staticmethod
    def normalize_prediction_value(
        value,
        minimum: float = 0,
        maximum: float = 100
    ):

        try:
            numeric_value = float(value)
        except (TypeError, ValueError):
            numeric_value = minimum

        return min(
            max(numeric_value, minimum),
            maximum
        )