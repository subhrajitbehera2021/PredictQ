class ModelConfig:

    # =====================================================
    # MODEL IDENTIFIERS
    # =====================================================

    ETA_MODEL_NAME = (
        "eta_prediction_model"
    )

    CROWD_MODEL_NAME = (
        "crowd_density_model"
    )

    NO_SHOW_MODEL_NAME = (
        "no_show_prediction_model"
    )

    LOAD_FORECAST_MODEL_NAME = (
        "hospital_load_model"
    )

    # =====================================================
    # MODEL VERSIONING
    # =====================================================

    MODEL_VERSION = "1.0.0"

    ENABLE_MODEL_VERSIONING = True

    # =====================================================
    # STORAGE SETTINGS
    # =====================================================

    MODEL_STORAGE_PATH = (
        "trained_models"
    )

    CHECKPOINT_PATH = (
        "trained_models/checkpoints"
    )

    # =====================================================
    # RETRAINING SETTINGS
    # =====================================================

    ENABLE_AUTO_RETRAINING = True

    RETRAINING_THRESHOLD = 60

    MAX_RETRAINING_ATTEMPTS = 3

    # =====================================================
    # INFERENCE SETTINGS
    # =====================================================

    ENABLE_REALTIME_INFERENCE = True

    MAX_INFERENCE_TIME_MS = 500

    ENABLE_BATCH_INFERENCE = True

    # =====================================================
    # CONFIDENCE SETTINGS
    # =====================================================

    MINIMUM_CONFIDENCE_SCORE = 60

    HIGH_CONFIDENCE_SCORE = 85

    # =====================================================
    # DRIFT SETTINGS
    # =====================================================

    ENABLE_DRIFT_MONITORING = True

    DRIFT_THRESHOLD = 30

    # =====================================================
    # FALLBACK SETTINGS
    # =====================================================

    ENABLE_FALLBACK_MODELS = True

    FALLBACK_MODEL_TYPE = (
        "RULE_BASED"
    )

    # =====================================================
    # PERFORMANCE SETTINGS
    # =====================================================

    ENABLE_PERFORMANCE_TRACKING = True

    ENABLE_MODEL_BENCHMARKING = True

    # =====================================================
    # LOGGING SETTINGS
    # =====================================================

    ENABLE_MODEL_LOGGING = True

    LOG_PREDICTIONS = True