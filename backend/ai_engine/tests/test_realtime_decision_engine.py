from ai_engine.optimization_ai.realtime_decision_engine import (
    RealtimeDecisionEngine
)


engine = RealtimeDecisionEngine()


def test_realtime_decisions():

    department_data = {

        "cardiology": {
            "queue_size": 80,
            "available_doctors": 2
        },

        "neurology": {
            "queue_size": 10,
            "available_doctors": 5
        }
    }

    decisions = (
        engine.generate_realtime_decisions(
            department_data
        )
    )

    assert len(decisions) >= 1


def test_capacity_expansion():

    decision = (
        engine.decide_capacity_expansion(
            predicted_load=100,
            available_doctors=2
        )
    )

    assert (
        decision["action"]
        == "EXPAND_CAPACITY"
    )