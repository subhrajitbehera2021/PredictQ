class AIEngineError(Exception):

    def __init__(
        self,
        message="AI Engine Error"
    ):

        self.message = message

        super().__init__(
            self.message
        )


# =====================================================
# QUEUE ERRORS
# =====================================================

class QueueEngineException(
    AIEngineError
):

    pass


class QueueFullException(
    QueueEngineException
):

    pass


class EmptyQueueException(
    QueueEngineException
):

    pass


class InvalidDepartmentException(
    QueueEngineException
):

    pass


# =====================================================
# PATIENT ERRORS
# =====================================================

class PatientException(
    AIEngineError
):

    pass


class PatientNotFoundException(
    PatientException
):

    pass


class DuplicatePatientException(
    PatientException
):

    pass


# =====================================================
# DOCTOR ERRORS
# =====================================================

class DoctorException(
    AIEngineError
):

    pass


class DoctorUnavailableException(
    DoctorException
):

    pass


class DoctorNotFoundException(
    DoctorException
):

    pass


# =====================================================
# PREDICTION ERRORS
# =====================================================

class PredictionException(
    AIEngineError
):

    pass


class ModelLoadException(
    PredictionException
):

    pass


class InferenceException(
    PredictionException
):

    pass


class DriftDetectionException(
    PredictionException
):

    pass


# =====================================================
# DATABASE ERRORS
# =====================================================

class DatabaseException(
    AIEngineError
):

    pass


class DatabaseConnectionException(
    DatabaseException
):

    pass


# =====================================================
# REALTIME ERRORS
# =====================================================

class RealtimeException(
    AIEngineError
):

    pass


class WebSocketException(
    RealtimeException
):

    pass