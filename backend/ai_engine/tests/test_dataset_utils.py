from ai_engine.ml.utils.dataset_utils import (
    DatasetUtils
)


sample_dataset = [
    {
        "queue_size": 10,
        "wait_time": 20
    },
    {
        "queue_size": 15,
        "wait_time": 30
    },
    {
        "queue_size": 25,
        "wait_time": 50
    }
]


def test_dataset_split():

    result = (
        DatasetUtils.split_dataset(
            sample_dataset,
            split_ratio=0.7
        )
    )

    assert (
        len(result["train_data"])
        == 2
    )


def test_dataset_size():

    size = (
        DatasetUtils.get_dataset_size(
            sample_dataset
        )
    )

    assert size == 3


def test_extract_column():

    values = (
        DatasetUtils.extract_column(
            sample_dataset,
            "wait_time"
        )
    )

    assert values == [20, 30, 50]


def test_dataset_summary():

    summary = (
        DatasetUtils.generate_dataset_summary(
            sample_dataset
        )
    )

    assert (
        summary["total_rows"]
        == 3
    )