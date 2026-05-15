from ai_engine.utils.logging_utils import (
    get_logger
)


logger = get_logger(__name__)


class QueueOptimizer:

    # =====================================================
    # OPTIMIZE QUEUE
    # =====================================================

    def optimize(
        self,
        queue: list
    ):

        optimized_queue = sorted(
            queue,
            key=lambda patient: (
                -patient.get("priority", 1),
                patient.get("created_at", "")
            )
        )

        logger.info(
            f"Queue optimized | "
            f"Total Patients: {len(optimized_queue)}"
        )

        return optimized_queue

    # =====================================================
    # GET NEXT PATIENT
    # =====================================================

    def get_next_patient(
        self,
        queue: list
    ):

        if not queue:

            logger.warning(
                "Attempted next patient retrieval "
                "from empty queue"
            )

            return None

        optimized_queue = self.optimize(
            queue
        )

        next_patient = optimized_queue[0]

        logger.info(
            f"Next patient selected: "
            f"{next_patient.get('patient_id')}"
        )

        return next_patient