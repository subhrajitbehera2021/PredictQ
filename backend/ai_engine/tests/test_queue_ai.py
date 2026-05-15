from ai_engine.engine import AIQueueEngine


engine = AIQueueEngine()
engine.boot()

engine.create_department("cardiology")


def test_patient_enqueue():
    
    engine.register_patient(
        "cardiology",
        {
            "patient_id": "P001",
            "name": "John",
            "priority": 3
        }
    )

    queue = engine.state_manager.get_department_queue(
        "cardiology"
    )

    assert len(queue) == 1


def test_eta_prediction():

    eta = engine.estimate_wait_time(5)

    assert eta == 50