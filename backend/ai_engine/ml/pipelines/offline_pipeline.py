from ai_engine.ml.preprocessing.data_cleaning import (
    DataCleaning
)

from ai_engine.ml.preprocessing.feature_engineering import (
    FeatureEngineering
)

from ai_engine.ml.preprocessing.dataset_builder import (
    DatasetBuilder
)

from ai_engine.analytics_ai.queue_analytics_engine import (
    QueueAnalyticsEngine
)

from ai_engine.utils.logging_utils import (
    get_logger
)


logger = get_logger(__name__)


class OfflinePipeline:

    def __init__(self):

        self.cleaner = DataCleaning()
        self.feature_engineering = FeatureEngineering()
        self.dataset_builder = DatasetBuilder()
        self.queue_analytics = QueueAnalyticsEngine()
        self.pipeline_history = []

    def process_historical_data(
        self,
        raw_dataset: list,
        duplicate_key: str = "patient_id"
    ):

        cleaned_dataset = self.cleaner.clean_dataset(
            raw_dataset,
            duplicate_key=duplicate_key
        )

        feature_records = []

        for record in cleaned_dataset:

            feature_set = (
                self.feature_engineering
                .generate_feature_set(
                    record,
                    record
                )
            )

            feature_records.append(
                feature_set
            )

        training_dataset = (
            self.dataset_builder
            .build_training_dataset(
                feature_records
            )
        )

        queue_analytics = (
            self.queue_analytics
            .analyze_queue_size(
                cleaned_dataset
            )
        )

        result = {
            "cleaned_records": len(cleaned_dataset),
            "feature_records": feature_records,
            "training_dataset": training_dataset,
            "queue_analytics": queue_analytics
        }

        self.pipeline_history.append(
            result
        )

        logger.info(
            "Offline historical pipeline completed"
        )

        return result

    def get_pipeline_history(self):

        return self.pipeline_history