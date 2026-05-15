from ai_engine.exceptions import (
    AIEngineError,
    QueueFullException,
    PatientNotFoundException,
    InvalidDepartmentException,
    DoctorUnavailableException,
    PredictionException,
    ModelLoadException,
    DatabaseException
)


def test_ai_engine_error():

    error = AIEngineError(
        "engine failure"
    )

    assert (
        str(error)
        == "engine failure"
    )


def test_queue_full_exception():

    error = QueueFullException(
        "queue full"
    )

    assert (
        str(error)
        == "queue full"
    )


def test_patient_not_found_exception():

    error = PatientNotFoundException(
        "patient missing"
    )

    assert (
        str(error)
        == "patient missing"
    )


def test_invalid_department_exception():

    error = InvalidDepartmentException(
        "invalid department"
    )

    assert (
        str(error)
        == "invalid department"
    )


def test_doctor_unavailable_exception():

    error = DoctorUnavailableException(
        "doctor unavailable"
    )

    assert (
        str(error)
        == "doctor unavailable"
    )


def test_prediction_exception():

    error = PredictionException(
        "prediction failed"
    )

    assert (
        str(error)
        == "prediction failed"
    )


def test_model_load_exception():

    error = ModelLoadException(
        "model missing"
    )

    assert (
        str(error)
        == "model missing"
    )


def test_database_exception():

    error = DatabaseException(
        "database failed"
    )

    assert (
        str(error)
        == "database failed"
    )