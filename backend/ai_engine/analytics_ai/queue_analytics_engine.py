from statistics import mean

from ai_engine.utils.logging_utils import (
    get_logger
)


logger = get_logger(__name__)


class QueueAnalyticsEngine:

    def __init__(self):

        self.analytics_cache = {}

    # =====================================================
    # QUEUE SIZE ANALYTICS
    # =====================================================

    def analyze_queue_size(
        self,
        queue: list
    ):

        queue_size = len(queue)

        logger.info(
            f"Queue size analyzed: "
            f"{queue_size}"
        )

        return {
            "queue_size": queue_size
        }

    # =====================================================
    # PRIORITY DISTRIBUTION
    # =====================================================

    def analyze_priority_distribution(
        self,
        queue: list
    ):

        distribution = {}

        for patient in queue:

            priority = patient.get(
                "priority",
                1
            )

            distribution[priority] = (
                distribution.get(priority, 0)
                + 1
            )

        logger.info(
            "Priority distribution analyzed"
        )

        return distribution

    # =====================================================
    # AVERAGE WAIT ANALYTICS
    # =====================================================

    def analyze_average_wait(
        self,
        wait_times: list
    ):

        if not wait_times:

            return {
                "average_wait": 0
            }

        average_wait = round(
            mean(wait_times),
            2
        )

        logger.info(
            f"Average wait analyzed: "
            f"{average_wait}"
        )

        return {
            "average_wait": average_wait
        }

    # =====================================================
    # DEPARTMENT ANALYTICS
    # =====================================================

    def analyze_department(
        self,
        department: str,
        queue: list,
        wait_times: list
    ):

        analytics = {
            "department": department,
            "queue": self.analyze_queue_size(
                queue
            ),
            "priority_distribution": (
                self.analyze_priority_distribution(
                    queue
                )
            ),
            "wait_metrics": (
                self.analyze_average_wait(
                    wait_times
                )
            )
        }

        self.analytics_cache[
            department
        ] = analytics

        logger.info(
            f"Department analytics completed "
            f"for {department}"
        )

        return analytics

    # =====================================================
    # GET CACHED ANALYTICS
    # =====================================================

    def get_cached_analytics(
        self,
        department: str
    ):

        return self.analytics_cache.get(
            department,
            {}
        )