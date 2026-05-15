from ai_engine.fallback_system.fail_safe_engine import (
    FailSafeEngine
)


engine = FailSafeEngine()


def test_prediction_failure():

    event = engine.handle_prediction_failure(
        fallback_wait_time=15
    )

    assert event["type"] == "PREDICTION_FAILURE"
    assert event["fallback_wait_time"] == 15


def test_realtime_failure():

    event = engine.handle_realtime_failure()

    assert event["action"] == "SWITCH_TO_POLLING_MODE"


def test_queue_overflow():

    event = engine.handle_queue_overflow()

    assert event["type"] == "QUEUE_OVERFLOW"