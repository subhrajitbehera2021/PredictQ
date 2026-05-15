from statistics import mean

from ai_engine.utils.logging_utils import (
    get_logger
)


logger = get_logger(__name__)


class WaitTimePredictor:

    def __init__(self):

        self.default_consultation_time = 10

    def predict(
        self,
        queue_length: int,
        available_doctors: int,
        avg_consultation_time: int = None
    ):

        if avg_consultation_time is None:
            avg_consultation_time = self.default_consultation_time

        if available_doctors <= 0:
            logger.warning("No available doctors detected")
            return -1

        total_minutes = (
            queue_length * avg_consultation_time
        ) / available_doctors

        return round(total_minutes, 2)

    def predict_wait_time(
        self,
        queue_size: int,
        available_doctors: int,
        avg_consultation_time: int = None
    ):

        return self.predict(
            queue_length=queue_size,
            available_doctors=available_doctors,
            avg_consultation_time=avg_consultation_time
        )

    def calculate_average_consultation(
        self,
        consultation_history: list
    ):

        if not consultation_history:
            return self.default_consultation_time

        return round(mean(consultation_history), 2)