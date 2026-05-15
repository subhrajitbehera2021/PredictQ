from ai_engine.analytics_ai.utilization_analysis import (
    UtilizationAnalysis
)


analysis = UtilizationAnalysis()


def test_doctor_utilization():

    utilization = (
        analysis.analyze_doctor_utilization(
            consultation_hours=6,
            available_hours=8
        )
    )

    assert utilization == 75.0


def test_room_utilization():

    utilization = (
        analysis.analyze_room_utilization(
            occupied_rooms=8,
            total_rooms=10
        )
    )

    assert utilization == 80.0


def test_utilization_report():

    report = (
        analysis.generate_utilization_report(
            consultation_hours=7,
            available_hours=8,
            occupied_rooms=9,
            total_rooms=10,
            active_patients=70,
            max_capacity=100,
            used_resources=15,
            total_resources=20
        )
    )

    assert "doctor_utilization" in report
    assert "room_utilization" in report