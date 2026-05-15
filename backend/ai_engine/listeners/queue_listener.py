from ai_engine.utils.logging_utils import (
    get_logger
)

logger = get_logger(__name__)


def on_patient_registered(payload):

    logger.info(
        f"New patient registered: "
        f"{payload['patient_id']}"
    )


def on_queue_updated(payload):

    logger.info(
        f"Queue updated for "
        f"{payload['department']} | "
        f"Queue Size: {payload['queue_size']}"
    )