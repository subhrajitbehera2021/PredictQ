from ai_engine.analytics_ai.doctor_performance_ai import (
    DoctorPerformanceAI
)


performance_ai = DoctorPerformanceAI()


def test_doctor_performance():

    report = (
        performance_ai.analyze_doctor_performance(
            doctor_id="D001",
            consultation_times=[10, 15, 20],
            patients_completed=18,
            working_hours=6,
            active_patients=12
        )
    )

    assert report["doctor_id"] == "D001"

    assert (
        report["performance_score"]
        > 0
    )


def test_workload_analysis():

    result = (
        performance_ai.analyze_workload(
            35
        )
    )

    assert (
        result["workload_status"]
        == "OVERLOADED"
    )