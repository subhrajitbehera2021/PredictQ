from ai_engine.utils.logging_utils import (
    get_logger
)


logger = get_logger(__name__)


class NoShowPredictor:

    def __init__(self):

        self.prediction_history = []

    # =====================================================
    # PREDICT NO-SHOW RISK
    # =====================================================

    def predict_no_show(
        self,
        previous_no_shows: int,
        travel_distance_km: float,
        waiting_time_minutes: int
    ):

        risk_score = 0

        # PREVIOUS HISTORY
        risk_score += (
            previous_no_shows * 20
        )

        # DISTANCE FACTOR
        if travel_distance_km >= 20:
            risk_score += 25

        elif travel_distance_km >= 10:
            risk_score += 15

        # WAITING TIME FACTOR
        if waiting_time_minutes >= 120:
            risk_score += 25

        elif waiting_time_minutes >= 60:
            risk_score += 10

        risk_score = min(risk_score, 100)

        # RISK LEVEL
        if risk_score >= 70:

            risk_level = "HIGH"

        elif risk_score >= 40:

            risk_level = "MEDIUM"

        else:

            risk_level = "LOW"

        prediction = {

            "risk_score":
            risk_score,

            "risk_level":
            risk_level,

            "previous_no_shows":
            previous_no_shows,

            "travel_distance_km":
            travel_distance_km,

            "waiting_time_minutes":
            waiting_time_minutes
        }

        self.prediction_history.append(
            prediction
        )

        logger.info(
            f"No-show risk predicted: "
            f"{risk_level}"
        )

        return prediction

    # =====================================================
    # GET PREDICTION HISTORY
    # =====================================================

    def get_prediction_history(self):

        return self.prediction_history

    # =====================================================
    # RESET HISTORY
    # =====================================================

    def reset_history(self):

        self.prediction_history = []

        logger.info(
            "No-show prediction history reset"
        )