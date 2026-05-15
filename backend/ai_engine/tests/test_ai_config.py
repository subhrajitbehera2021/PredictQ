from ai_engine.configs.ai_config import (
    AIConfig
)


def test_eta_thresholds():

    assert (
        AIConfig.ETA_WARNING_THRESHOLD
        == 30
    )

    assert (
        AIConfig.ETA_CRITICAL_THRESHOLD
        == 60
    )


def test_confidence_thresholds():

    assert (
        AIConfig.HIGH_CONFIDENCE
        == 85
    )

    assert (
        AIConfig.MEDIUM_CONFIDENCE
        == 60
    )


def test_fallback_enabled():

    assert (
        AIConfig.ENABLE_FALLBACK_MODE
        is True
    )


def test_model_storage_path():

    assert (
        AIConfig.MODEL_STORAGE_PATH
        == "trained_models"
    )