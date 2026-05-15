from ai_engine.configs.queue_config import (
    QueueConfig
)


def test_queue_limits():

    assert (
        QueueConfig.MAX_QUEUE_SIZE
        == 500
    )

    assert (
        QueueConfig.CRITICAL_QUEUE_SIZE
        == 200
    )


def test_wait_time_limits():

    assert (
        QueueConfig.MAX_WAIT_TIME
        == 180
    )

    assert (
        QueueConfig.WARNING_WAIT_TIME
        == 60
    )


def test_priority_levels():

    assert (
        QueueConfig.PRIORITY_CRITICAL
        == 1
    )

    assert (
        QueueConfig.PRIORITY_LOW
        == 4
    )


def test_realtime_features():

    assert (
        QueueConfig.ENABLE_REALTIME_BALANCING
        is True
    )

    assert (
        QueueConfig.ENABLE_AUTO_QUEUE_OPTIMIZATION
        is True
    )