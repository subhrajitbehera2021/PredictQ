from ai_engine.ml.evaluation.validation_metrics import (
    ValidationMetrics
)

from ai_engine.utils.logging_utils import (
    get_logger
)


logger = get_logger(__name__)


class ModelBenchmark:

    def __init__(self):

        self.metrics = ValidationMetrics()
        self.benchmark_history = []

    def benchmark_model(
        self,
        model_name: str,
        actual: list,
        predicted: list
    ):

        report = self.metrics.generate_validation_report(
            actual,
            predicted
        )

        benchmark = {
            "model_name": model_name,
            "metrics": report
        }

        self.benchmark_history.append(
            benchmark
        )

        logger.info(
            f"Model benchmark completed: {model_name}"
        )

        return benchmark

    def compare_models(
        self,
        benchmarks: list
    ):

        if not benchmarks:
            return None

        best_model = min(
            benchmarks,
            key=lambda item: item["metrics"]["rmse"]
        )

        logger.info(
            f"Best model selected: {best_model['model_name']}"
        )

        return best_model

    def get_benchmark_history(self):

        return self.benchmark_history