from ai_engine.utils.logging_utils import (
    get_logger
)


logger = get_logger(__name__)


class DriftDetector:

    def __init__(self):

        self.reference_mean = None
        self.drift_history = []

    # =====================================================
    # SET REFERENCE DATA
    # =====================================================

    def set_reference_data(
        self,
        dataset: list
    ):

        if not dataset:
            return 0

        self.reference_mean = (
            sum(dataset) / len(dataset)
        )

        logger.info(
            f"Reference mean set: "
            f"{self.reference_mean}"
        )

        return self.reference_mean

    # =====================================================
    # DETECT DRIFT
    # =====================================================

    def detect_drift(
        self,
        new_dataset: list,
        threshold: float = 20
    ):

        if self.reference_mean is None:

            raise ValueError(
                "Reference data not initialized"
            )

        if not new_dataset:
            return {
                "drift_detected": False,
                "drift_percentage": 0
            }

        new_mean = (
            sum(new_dataset)
            / len(new_dataset)
        )

        drift_percentage = abs(
            (
                new_mean
                - self.reference_mean
            )
            / self.reference_mean
        ) * 100

        drift_detected = (
            drift_percentage >= threshold
        )

        result = {
            "reference_mean":
            round(
                self.reference_mean,
                2
            ),

            "new_mean":
            round(
                new_mean,
                2
            ),

            "drift_percentage":
            round(
                drift_percentage,
                2
            ),

            "drift_detected":
            drift_detected
        }

        self.drift_history.append(
            result
        )

        logger.info(
            f"Drift analysis completed: "
            f"{drift_percentage:.2f}%"
        )

        return result

    # =====================================================
    # GET DRIFT HISTORY
    # =====================================================

    def get_drift_history(self):

        return self.drift_history