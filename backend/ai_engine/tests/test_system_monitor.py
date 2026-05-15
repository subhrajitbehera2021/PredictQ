from ai_engine.monitoring.system_monitor import (
    SystemMonitor
)


monitor = SystemMonitor()


def test_health_monitoring():

    result = monitor.monitor_health(
        queue_size=60,
        available_doctors=1
    )

    assert (
        result["queue_status"]
        == "CRITICAL"
    )


def test_anomaly_monitoring():

    report = monitor.monitor_anomalies(
        queue_size=80,
        available_doctors=0
    )

    assert (
        report["total_anomalies"]
        >= 2
    )


def test_system_recovery():

    monitor.activate_degraded_mode(
        "REALTIME_FAILURE"
    )

    recovery = monitor.recover_system()

    assert (
        recovery["system"]
        == "RECOVERED"
    )