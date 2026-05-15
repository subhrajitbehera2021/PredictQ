from ai_engine.optimization_ai.resource_allocator import (
    ResourceAllocator
)


allocator = ResourceAllocator()


def test_resource_allocator():

    department_data = {

        "cardiology": {
            "queue_size": 50,
            "available_doctors": 2
        },

        "neurology": {
            "queue_size": 5,
            "available_doctors": 5
        }
    }

    reallocations = (
        allocator.generate_reallocation_plan(
            department_data
        )
    )

    assert len(reallocations) >= 1

    assert (
        reallocations[0]["to_department"]
        == "cardiology"
    )