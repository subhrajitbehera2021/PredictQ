from ai_engine.database.database_manager import (
    DatabaseManager
)


db = DatabaseManager()


def test_database_connection():

    result = db.connect()

    assert (
        result["status"]
        == "CONNECTED"
    )


def test_save_patient():

    result = db.save_patient(
        {
            "patient_id": 1,
            "name": "Rahul"
        }
    )

    assert (
        result["saved"]
        is True
    )


def test_save_prediction():

    result = db.save_prediction(
        {
            "prediction": "ETA",
            "value": 25
        }
    )

    assert (
        result["saved"]
        is True
    )


def test_database_status():

    status = db.get_status()

    assert (
        status["connected"]
        is True
    )