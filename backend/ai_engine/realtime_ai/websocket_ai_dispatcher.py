from ai_engine.utils.logging_utils import (
    get_logger
)


logger = get_logger(__name__)


class WebSocketAIDispatcher:

    def __init__(self):

        self.connected_clients = []

    # =====================================================
    # CONNECT CLIENT
    # =====================================================

    def connect_client(
        self,
        client_id: str
    ):

        if client_id not in self.connected_clients:

            self.connected_clients.append(
                client_id
            )

            logger.info(
                f"Client connected: {client_id}"
            )

    # =====================================================
    # DISCONNECT CLIENT
    # =====================================================

    def disconnect_client(
        self,
        client_id: str
    ):

        if client_id in self.connected_clients:

            self.connected_clients.remove(
                client_id
            )

            logger.info(
                f"Client disconnected: {client_id}"
            )

    # =====================================================
    # BROADCAST EVENT
    # =====================================================

    def broadcast_event(
        self,
        event_name: str,
        payload: dict
    ):

        logger.info(
            f"Broadcasting event "
            f"{event_name} "
            f"to {len(self.connected_clients)} "
            f"clients"
        )

        for client in self.connected_clients:

            logger.info(
                f"Sent event to client: {client}"
            )

    # =====================================================
    # GET ACTIVE CLIENTS
    # =====================================================

    def get_active_clients(self):

        return self.connected_clients