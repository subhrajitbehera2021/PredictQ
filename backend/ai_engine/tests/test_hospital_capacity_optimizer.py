from ai_engine.optimization_ai.hospital_capacity_optimizer import (
    HospitalCapacityOptimizer
)


optimizer = (
    HospitalCapacityOptimizer()
)


def test_capacity_analysis():

    result = optimizer.analyze_capacity(
        patient_load=100,
        doctor_count=2,
        room_count=2
    )

    assert (
        result["capacity_status"]
        in [
            "HIGH",
            "CRITICAL"
        ]
    )


def test_capacity_recommendations():

    recommendations = (
        optimizer.generate_recommendations(
            95
        )
    )

    assert len(recommendations) >= 1


def test_optimization_report():

    report = (
        optimizer.generate_optimization_report(
            patient_load=120,
            doctor_count=3,
            room_count=3
        )
    )

    assert "analysis" in report
    assert "recommendations" in report