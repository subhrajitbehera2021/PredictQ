from ai_engine.utils.logging_utils import (
    get_logger
)


logger = get_logger(__name__)


class FailSafeEngine:

    def __init__(self):

        self.fail_safe_events = []

    def handle_prediction_failure(
        self,
        fallback_wait_time: int = 10
    ):

        event = {
            "type": "PREDICTION_FAILURE",
            "fallback_wait_time": fallback_wait_time,
            "action": "USED_DEFAULT_WAIT_TIME"
        }

        self.fail_safe_events.append(event)

        logger.warning(
            "Prediction failed. Default wait time used."
        )

        return event

    def handle_realtime_failure(self):

        event = {
            "type": "REALTIME_FAILURE",
            "action": "SWITCH_TO_POLLING_MODE"
        }

        self.fail_safe_events.append(event)

        logger.warning(
            "Realtime failure detected. Switching to polling mode."
        )

        return event

    def handle_doctor_unavailable(self):

        event = {
            "type": "DOCTOR_UNAVAILABLE",
            "action": "KEEP_PATIENT_IN_QUEUE"
        }

        self.fail_safe_events.append(event)

        logger.warning(
            "No doctor available. Patient remains in queue."
        )

        return event

    def handle_queue_overflow(self):

        event = {
            "type": "QUEUE_OVERFLOW",
            "action": "TRIGGER_ADMIN_ALERT"
        }

        self.fail_safe_events.append(event)

        logger.warning(
            "Queue overflow detected. Admin alert triggered."
        )

        return event

    def get_fail_safe_events(self):

        return self.fail_safe_events

    def reset(self):

        self.fail_safe_events = []

        logger.info(
            "Fail-safe events reset"
        )