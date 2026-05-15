from ai_engine.utils.logging_utils import (
    get_logger
)


logger = get_logger(__name__)


class DegradedModeManager:

    def __init__(self):

        self.degraded_mode = False

        self.reason = None

    def activate_degraded_mode(
        self,
        reason: str
    ):

        self.degraded_mode = True
        self.reason = reason

        logger.warning(
            f"Degraded mode activated: {reason}"
        )

        return {
            "degraded_mode": self.degraded_mode,
            "reason": self.reason,
            "allowed_features": self.get_allowed_features()
        }

    def deactivate_degraded_mode(self):

        self.degraded_mode = False
        self.reason = None

        logger.info(
            "Degraded mode deactivated"
        )

        return {
            "degraded_mode": self.degraded_mode,
            "reason": self.reason
        }

    def is_degraded(self):

        return self.degraded_mode

    def get_allowed_features(self):

        if self.degraded_mode:

            return [
                "REGISTER_PATIENT",
                "VIEW_QUEUE",
                "CALL_NEXT_PATIENT",
                "MANUAL_WAIT_TIME"
            ]

        return [
            "REGISTER_PATIENT",
            "VIEW_QUEUE",
            "CALL_NEXT_PATIENT",
            "REALTIME_SYNC",
            "AI_PREDICTION",
            "ANALYTICS",
            "AUTO_DECISION"
        ]

    def get_status(self):

        return {
            "degraded_mode": self.degraded_mode,
            "reason": self.reason,
            "allowed_features": self.get_allowed_features()
        }   