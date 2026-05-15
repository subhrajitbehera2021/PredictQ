from ai_engine.fallback_system.recovery_engine import (
    RecoveryEngine
)


engine = RecoveryEngine()


def test_prediction_recovery():

    result = engine.recover_prediction_service()

    assert result["service"] == "AI_PREDICTION"
    assert result["status"] == "RECOVERED"


def test_realtime_recovery():

    result = engine.recover_realtime_service()

    assert result["service"] == "REALTIME_SYNC"


def test_full_recovery():

    result = engine.recover_full_system()

    assert result["system"] == "RECOVERED"
    assert len(result["recoveries"]) == 3