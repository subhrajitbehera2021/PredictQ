from ai_engine.utils.logging_utils import (
    get_logger
)


logger = get_logger(__name__)


class CrowdInference:

    def __init__(self, model=None):

        self.model = model
        self.inference_history = []

    def load_model(
        self,
        model
    ):

        self.model = model

        logger.info(
            "Crowd inference model loaded"
        )

        return True

    def predict_crowd(
        self,
        features: dict
    ):

        if self.model is None:

            density = self._rule_based_crowd(
                features
            )

            source = "RULE_BASED"

        else:

            density = self.model.predict([
                [
                    features.get("patient_count", 0),
                    features.get("room_capacity", 1),
                    features.get("doctor_count", 1)
                ]
            ])[0]

            source = "ML_MODEL"

        density = min(
            max(float(density), 0),
            100
        )

        if density >= 90:
            crowd_level = "CRITICAL"

        elif density >= 70:
            crowd_level = "HIGH"

        elif density >= 40:
            crowd_level = "MEDIUM"

        else:
            crowd_level = "LOW"

        result = {
            "density_percentage": round(density, 2),
            "crowd_level": crowd_level,
            "features": features,
            "source": source
        }

        self.inference_history.append(
            result
        )

        logger.info(
            f"Crowd predicted: {crowd_level}"
        )

        return result

    def _rule_based_crowd(
        self,
        features: dict
    ):

        patient_count = features.get(
            "patient_count",
            0
        )

        room_capacity = max(
            features.get(
                "room_capacity",
                1
            ),
            1
        )

        density = (
            patient_count
            / room_capacity
        ) * 100

        return density

    def get_inference_history(self):

        return self.inference_history

    def clear_history(self):

        self.inference_history = []

        logger.info(
            "Crowd inference history cleared"
        )