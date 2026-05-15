from ai_engine.ml.preprocessing.dataset_builder import (
    DatasetBuilder
)


builder = DatasetBuilder()


sample_records = [

    {
        "eta_features": {
            "queue_size": 10,
            "available_doctors": 2,
            "patient_priority": 1,
            "symptoms_count": 3
        },

        "no_show_features": {
            "previous_no_shows": 1,
            "travel_distance_km": 20,
            "waiting_time_minutes": 60
        },

        "crowd_features": {
            "patient_count": 40,
            "room_capacity": 50,
            "doctor_count": 5
        }
    }
]


def test_eta_dataset():

    dataset = (
        builder.build_eta_dataset(
            sample_records
        )
    )

    assert dataset[0]["queue_size"] == 10


def test_no_show_dataset():

    dataset = (
        builder.build_no_show_dataset(
            sample_records
        )
    )

    assert (
        dataset[0][
            "travel_distance_km"
        ] == 20
    )


def test_training_dataset():

    dataset = (
        builder.build_training_dataset(
            sample_records
        )
    )

    assert "eta_dataset" in dataset
    assert "crowd_dataset" in dataset