from ai_engine.core.state_manager import StateManager
from ai_engine.queue_ai.queue_builder import QueueBuilder
from ai_engine.core.queue_orchestrator import QueueOrchestrator


state = StateManager()
state.create_department("cardiology")

builder = QueueBuilder(state)
orchestrator = QueueOrchestrator(state, builder)


def test_queue_orchestrator_enqueue():

    queue = orchestrator.enqueue_patient(
        "cardiology",
        {
            "patient_id": "P001",
            "priority": 2,
            "created_at": "2026-01-01T10:00:00"
        }
    )

    assert len(queue) == 1


def test_queue_orchestrator_call_next():

    patient = orchestrator.call_next_patient(
        "cardiology"
    )

    assert patient["patient_id"] == "P001"