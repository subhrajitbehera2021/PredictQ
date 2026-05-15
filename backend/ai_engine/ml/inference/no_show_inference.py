from ai_engine.utils.logging_utils import (
    get_logger
)


logger = get_logger(__name__)


class NoShowInference:

    def __init__(self, model=None):

        self.model = model
        self.inference_history = []

    def load_model(
        self,
        model
    ):

        self.model = model

        logger.info(
            "No-show inference model loaded"
        )

        return True

    def predict_no_show(
        self,
        features: dict
    ):

        if self.model is None:

            risk_score = self._rule_based_no_show(
                features
            )

            source = "RULE_BASED"

        else:

            risk_score = self.model.predict([
                [
                    features.get("previous_no_shows", 0),
                    features.get("travel_distance_km", 0),
                    features.get("waiting_time_minutes", 0)
                ]
            ])[0]

            source = "ML_MODEL"

        risk_score = min(
            max(float(risk_score), 0),
            100
        )

        if risk_score >= 70:
            risk_level = "HIGH"

        elif risk_score >= 40:
            risk_level = "MEDIUM"

        else:
            risk_level = "LOW"

        result = {
            "risk_score": round(risk_score, 2),
            "risk_level": risk_level,
            "features": features,
            "source": source
        }

        self.inference_history.append(
            result
        )

        logger.info(
            f"No-show predicted: {risk_level}"
        )

        return result

    def _rule_based_no_show(
        self,
        features: dict
    ):

        risk_score = 0

        risk_score += (
            features.get("previous_no_shows", 0)
            * 20
        )

        distance = features.get(
            "travel_distance_km",
            0
        )

        if distance >= 20:
            risk_score += 25

        elif distance >= 10:
            risk_score += 15

        waiting_time = features.get(
            "waiting_time_minutes",
            0
        )

        if waiting_time >= 120:
            risk_score += 25

        elif waiting_time >= 60:
            risk_score += 10

        return risk_score

    def get_inference_history(self):

        return self.inference_history

    def clear_history(self):

        self.inference_history = []

        logger.info(
            "No-show inference history cleared"
        )