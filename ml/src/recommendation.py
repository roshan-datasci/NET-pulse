def recommend_network(candidates):
    """
    Select the most suitable network.

    Suitability is the primary criterion.
    Distance is used only when suitability scores are equal.
    """

    if not candidates:
        return None

    ranked_candidates = sorted(
        candidates,
        key=lambda candidate: (
            -candidate["suitability_score"],
            candidate["distance_to_ap_m"],
        ),
    )

    return ranked_candidates[0]


if __name__ == "__main__":

    candidates = [
        {
            "network_name": "Nearby_WiFi",
            "suitability_score": 45,
            "distance_to_ap_m": 20,
        },

        {
            "network_name": "Sample_WiFi",
            "suitability_score": 78,
            "distance_to_ap_m": 80,
        },

        {
            "network_name": "Library_WiFi",
            "suitability_score": 72,
            "distance_to_ap_m": 60,
        },
    ]

    recommendation = recommend_network(
        candidates
    )

    print("=== WiSense Recommendation ===")
    print()

    if recommendation is None:

        print("No suitable network found.")

    else:

        print(
            f"Recommended network: "
            f"{recommendation['network_name']}"
        )

        print(
            f"Suitability: "
            f"{recommendation['suitability_score']}/100"
        )

        print(
            f"Distance: "
            f"{recommendation['distance_to_ap_m']} m"
        )