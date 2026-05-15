from math import sqrt

from ai_engine.utils.logging_utils import (
    get_logger
)


logger = get_logger(__name__)


class ValidationMetrics:

    def __init__(self):

        self.metrics_history = []

    # =====================================================
    # MEAN ABSOLUTE ERROR
    # =====================================================

    def calculate_mae(
        self,
        actual: list,
        predicted: list
    ):

        if not actual or not predicted:
            return 0

        total_error = 0

        for a, p in zip(
            actual,
            predicted
        ):

            total_error += abs(a - p)

        mae = total_error / len(actual)

        return round(mae, 4)

    # =====================================================
    # MEAN SQUARED ERROR
    # =====================================================

    def calculate_mse(
        self,
        actual: list,
        predicted: list
    ):

        if not actual or not predicted:
            return 0

        total_error = 0

        for a, p in zip(
            actual,
            predicted
        ):

            total_error += (
                (a - p) ** 2
            )

        mse = total_error / len(actual)

        return round(mse, 4)

    # =====================================================
    # ROOT MEAN SQUARED ERROR
    # =====================================================

    def calculate_rmse(
        self,
        actual: list,
        predicted: list
    ):

        mse = self.calculate_mse(
            actual,
            predicted
        )

        rmse = sqrt(mse)

        return round(rmse, 4)

    # =====================================================
    # SIMPLE ACCURACY
    # =====================================================

    def calculate_accuracy(
        self,
        actual: list,
        predicted: list
    ):

        if not actual or not predicted:
            return 0

        correct = 0

        for a, p in zip(
            actual,
            predicted
        ):

            if a == p:
                correct += 1

        accuracy = (
            correct / len(actual)
        ) * 100

        return round(accuracy, 2)

    # =====================================================
    # COMPLETE VALIDATION REPORT
    # =====================================================

    def generate_validation_report(
        self,
        actual: list,
        predicted: list
    ):

        report = {

            "mae":
            self.calculate_mae(
                actual,
                predicted
            ),

            "mse":
            self.calculate_mse(
                actual,
                predicted
            ),

            "rmse":
            self.calculate_rmse(
                actual,
                predicted
            ),

            "accuracy":
            self.calculate_accuracy(
                actual,
                predicted
            )
        }

        self.metrics_history.append(
            report
        )

        logger.info(
            "Validation report generated"
        )

        return report

    # =====================================================
    # GET METRIC HISTORY
    # =====================================================

    def get_metrics_history(self):

        return self.metrics_history