from ai_engine.monitoring.performance_tracker import (
    PerformanceTracker
)


tracker = PerformanceTracker()


def test_record_metric():

    metric = tracker.record_metric(
        "QUEUE_ENQUEUE_TIME",
        12.5,
        "QUEUE_OPERATION"
    )

    assert metric["metric_name"] == "QUEUE_ENQUEUE_TIME"
    assert metric["value"] == 12.5


def test_category_filter():

    metrics = tracker.get_metrics_by_category(
        "QUEUE_OPERATION"
    )

    assert len(metrics) >= 1


def test_average_metric():

    tracker.record_queue_operation_time(
        "QUEUE_DEQUEUE_TIME",
        7.5
    )

    avg = tracker.calculate_average_metric(
        "QUEUE_OPERATION"
    )

    assert avg > 0