from ai_engine.analytics_ai.hospital_insights_ai import (
    HospitalInsightsAI
)


insights_ai = HospitalInsightsAI()


def test_hospital_insights():

    department_data = {

        "cardiology": {
            "queue_size": 40,
            "available_doctors": 1
        },

        "neurology": {
            "queue_size": 10,
            "available_doctors": 4
        }
    }

    insights = (
        insights_ai.generate_hospital_insights(
            department_data
        )
    )

    assert (
        insights["busiest_department"]
        == "cardiology"
    )

    assert (
        "cardiology"
        in insights["overloaded_departments"]
    )

    assert (
        "cardiology"
        in insights["doctor_shortages"]
    )