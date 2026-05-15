from ai_engine.utils.queue_utils import QueueUtils


class QueueBuilder:

    def __init__(self, state_manager):
        self.state_manager = state_manager

    def enqueue_patient(self, department: str, patient_data: dict):
        self.state_manager.add_patient(department, patient_data)

        queue = self.state_manager.get_department_queue(department)

        sorted_queue = QueueUtils.sort_by_priority(queue)

        self.state_manager.departments[department] = sorted_queue

        return sorted_queue

    def dequeue_patient(self, department: str):
        queue = self.state_manager.get_department_queue(department)

        if not queue:
            return None

        patient = queue.pop(0)

        return patient