import sys
import os

sys.path.append(
    os.path.abspath(
        os.path.join(
            os.path.dirname(__file__),
            "../../"
        )
    )
)

from ai_engine.bootstrap import engine


def test_engine_run():

    # ============================================
    # REGISTER PATIENT
    # ============================================

    queue = engine.register_patient(
        "cardiology",
        {
            "patient_id": "P001",
            "name": "John",
            "priority": 1
        }
    )

    # ============================================
    # ASSERT QUEUE
    # ============================================

    assert len(queue) >= 1

    print("Patient registered successfully")

    # ============================================
    # REALTIME SNAPSHOT TEST
    # ============================================

    snapshot = (
        engine.realtime_sync_manager.get_live_snapshot(
            "cardiology"
        )
    )

    print("\nRealtime Snapshot:\n")

    print(snapshot)

    # ============================================
    # ASSERT REALTIME STATE
    # ============================================

    assert snapshot["queue_size"] == 1

    assert snapshot["department"] == "cardiology"


if __name__ == "__main__":

    test_engine_run()