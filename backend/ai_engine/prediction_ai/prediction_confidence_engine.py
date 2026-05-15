from ai_engine.core.confidence_manager import (
    ConfidenceManager
)

from ai_engine.utils.logging_utils import (
    get_logger
)


logger = get_logger(__name__)


class PredictionConfidenceEngine:

    def __init__(self):

        self.confidence_manager = (
            ConfidenceManager()
        )

        self.prediction_history = []

    # =====================================================
    # EVALUATE ETA PREDICTION
    # =====================================================

    def evaluate_eta_prediction(
        self,
        actual_wait_time: float,
        predicted_wait_time: float
    ):

        result = (
            self.confidence_manager
            .evaluate_prediction(
                prediction_type="ETA",
                actual=actual_wait_time,
                predicted=predicted_wait_time
            )
        )

        self.prediction_history.append(
            result
        )

        logger.info(
            "ETA confidence evaluated"
        )

        return result

    # =====================================================
    # EVALUATE CROWD PREDICTION
    # =====================================================

    def evaluate_crowd_prediction(
        self,
        actual_density: float,
        predicted_density: float
    ):

        result = (
            self.confidence_manager
            .evaluate_prediction(
                prediction_type="CROWD",
                actual=actual_density,
                predicted=predicted_density
            )
        )

        self.prediction_history.append(
            result
        )

        logger.info(
            "Crowd confidence evaluated"
        )

        return result

    # =====================================================
    # EVALUATE NO-SHOW PREDICTION
    # =====================================================

    def evaluate_no_show_prediction(
        self,
        actual_value: float,
        predicted_value: float
    ):

        result = (
            self.confidence_manager
            .evaluate_prediction(
                prediction_type="NO_SHOW",
                actual=actual_value,
                predicted=predicted_value
            )
        )

        self.prediction_history.append(
            result
        )

        logger.info(
            "No-show confidence evaluated"
        )

        return result

    # =====================================================
    # GET PREDICTION HISTORY
    # =====================================================

    def get_prediction_history(self):

        return self.prediction_history