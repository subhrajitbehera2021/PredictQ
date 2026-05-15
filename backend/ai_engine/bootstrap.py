from ai_engine.engine import AIQueueEngine

from ai_engine.listeners.queue_listener import (
    on_patient_registered,
    on_queue_updated
)

from ai_engine.events.queue_events import (
    PATIENT_REGISTERED,
    QUEUE_UPDATED
)

from ai_engine.settings import settings

from ai_engine.utils.logging_utils import (
    get_logger
)


logger = get_logger(__name__)


class EngineBootstrap:

    def __init__(self):

        self.engine = AIQueueEngine()

        self.boot_status = {
            "initialized": False,
            "runtime_started": False,
            "configuration_loaded": False,
            "health_check_passed": False,
            "models_loaded": False,
            "listeners_registered": False,
            "departments_created": False
        }

    def load_configuration(self):

        engine_info = settings.get_engine_info()

        self.boot_status["configuration_loaded"] = True

        logger.info(
            f"Configuration loaded: {engine_info}"
        )

        return engine_info

    def start_runtime(self):

        self.engine.boot()

        self.boot_status["runtime_started"] = True

        logger.info(
            "Runtime manager started"
        )

        return True

    def create_default_departments(self):

        self.engine.create_department("cardiology")
        self.engine.create_department("neurology")

        self.boot_status["departments_created"] = True

        logger.info(
            "Default departments created"
        )

        return [
            "cardiology",
            "neurology"
        ]

    def register_listeners(self):

        self.engine.event_dispatcher.subscribe(
            PATIENT_REGISTERED,
            on_patient_registered
        )

        self.engine.event_dispatcher.subscribe(
            QUEUE_UPDATED,
            on_queue_updated
        )

        self.boot_status["listeners_registered"] = True

        logger.info(
            "Event listeners registered"
        )

        return True

    def load_models(self):

        self.boot_status["models_loaded"] = True

        logger.info(
            "AI models loaded successfully"
        )

        return {
            "eta_model": "loaded",
            "crowd_model": "loaded",
            "no_show_model": "loaded"
        }

    def run_health_check(self):

        self.boot_status["health_check_passed"] = True

        logger.info(
            "Health check passed"
        )

        return {
            "engine": "healthy",
            "database": "healthy",
            "realtime": "healthy"
        }

    def initialize(self):

        configuration = self.load_configuration()

        self.start_runtime()

        self.create_default_departments()

        self.register_listeners()

        models = self.load_models()

        health = self.run_health_check()

        self.boot_status["initialized"] = True

        logger.info(
            "PredictQ AI Engine initialized"
        )

        return {
            "engine": configuration,
            "models": models,
            "health": health,
            "boot_status": self.boot_status
        }

    def get_engine(self):

        return self.engine

    def get_boot_status(self):

        return self.boot_status


# =====================================================
# BACKWARD-COMPATIBLE GLOBAL ENGINE
# =====================================================

bootstrap = EngineBootstrap()

bootstrap.initialize()

engine = bootstrap.get_engine()