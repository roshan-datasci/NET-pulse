TASK_REQUIREMENTS = {
    "general": {
        "min_suitability": 40,
        "description": "Suitable for normal internet usage.",
    },

    "browsing": {
        "min_suitability": 35,
        "description": "Suitable for web browsing and light usage.",
    },

    "video_call": {
        "min_suitability": 65,
        "description": "Requires stable and reasonably strong connectivity.",
    },

    "download": {
        "min_suitability": 60,
        "description": "Requires good throughput for faster downloads.",
    },

    "gaming": {
        "min_suitability": 70,
        "description": "Requires strong and stable connectivity.",
    },
}


def get_task_requirement(task):
    """
    Return the connectivity requirement for a task.
    """

    task = task.lower()

    if task not in TASK_REQUIREMENTS:
        raise ValueError(
            f"Unknown task: {task}"
        )

    return TASK_REQUIREMENTS[task]


def is_suitable_for_task(
    suitability_score,
    task
):
    """
    Check whether a connectivity score
    satisfies the selected task.
    """

    requirement = get_task_requirement(task)

    return (
        suitability_score
        >= requirement["min_suitability"]
    )


if __name__ == "__main__":

    print("=== WiSense Task Requirements ===")
    print()

    test_score = 68

    for task in TASK_REQUIREMENTS:

        requirement = get_task_requirement(task)

        suitable = is_suitable_for_task(
            test_score,
            task
        )

        print(
            f"{task}: "
            f"minimum={requirement['min_suitability']}, "
            f"score={test_score}, "
            f"suitable={suitable}"
        )
