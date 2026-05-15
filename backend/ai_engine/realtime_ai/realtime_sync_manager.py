from ai_engine.utils.logging_utils import (
    get_logger
)

from ai_engine.realtime_ai.live_queue_updater import (
    LiveQueueUpdater
)

from ai_engine.realtime_ai.websocket_ai_dispatcher import (
    WebSocketAIDispatcher
)


logger = get_logger(__name__)


class RealtimeSyncManager:

    def __init__(self):

        # LIVE QUEUE STORAGE
        self.live_updater = LiveQueueUpdater()

        # WEBSOCKET EVENT DISPATCHER
        self.websocket_dispatcher = (
            WebSocketAIDispatcher()
        )

    # =====================================================
    # SYNC QUEUE STATE
    # =====================================================

    def sync_department_queue(
        self,
        department: str,
        queue_data: list
    ):

        # UPDATE LIVE QUEUE STATE
        updated_queue = (
            self.live_updater.update_queue(
                department,
                queue_data
            )
        )

        # BROADCAST LIVE EVENT
        self.websocket_dispatcher.broadcast_event(
            "LIVE_QUEUE_UPDATED",
            updated_queue
        )

        logger.info(
            f"Realtime sync completed for "
            f"{department}"
        )

        return updated_queue

    # =====================================================
    # GET LIVE SNAPSHOT
    # =====================================================

    def get_live_snapshot(
        self,
        department: str
    ):

        return self.live_updater.get_live_queue(
            department
        )

    # =====================================================
    # GET GLOBAL SNAPSHOT
    # =====================================================

    def get_global_snapshot(self):

        return self.live_updater.get_all_live_queues()

    # =====================================================
    # CONNECT CLIENT
    # =====================================================

    def connect_client(
        self,
        client_id: str
    ):

        self.websocket_dispatcher.connect_client(
            client_id
        )

    # =====================================================
    # DISCONNECT CLIENT
    # =====================================================

    def disconnect_client(
        self,
        client_id: str
    ):

        self.websocket_dispatcher.disconnect_client(
            client_id
        )

    # =====================================================
    # GET ACTIVE CLIENTS
    # =====================================================

    def get_active_clients(self):

        return (
            self.websocket_dispatcher
            .get_active_clients()
        )