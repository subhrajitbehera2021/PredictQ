from ai_engine.ml.preprocessing.data_cleaning import (
    DataCleaning
)


cleaner = DataCleaning()


def test_remove_null_values():

    dataset = [

        {"id": 1, "name": "John"},

        {"id": 2, "name": None}
    ]

    cleaned = cleaner.remove_null_values(
        dataset
    )

    assert len(cleaned) == 1


def test_remove_duplicates():

    dataset = [

        {"id": 1, "name": "John"},

        {"id": 1, "name": "John"}
    ]

    cleaned = cleaner.remove_duplicates(
        dataset,
        "id"
    )

    assert len(cleaned) == 1


def test_clean_pipeline():

    dataset = [

        {
            "id": 1,
            "name": " JOHN "
        },

        {
            "id": 1,
            "name": " JOHN "
        }
    ]

    cleaned = cleaner.clean_dataset(
        dataset,
        "id"
    )

    assert cleaned[0]["name"] == "john"