from ai_engine.monitoring.ai_health_monitor import (
    AIHealthMonitor
)


monitor = AIHealthMonitor()


def test_queue_pressure():

    status = monitor.check_queue_pressure(
        60
    )

    assert status == "CRITICAL"


def test_doctor_availability():

    status = (
        monitor.check_doctor_availability(
            0
        )
    )

    assert status == "CRITICAL"


def test_system_health():

    monitor.check_queue_pressure(60)

    health = monitor.get_system_health()

    assert health["system"] == "CRITICAL"