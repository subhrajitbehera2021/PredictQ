from ai_engine.core.event_dispatcher import (
    EventDispatcher
)


dispatcher = EventDispatcher()

called = False


def sample_listener(payload):

    global called

    called = True


def test_event_dispatch():

    dispatcher.subscribe(
        "TEST_EVENT",
        sample_listener
    )

    dispatcher.dispatch(
        "TEST_EVENT",
        {
            "hello": "world"
        }
    )

    assert called is True