from ai_engine.utils.logging_utils import (
    get_logger
)

from ai_engine.utils.time_utils import (
    TimeUtils
)


logger = get_logger(__name__)


class PerformanceTracker:

    def __init__(self):

        self.metrics = []

    def record_metric(
        self,
        metric_name: str,
        value: float,
        category: str = "GENERAL"
    ):

        metric = {
            "metric_name": metric_name,
            "value": value,
            "category": category,
            "timestamp": str(TimeUtils.now())
        }

        self.metrics.append(metric)

        logger.info(
            f"Performance metric recorded: {metric_name}"
        )

        return metric

    def record_queue_operation_time(
        self,
        operation_name: str,
        duration_ms: float
    ):

        return self.record_metric(
            metric_name=operation_name,
            value=duration_ms,
            category="QUEUE_OPERATION"
        )

    def record_prediction_time(
        self,
        model_name: str,
        duration_ms: float
    ):

        return self.record_metric(
            metric_name=model_name,
            value=duration_ms,
            category="PREDICTION"
        )

    def get_metrics(self):

        return self.metrics

    def get_metrics_by_category(
        self,
        category: str
    ):

        return [
            metric
            for metric in self.metrics
            if metric["category"] == category
        ]

    def calculate_average_metric(
        self,
        category: str
    ):

        filtered_metrics = self.get_metrics_by_category(
            category
        )

        if not filtered_metrics:
            return 0

        total = sum(
            metric["value"]
            for metric in filtered_metrics
        )

        return round(
            total / len(filtered_metrics),
            2
        )

    def clear_metrics(self):

        self.metrics = []

        logger.info(
            "Performance metrics cleared"
        )