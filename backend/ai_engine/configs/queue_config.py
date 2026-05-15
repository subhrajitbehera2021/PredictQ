class QueueConfig:

    # =====================================================
    # QUEUE LIMITS
    # =====================================================

    MAX_QUEUE_SIZE = 500

    CRITICAL_QUEUE_SIZE = 200

    WARNING_QUEUE_SIZE = 100

    # =====================================================
    # WAIT TIME LIMITS
    # =====================================================

    MAX_WAIT_TIME = 180

    CRITICAL_WAIT_TIME = 120

    WARNING_WAIT_TIME = 60

    # =====================================================
    # PATIENT PRIORITY LEVELS
    # =====================================================

    PRIORITY_CRITICAL = 1

    PRIORITY_HIGH = 2

    PRIORITY_MEDIUM = 3

    PRIORITY_LOW = 4

    # =====================================================
    # DOCTOR LOAD SETTINGS
    # =====================================================

    MAX_PATIENTS_PER_DOCTOR = 50

    IDEAL_PATIENTS_PER_DOCTOR = 20

    MIN_AVAILABLE_DOCTORS = 1

    # =====================================================
    # REALTIME QUEUE SETTINGS
    # =====================================================

    ENABLE_REALTIME_BALANCING = True

    ENABLE_AUTO_QUEUE_OPTIMIZATION = True

    ENABLE_OVERFLOW_REDIRECTION = True

    # =====================================================
    # TOKEN SETTINGS
    # =====================================================

    TOKEN_PREFIX = "PQ"

    START_TOKEN_NUMBER = 1000

    # =====================================================
    # OPD SETTINGS
    # =====================================================

    OPD_START_HOUR = 9

    OPD_END_HOUR = 18

    # =====================================================
    # ALERT SETTINGS
    # =====================================================

    ENABLE_QUEUE_ALERTS = True

    ENABLE_DOCTOR_ALERTS = True

    ENABLE_PATIENT_ALERTS = True