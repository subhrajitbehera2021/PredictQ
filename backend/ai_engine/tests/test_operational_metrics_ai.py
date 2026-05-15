from ai_engine.analytics_ai.operational_metrics_ai import (
    OperationalMetricsAI
)


engine = OperationalMetricsAI()


def test_queue_efficiency():

    efficiency = (
        engine.calculate_queue_efficiency(
            served_patients=80,
            total_patients=100
        )
    )

    assert efficiency == 80.0


def test_doctor_utilization():

    utilization = (
        engine.calculate_doctor_utilization(
            busy_doctors=4,
            total_doctors=5
        )
    )

    assert utilization == 80.0


def test_operational_report():

    report = (
        engine.generate_operational_report(
            served_patients=100,
            total_patients=120,
            busy_doctors=5,
            total_doctors=6,
            operating_hours=10,
            overloaded_departments=1,
            total_departments=5
        )
    )

    assert "queue_efficiency" in report
    assert "doctor_utilization" in report