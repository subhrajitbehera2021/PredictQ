import os
from dataclasses import dataclass


@dataclass
class EngineSettings:

    # =====================================================
    # ENGINE
    # =====================================================

    ENGINE_NAME: str = (
        "PredictQ AI Engine"
    )

    ENGINE_VERSION: str = (
        "1.0.0"
    )

    # =====================================================
    # ENVIRONMENT
    # =====================================================

    ENVIRONMENT: str = os.getenv(
        "PREDICTQ_ENV",
        "development"
    )

    DEBUG: bool = (
        os.getenv(
            "PREDICTQ_DEBUG",
            "true"
        ).lower() == "true"
    )

    # =====================================================
    # QUEUE SETTINGS
    # =====================================================

    MAX_QUEUE_SIZE: int = 500

    DEFAULT_CONSULTATION_MINUTES: int = 10

    DEFAULT_WAIT_TIME: int = 20

    # =====================================================
    # FEATURE FLAGS
    # =====================================================

    ENABLE_REALTIME: bool = True

    ENABLE_AI_PREDICTION: bool = True

    ENABLE_MONITORING: bool = True

    ENABLE_DRIFT_DETECTION: bool = True

    ENABLE_AUTO_RETRAINING: bool = True

    ENABLE_FALLBACK_MODE: bool = True

    # =====================================================
    # THRESHOLDS
    # =====================================================

    DEFAULT_CONFIDENCE_THRESHOLD: int = 60

    DEFAULT_DRIFT_THRESHOLD: int = 30

    CRITICAL_QUEUE_THRESHOLD: int = 200

    # =====================================================
    # MODEL STORAGE
    # =====================================================

    MODEL_STORAGE_PATH: str = (
        "trained_models"
    )

    ETA_MODEL_PATH: str = (
        "trained_models/eta_model.pkl"
    )

    CROWD_MODEL_PATH: str = (
        "trained_models/crowd_model.pkl"
    )

    NO_SHOW_MODEL_PATH: str = (
        "trained_models/no_show_model.pkl"
    )

    # =====================================================
    # DATABASE
    # =====================================================

    DATABASE_URL: str = os.getenv(
        "DATABASE_URL",
        "memory://local"
    )

    # =====================================================
    # LOGGING
    # =====================================================

    LOG_LEVEL: str = os.getenv(
        "LOG_LEVEL",
        "INFO"
    )

    # =====================================================
    # HELPERS
    # =====================================================

    def is_production(self):

        return (
            self.ENVIRONMENT
            == "production"
        )

    def is_development(self):

        return (
            self.ENVIRONMENT
            == "development"
        )

    def get_engine_info(self):

        return {
            "name":
            self.ENGINE_NAME,

            "version":
            self.ENGINE_VERSION,

            "environment":
            self.ENVIRONMENT,

            "debug":
            self.DEBUG
        }


settings = EngineSettings()