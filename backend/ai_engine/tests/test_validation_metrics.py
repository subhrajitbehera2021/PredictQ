from ai_engine.ml.evaluation.validation_metrics import (
    ValidationMetrics
)


metrics = ValidationMetrics()


actual = [10, 20, 30, 40]
predicted = [12, 18, 29, 41]


def test_mae():

    mae = metrics.calculate_mae(
        actual,
        predicted
    )

    assert mae > 0


def test_rmse():

    rmse = metrics.calculate_rmse(
        actual,
        predicted
    )

    assert rmse > 0


def test_validation_report():

    report = (
        metrics.generate_validation_report(
            actual,
            predicted
        )
    )

    assert "mae" in report
    assert "rmse" in report