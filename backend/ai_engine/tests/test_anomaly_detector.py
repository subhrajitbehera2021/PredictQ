from ai_engine.monitoring.anomaly_detector import (
    AnomalyDetector
)


detector = AnomalyDetector()


def test_queue_spike_detection():

    detected = detector.detect_queue_spike(
        80
    )

    assert detected is True


def test_doctor_shortage_detection():

    detected = (
        detector.detect_doctor_shortage(
            0
        )
    )

    assert detected is True


def test_risk_report():

    report = detector.generate_risk_report()

    assert (
        report["total_anomalies"]
        >= 2
    )