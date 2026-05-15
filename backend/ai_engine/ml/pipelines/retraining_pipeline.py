from ai_engine.ml.evaluation.drift_detector import (
    DriftDetector
)

from ai_engine.ml.pipelines.training_pipeline import (
    TrainingPipeline
)

from ai_engine.utils.logging_utils import (
    get_logger
)


logger = get_logger(__name__)


class RetrainingPipeline:

    def __init__(self):

        self.drift_detector = DriftDetector()
        self.training_pipeline = TrainingPipeline()
        self.retraining_history = []

    def initialize_reference_data(
        self,
        reference_values: list
    ):

        reference_mean = (
            self.drift_detector.set_reference_data(
                reference_values
            )
        )

        logger.info(
            "Reference data initialized for retraining"
        )

        return reference_mean

    def should_retrain(
        self,
        new_values: list,
        threshold: float = 20
    ):

        drift_report = (
            self.drift_detector.detect_drift(
                new_values,
                threshold
            )
        )

        return drift_report

    def retrain_if_needed(
        self,
        new_values: list,
        training_dataset: list,
        threshold: float = 20
    ):

        drift_report = self.should_retrain(
            new_values,
            threshold
        )

        if drift_report["drift_detected"] is False:

            result = {
                "retrained": False,
                "reason": "NO_DRIFT_DETECTED",
                "drift_report": drift_report
            }

            self.retraining_history.append(
                result
            )

            logger.info(
                "Retraining skipped. No drift detected."
            )

            return result

        training_result = (
            self.training_pipeline.train_eta_model(
                training_dataset
            )
        )

        result = {
            "retrained": True,
            "reason": "DRIFT_DETECTED",
            "drift_report": drift_report,
            "training_result": training_result
        }

        self.retraining_history.append(
            result
        )

        logger.info(
            "Model retraining completed after drift detection"
        )

        return result

    def get_retraining_history(self):

        return self.retraining_history