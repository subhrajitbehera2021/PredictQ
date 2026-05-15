from ai_engine.core.state_manager import (
    StateManager
)

from ai_engine.queue_ai.queue_builder import (
    QueueBuilder
)

from ai_engine.core.workflow_engine import (
    WorkflowEngine
)

from ai_engine.doctor_ai.doctor_availability_engine import (
    DoctorAvailabilityEngine
)

from ai_engine.prediction_ai.wait_time_predictor import (
    WaitTimePredictor
)


state = StateManager()

state.create_department(
    "cardiology"
)

queue_builder = QueueBuilder(
    state
)

doctor_engine = (
    DoctorAvailabilityEngine()
)

doctor_engine.register_doctor(
    "D001",
    "Dr. Smith",
    "cardiology"
)

workflow = WorkflowEngine(
    state,
    doctor_engine,
    queue_builder,
    WaitTimePredictor()
)


def test_register_patient_workflow():

    result = workflow.process_patient_registration(
        "cardiology",
        {
            "patient_id": "P001",
            "name": "John",
            "age": 70
        }
    )

    assert result["queue_size"] == 1

    assert (
        result["patient"]["priority"]
        >= 1
    )


def test_department_snapshot():

    snapshot = (
        workflow.get_department_snapshot(
            "cardiology"
        )
    )

    assert (
        snapshot["department"]
        == "cardiology"
    )

    assert (
        snapshot["queue_size"]
        >= 1
    )