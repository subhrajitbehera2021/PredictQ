from ai_engine.doctor_ai.consultation_time_predictor import (
    ConsultationTimePredictor
)


predictor = ConsultationTimePredictor()


def test_consultation_prediction():

    result = predictor.predict_time(
        patient_age=70,
        symptoms_count=3,
        priority=2
    )

    assert (
        result["predicted_minutes"]
        > 10
    )


def test_average_consultation_time():

    predictor.predict_time(
        patient_age=40,
        symptoms_count=1,
        priority=1
    )

    avg = (
        predictor.average_consultation_time()
    )

    assert avg > 0