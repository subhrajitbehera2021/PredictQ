from ai_engine.ml.preprocessing.data_cleaning import (
    DataCleaning
)

from ai_engine.ml.evaluation.validation_metrics import (
    ValidationMetrics
)

from ai_engine.ml.utils.model_saver import (
    ModelSaver
)

from ai_engine.utils.logging_utils import (
    get_logger
)


logger = get_logger(__name__)


class DummyModel:

    def __init__(self):
        self.trained = False

    def fit(
        self,
        features,
        targets
    ):
        self.trained = True

    def predict(
        self,
        data
    ):
        return [30 for _ in data]


class TrainingPipeline:

    def __init__(self):

        self.cleaner = DataCleaning()
        self.validation_metrics = ValidationMetrics()
        self.model_saver = ModelSaver()
        self.training_history = []

    def train_eta_model(
        self,
        dataset: list
    ):

        cleaned_dataset = self.cleaner.clean_dataset(
            dataset,
            duplicate_key="queue_size"
        )

        features = [
            [
                row.get("queue_size", 0),
                row.get("available_doctors", 1),
                row.get("patient_priority", 1)
            ]
            for row in cleaned_dataset
        ]

        targets = [
            row.get("wait_time", 30)
            for row in cleaned_dataset
        ]

        model = DummyModel()

        model.fit(
            features,
            targets
        )

        predictions = model.predict(
            features
        )

        validation_report = (
            self.validation_metrics.generate_validation_report(
                targets,
                predictions
            )
        )

        saved_model_path = (
            self.model_saver.save_model(
                model,
                "eta_model",
                "trained_models"
            )
        )

        result = {
            "model_trained": True,
            "samples": len(cleaned_dataset),
            "validation": validation_report,
            "model_path": saved_model_path
        }

        self.training_history.append(
            result
        )

        logger.info(
            "ETA training pipeline completed"
        )

        return result

    def get_training_history(self):

        return self.training_history