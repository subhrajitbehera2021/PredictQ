class AIConfig:

    # =====================================================
    # ETA CONFIGURATION
    # =====================================================

    ETA_WARNING_THRESHOLD = 30

    ETA_CRITICAL_THRESHOLD = 60

    DEFAULT_WAIT_TIME = 20

    # =====================================================
    # CROWD DENSITY CONFIGURATION
    # =====================================================

    CROWD_LOW_LIMIT = 20

    CROWD_MEDIUM_LIMIT = 50

    CROWD_HIGH_LIMIT = 80

    # =====================================================
    # NO SHOW CONFIGURATION
    # =====================================================

    NO_SHOW_LOW_RISK = 20

    NO_SHOW_MEDIUM_RISK = 50

    NO_SHOW_HIGH_RISK = 80

    # =====================================================
    # CONFIDENCE CONFIGURATION
    # =====================================================

    HIGH_CONFIDENCE = 85

    MEDIUM_CONFIDENCE = 60

    LOW_CONFIDENCE = 40

    # =====================================================
    # FALLBACK CONFIGURATION
    # =====================================================

    ENABLE_FALLBACK_MODE = True

    FALLBACK_CONFIDENCE_THRESHOLD = 60

    # =====================================================
    # QUEUE CONFIGURATION
    # =====================================================

    MAX_QUEUE_SIZE = 500

    CRITICAL_QUEUE_SIZE = 200

    # =====================================================
    # DOCTOR CONFIGURATION
    # =====================================================

    MIN_AVAILABLE_DOCTORS = 1

    MAX_DOCTOR_LOAD = 50

    # =====================================================
    # SYSTEM CONFIGURATION
    # =====================================================

    ENABLE_REALTIME_MONITORING = True

    ENABLE_PREDICTION_MONITORING = True

    ENABLE_DRIFT_DETECTION = True

    ENABLE_AUTO_RETRAINING = True

    # =====================================================
    # MODEL CONFIGURATION
    # =====================================================

    MODEL_VERSION = "1.0.0"

    MODEL_STORAGE_PATH = (
        "trained_models"
    )

    # =====================================================
    # LOGGING CONFIGURATION
    # =====================================================

    ENABLE_AI_LOGGING = True

    LOG_LEVEL = "INFO"