class WaitTimeEngine:

    @staticmethod
    def estimate_wait_time(
        queue_position,
        avg_consult_time=10
    ):

        return queue_position * avg_consult_time