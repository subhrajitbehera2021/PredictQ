from ai_engine.analytics_ai.queue_analytics_engine import (
    QueueAnalyticsEngine
)


analytics = QueueAnalyticsEngine()


def test_queue_size_analytics():

    result = analytics.analyze_queue_size(
        [
            {"patient_id": "P001"},
            {"patient_id": "P002"}
        ]
    )

    assert result["queue_size"] == 2


def test_priority_distribution():

    queue = [
        {"priority": 1},
        {"priority": 2},
        {"priority": 2}
    ]

    result = (
        analytics.analyze_priority_distribution(
            queue
        )
    )

    assert result[2] == 2


def test_average_wait():

    result = analytics.analyze_average_wait(
        [10, 20, 30]
    )

    assert result["average_wait"] == 20