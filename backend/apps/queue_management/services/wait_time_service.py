class WaitTimeService:

    @staticmethod
    def estimate_wait_time(position, avg_time=10):

        return (position - 1) * avg_time