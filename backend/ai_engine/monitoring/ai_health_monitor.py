from ai_engine.utils.logging_utils import (
    get_logger
)


logger = get_logger(__name__)


class AIHealthMonitor:

    def __init__(self):

        self.health_status = {
            "system": "HEALTHY",
            "queue_pressure": "NORMAL",
            "doctor_availability": "NORMAL",
            "realtime_sync": "ACTIVE",
            "websocket": "CONNECTED"
        }

    # =====================================================
    # CHECK QUEUE PRESSURE
    # =====================================================

    def check_queue_pressure(
        self,
        queue_size: int
    ):

        if queue_size >= 50:

            self.health_status[
                "queue_pressure"
            ] = "CRITICAL"

        elif queue_size >= 30:

            self.health_status[
                "queue_pressure"
            ] = "HIGH"

        else:

            self.health_status[
                "queue_pressure"
            ] = "NORMAL"

        logger.info(
            f"Queue pressure status: "
            f"{self.health_status['queue_pressure']}"
        )

        return self.health_status[
            "queue_pressure"
        ]

    # =====================================================
    # CHECK DOCTOR AVAILABILITY
    # =====================================================

    def check_doctor_availability(
        self,
        available_doctors: int
    ):

        if available_doctors <= 0:

            self.health_status[
                "doctor_availability"
            ] = "CRITICAL"

        elif available_doctors <= 2:

            self.health_status[
                "doctor_availability"
            ] = "LOW"

        else:

            self.health_status[
                "doctor_availability"
            ] = "NORMAL"

        logger.info(
            f"Doctor availability status: "
            f"{self.health_status['doctor_availability']}"
        )

        return self.health_status[
            "doctor_availability"
        ]

    # =====================================================
    # REALTIME SYNC STATUS
    # =====================================================

    def check_realtime_sync(
        self,
        sync_active: bool
    ):

        self.health_status[
            "realtime_sync"
        ] = (
            "ACTIVE"
            if sync_active
            else "FAILED"
        )

        logger.info(
            f"Realtime sync status: "
            f"{self.health_status['realtime_sync']}"
        )

        return self.health_status[
            "realtime_sync"
        ]

    # =====================================================
    # WEBSOCKET STATUS
    # =====================================================

    def check_websocket_status(
        self,
        connected: bool
    ):

        self.health_status[
            "websocket"
        ] = (
            "CONNECTED"
            if connected
            else "DISCONNECTED"
        )

        logger.info(
            f"WebSocket status: "
            f"{self.health_status['websocket']}"
        )

        return self.health_status[
            "websocket"
        ]

    # =====================================================
    # GLOBAL SYSTEM STATUS
    # =====================================================

    def get_system_health(self):

        if (
            self.health_status[
                "queue_pressure"
            ] == "CRITICAL"
            or
            self.health_status[
                "doctor_availability"
            ] == "CRITICAL"
        ):

            self.health_status[
                "system"
            ] = "CRITICAL"

        else:

            self.health_status[
                "system"
            ] = "HEALTHY"

        logger.info(
            f"Global system status: "
            f"{self.health_status['system']}"
        )

        return self.health_status