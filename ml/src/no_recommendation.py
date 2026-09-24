def build_no_recommendation_result(
    task,
    candidates
):
    """
    Handle the situation where no network
    satisfies the selected task.
    """

    if candidates:
        return None

    return {
        "status": "no_recommendation",
        "task": task,
        "message": (
            f"No suitable network was found "
            f"for {task}."
        ),
        "suggestion": (
            "Try another location or select "
            "a different task."
        ),
    }


if __name__ == "__main__":

    task = "gaming"

    candidates = []

    result = build_no_recommendation_result(
        task,
        candidates
    )

    print(
        "=== WiSense No Recommendation Test ==="
    )
    print()

    if result:

        print(
            f"Status: "
            f"{result['status']}"
        )

        print(
            f"Message: "
            f"{result['message']}"
        )

        print(
            f"Suggestion: "
            f"{result['suggestion']}"
        )

    else:

        print(
            "Suitable candidates exist."
        )
