from ai_engine.analytics_ai.predictive_analytics_engine import (
    PredictiveAnalyticsEngine
)


engine = PredictiveAnalyticsEngine()


def test_predictive_report():

    report = (
        engine.generate_predictive_report(
            current_queue=20,
            predicted_load=80,
            available_doctors=2
        )
    )

    assert (
        report["overload_risk"]
        == "CRITICAL"
    )

    assert (
        report["staffing"]["status"]
        == "SHORTAGE"
    )


def test_queue_growth():

    growth = engine.predict_queue_growth(
        20,
        50
    )

    assert growth == 30