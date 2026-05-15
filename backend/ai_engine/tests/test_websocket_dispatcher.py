from ai_engine.realtime_ai.websocket_ai_dispatcher import (
    WebSocketAIDispatcher
)


dispatcher = WebSocketAIDispatcher()


def test_websocket_dispatcher():

    dispatcher.connect_client(
        "dashboard_client_1"
    )

    dispatcher.broadcast_event(
        "TEST_EVENT",
        {
            "hello": "world"
        }
    )

    clients = dispatcher.get_active_clients()

    assert len(clients) == 1