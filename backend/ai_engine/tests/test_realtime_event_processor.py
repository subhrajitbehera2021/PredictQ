from ai_engine.realtime_ai.realtime_sync_manager import (
    RealtimeSyncManager
)

from ai_engine.core.event_dispatcher import (
    EventDispatcher
)

from ai_engine.realtime_ai.realtime_event_processor import (
    RealtimeEventProcessor
)


processor = RealtimeEventProcessor(
    RealtimeSyncManager(),
    EventDispatcher()
)


def test_realtime_queue_update():

    result = processor.process_queue_update(
        "cardiology",
        [
            {
                "patient_id": "P001"
            }
        ]
    )

    assert result["success"] is True
    assert result["queue_size"] == 1


def test_realtime_alert():

    result = processor.process_system_alert(
        "OVERLOAD",
        "Queue overloaded"
    )

    assert result["alert_type"] == "OVERLOAD"