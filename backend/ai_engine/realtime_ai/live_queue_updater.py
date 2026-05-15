from copy import deepcopy

from ai_engine.utils.logging_utils import (
    get_logger
)


logger = get_logger(__name__)


class LiveQueueUpdater:

    def __init__(self):

        # {
        #   "cardiology": {...},
        #   "neurology": {...}
        # }

        self.live_queue_state = {}

    # =====================================================
    # UPDATE LIVE QUEUE
    # =====================================================

    def update_queue(
        self,
        department: str,
        queue_data: list
    ):

        self.live_queue_state[department] = {
            "department": department,
            "queue_size": len(queue_data),
            "patients": deepcopy(queue_data)
        }

        logger.info(
            f"Live queue updated for {department}"
        )

        return self.live_queue_state[department]

    # =====================================================
    # GET LIVE QUEUE
    # =====================================================

    def get_live_queue(
        self,
        department: str
    ):

        return self.live_queue_state.get(
            department,
            {
                "department": department,
                "queue_size": 0,
                "patients": []
            }
        )

    # =====================================================
    # GET ALL LIVE QUEUES
    # =====================================================

    def get_all_live_queues(self):

        return deepcopy(
            self.live_queue_state
        )

    # =====================================================
    # REMOVE DEPARTMENT
    # =====================================================

    def remove_department(
        self,
        department: str
    ):

        if department in self.live_queue_state:

            del self.live_queue_state[department]

            logger.info(
                f"Removed live queue for {department}"
            )

    # =====================================================
    # CLEAR ALL LIVE DATA
    # =====================================================

    def clear(self):

        self.live_queue_state.clear()

        logger.info(
            "All live queues cleared"
        )