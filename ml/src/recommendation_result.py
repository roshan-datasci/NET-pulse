def build_recommendation_result(
    recommendation,
    task
):
    """
    Build a structured recommendation result
    for the WiSense application.
    """

    if recommendation is None:

        return {
            "status": "no_recommendation",
            "task": task,
            "network_name": None,
            "suitability_score": None,
            "distance_to_ap_m": None,
        }

    return {
        "status": "recommended",
        "task": task,
        "network_name": recommendation["network_name"],
        "suitability_score": recommendation[
            "suitability_score"
        ],
        "distance_to_ap_m": recommendation[
            "distance_to_ap_m"
        ],
    }


if __name__ == "__main__":

    test_recommendation = {
        "network_name": "Sample_WiFi",
        "suitability_score": 83,
        "distance_to_ap_m": 80,
    }

    result = build_recommendation_result(
        test_recommendation,
        "gaming"
    )

    print("=== WiSense Recommendation Result ===")
    print()

    for key, value in result.items():

        print(
            f"{key}: {value}"
        )
