from ai_engine.queue_ai.queue_balancer import (
    QueueBalancer
)


balancer = QueueBalancer()


def test_queue_balancer():

    departments = {
        "cardiology": [
            {"patient_id": "P001"},
            {"patient_id": "P002"}
        ],
        "neurology": [
            {"patient_id": "P003"}
        ]
    }

    result = balancer.balance_departments(
        departments
    )

    assert (
        result["least_busy_department"]
        == "neurology"
    )

    assert (
        result["department_loads"]
        ["cardiology"] == 2
    )
