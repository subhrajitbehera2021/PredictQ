from ai_engine.utils.logging_utils import (
    get_logger
)

from ai_engine.utils.time_utils import (
    TimeUtils
)


logger = get_logger(__name__)


class PredictionMonitor:

    def __init__(self):

        self.prediction_logs = []

    def record_prediction(
        self,
        prediction_type: str,
        predicted_value,
        confidence: float = 1.0
    ):

        log = {
            "prediction_type": prediction_type,
            "predicted_value": predicted_value,
            "confidence": confidence,
            "timestamp": str(TimeUtils.now())
        }

        self.prediction_logs.append(log)

        logger.info(
            f"Prediction recorded: {prediction_type}"
        )

        return log

    def record_prediction_failure(
        self,
        prediction_type: str,
        error_message: str
    ):

        log = {
            "prediction_type": prediction_type,
            "status": "FAILED",
            "error_message": error_message,
            "timestamp": str(TimeUtils.now())
        }

        self.prediction_logs.append(log)

        logger.warning(
            f"Prediction failure recorded: {prediction_type}"
        )

        return log

    def check_low_confidence(
        self,
        confidence: float,
        threshold: float = 0.6
    ):

        return confidence < threshold

    def get_prediction_logs(self):

        return self.prediction_logs

    def get_failed_predictions(self):

        return [
            log
            for log in self.prediction_logs
            if log.get("status") == "FAILED"
        ]

    def clear_logs(self):

        self.prediction_logs = []

        logger.info(
            "Prediction logs cleared"
        )