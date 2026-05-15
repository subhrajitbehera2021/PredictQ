from typing import List


class QueueUtils:

    @staticmethod
    def calculate_eta(position: int, avg_time: int):
        return position * avg_time

    @staticmethod
    def sort_by_priority(queue: List[dict]):
        return sorted(
            queue,
            key=lambda x: x.get("priority", 1),
            reverse=True
        )