from ai_engine.prediction_ai.hospital_load_forecaster import (
    HospitalLoadForecaster
)


forecaster = HospitalLoadForecaster()


def test_forecast_patient_load():

    predicted = (
        forecaster.forecast_patient_load(
            [40, 50, 60]
        )
    )

    assert predicted == 50


def test_peak_detection():

    peak = forecaster.detect_peak_load(
        80
    )

    assert peak is True


def test_forecast_report():

    report = (
        forecaster.generate_forecast_report(
            [40, 50, 60]
        )
    )

    assert report["predicted_load"] == 50