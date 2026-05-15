from ai_engine.utils.logging_utils import (
    get_logger
)


logger = get_logger(__name__)


class ETAInference:

    def __init__(self, model=None):

        self.model = model
        self.inference_history = []

    def load_model(
        self,
        model
    ):

        self.model = model

        logger.info(
            "ETA inference model loaded"
        )

        return True

    def predict_eta(
        self,
        features: dict
    ):

        if self.model is None:

            eta = self._rule_based_eta(
                features
            )

        else:

            eta = self.model.predict([
                [
                    features.get("queue_size", 0),
                    features.get("available_doctors", 1),
                    features.get("patient_priority", 1),
                    features.get("symptoms_count", 0)
                ]
            ])[0]

        result = {
            "eta_minutes": round(float(eta), 2),
            "features": features,
            "source": (
                "ML_MODEL"
                if self.model is not None
                else "RULE_BASED"
            )
        }

        self.inference_history.append(
            result
        )

        logger.info(
            f"ETA predicted: {result['eta_minutes']} minutes"
        )

        return result

    def _rule_based_eta(
        self,
        features: dict
    ):

        queue_size = features.get(
            "queue_size",
            0
        )

        available_doctors = max(
            features.get(
                "available_doctors",
                1
            ),
            1
        )

        patient_priority = features.get(
            "patient_priority",
            1
        )

        symptoms_count = features.get(
            "symptoms_count",
            0
        )

        base_eta = (
            queue_size * 10
        ) / available_doctors

        priority_adjustment = max(
            0,
            5 - patient_priority
        )

        symptoms_adjustment = (
            symptoms_count * 2
        )

        eta = (
            base_eta
            + priority_adjustment
            + symptoms_adjustment
        )

        return eta

    def get_inference_history(self):

        return self.inference_history

    def clear_history(self):

        self.inference_history = []

        logger.info(
            "ETA inference history cleared"
        )