from ai_engine.fallback_system.degraded_mode_manager import (
    DegradedModeManager
)


manager = DegradedModeManager()


def test_activate_degraded_mode():

    status = manager.activate_degraded_mode(
        "REALTIME_FAILURE"
    )

    assert status["degraded_mode"] is True
    assert status["reason"] == "REALTIME_FAILURE"


def test_allowed_features_in_degraded_mode():

    features = manager.get_allowed_features()

    assert "REGISTER_PATIENT" in features
    assert "AI_PREDICTION" not in features


def test_deactivate_degraded_mode():

    status = manager.deactivate_degraded_mode()

    assert status["degraded_mode"] is False