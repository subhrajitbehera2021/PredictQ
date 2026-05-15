from ai_engine.ml.evaluation.model_benchmark import (
    ModelBenchmark
)


benchmark = ModelBenchmark()


def test_model_benchmark():

    result = benchmark.benchmark_model(
        "eta_dummy_model",
        actual=[10, 20, 30],
        predicted=[12, 19, 29]
    )

    assert result["model_name"] == "eta_dummy_model"
    assert "rmse" in result["metrics"]


def test_compare_models():

    model_a = benchmark.benchmark_model(
        "model_a",
        actual=[10, 20, 30],
        predicted=[12, 19, 29]
    )

    model_b = benchmark.benchmark_model(
        "model_b",
        actual=[10, 20, 30],
        predicted=[20, 30, 40]
    )

    best = benchmark.compare_models(
        [model_a, model_b]
    )

    assert best["model_name"] == "model_a"


def test_benchmark_history():

    history = benchmark.get_benchmark_history()

    assert len(history) >= 1