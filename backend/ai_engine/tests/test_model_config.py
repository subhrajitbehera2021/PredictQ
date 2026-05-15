from ai_engine.configs.model_config import (
    ModelConfig
)


def test_model_names():

    assert (
        ModelConfig.ETA_MODEL_NAME
        == "eta_prediction_model"
    )

    assert (
        ModelConfig.CROWD_MODEL_NAME
        == "crowd_density_model"
    )


def test_model_version():

    assert (
        ModelConfig.MODEL_VERSION
        == "1.0.0"
    )


def test_retraining_settings():

    assert (
        ModelConfig.ENABLE_AUTO_RETRAINING
        is True
    )

    assert (
        ModelConfig.RETRAINING_THRESHOLD
        == 60
    )


def test_inference_settings():

    assert (
        ModelConfig.ENABLE_REALTIME_INFERENCE
        is True
    )

    assert (
        ModelConfig.MAX_INFERENCE_TIME_MS
        == 500
    )