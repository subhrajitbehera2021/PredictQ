from ai_engine.utils.queue_utils import QueueUtils


class QueueTimeEstimator:

    def estimate(self, queue_position: int, avg_consultation_time: int):
        return QueueUtils.calculate_eta(
            queue_position,
            avg_consultation_time
        )