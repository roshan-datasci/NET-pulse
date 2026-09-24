def compare_current_network(
    current_network,
    recommended_network
):
    """
    Compare the user's current network with
    the recommended alternative.
    """

    if recommended_network is None:
        return {
            "has_better_alternative": False,
            "message": "No suitable alternative network found.",
        }

    current_score = current_network[
        "suitability_score"
    ]

    recommended_score = recommended_network[
        "suitability_score"
    ]

    score_difference = (
        recommended_score - current_score
    )

    if score_difference > 0:

        return {
            "has_better_alternative": True,
            "message": (
                f"{recommended_network['network_name']} "
                f"is more suitable than your current "
                f"network for this task."
            ),
            "current_score": current_score,
            "recommended_score": recommended_score,
            "improvement": score_difference,
        }

    return {
        "has_better_alternative": False,
        "message": (
            "Your current network is already "
            "the most suitable available option."
        ),
        "current_score": current_score,
        "recommended_score": recommended_score,
        "improvement": 0,
    }


if __name__ == "__main__":

    current_network = {
        "network_name": "Nearby_WiFi",
        "suitability_score": 45,
    }

    recommended_network = {
        "network_name": "Sample_WiFi",
        "suitability_score": 83,
    }

    result = compare_current_network(
        current_network,
        recommended_network
    )

    print("=== WiSense Current vs Alternative ===")
    print()

    print(
        f"Current network: "
        f"{current_network['network_name']}"
    )

    print(
        f"Current score: "
        f"{current_network['suitability_score']}/100"
    )

    print()

    print(result["message"])

    if result["has_better_alternative"]:

        print(
            f"Recommended score: "
            f"{result['recommended_score']}/100"
        )

        print(
            f"Improvement: "
            f"+{result['improvement']} points"
        )
