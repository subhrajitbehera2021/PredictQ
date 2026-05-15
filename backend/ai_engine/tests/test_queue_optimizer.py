from ai_engine.queue_ai.queue_optimizer import (
    QueueOptimizer
)


optimizer = QueueOptimizer()


def test_queue_optimizer_priority():

    queue = [
        {
            "patient_id": "P001",
            "priority": 1,
            "created_at": "2026-01-01T10:00:00"
        },
        {
            "patient_id": "P002",
            "priority": 4,
            "created_at": "2026-01-01T10:05:00"
        }
    ]

    optimized = optimizer.optimize(queue)

    assert optimized[0]["patient_id"] == "P002"


def test_next_patient():

    queue = [
        {
            "patient_id": "P100",
            "priority": 3,
            "created_at": "2026-01-01T10:00:00"
        }
    ]

    next_patient = (
        optimizer.get_next_patient(queue)
    )

    assert next_patient["patient_id"] == "P100"