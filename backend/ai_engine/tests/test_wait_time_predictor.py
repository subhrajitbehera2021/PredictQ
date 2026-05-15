from ai_engine.prediction_ai.wait_time_predictor import (
    WaitTimePredictor
)


predictor = WaitTimePredictor()


def test_wait_prediction():

    wait = predictor.predict_wait_time(
        queue_size=10,
        available_doctors=2,
        avg_consultation_time=10
    )

    assert wait == 50


def test_average_consultation():

    avg = predictor.calculate_average_consultation(
        [10, 15, 20]
    )

    assert avg == 15