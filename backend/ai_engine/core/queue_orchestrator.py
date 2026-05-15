from ai_engine.queue_ai.queue_optimizer import QueueOptimizer
from ai_engine.queue_ai.queue_balancer import QueueBalancer

from ai_engine.utils.logging_utils import (
    get_logger
)


logger = get_logger(__name__)


class QueueOrchestrator:

    def __init__(
        self,
        state_manager,
        queue_builder
    ):

        self.state_manager = state_manager
        self.queue_builder = queue_builder

        self.queue_optimizer = QueueOptimizer()
        self.queue_balancer = QueueBalancer()

    def enqueue_patient(
        self,
        department: str,
        patient_data: dict
    ):

        queue = self.queue_builder.enqueue_patient(
            department,
            patient_data
        )

        optimized_queue = self.queue_optimizer.optimize(
            queue
        )

        self.state_manager.departments[department] = (
            optimized_queue
        )

        logger.info(
            f"Patient enqueued through orchestrator: "
            f"{patient_data.get('patient_id')}"
        )

        return optimized_queue

    def call_next_patient(
        self,
        department: str
    ):

        queue = self.state_manager.get_department_queue(
            department
        )

        next_patient = (
            self.queue_optimizer.get_next_patient(queue)
        )

        if next_patient is None:
            return None

        self.state_manager.remove_patient(
            department,
            next_patient["patient_id"]
        )

        logger.info(
            f"Next patient called through orchestrator: "
            f"{next_patient.get('patient_id')}"
        )

        return next_patient

    def get_queue_status(
        self,
        department: str
    ):

        queue = self.state_manager.get_department_queue(
            department
        )

        return {
            "department": department,
            "queue_size": len(queue),
            "patients": queue
        }

    def get_system_balance(self):

        return self.queue_balancer.balance_departments(
            self.state_manager.departments
        )