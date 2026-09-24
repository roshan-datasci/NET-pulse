from suitability import calculate_suitability
from task_requirements import is_suitable_for_task


def filter_candidates(observations, task):
    """
    Filter Wi-Fi observations based on the
    user's selected task.
    """

    candidates = []

    for observation in observations:

        suitability_score = calculate_suitability(
            observation
        )

        suitable = is_suitable_for_task(
            suitability_score,
            task
        )

        if suitable:

            candidate = observation.copy()

            candidate["suitability_score"] = (
                suitability_score
            )

            candidates.append(candidate)

    return candidates


if __name__ == "__main__":

    test_networks = [
        {
            "network_name": "Nearby_WiFi",
            "rssi_dbm": -75,
            "signal_std_dbm": 7,
            "distance_to_ap_m": 20,
            "connected_devices": 70,
            "avg_download_mbps": 25,
            "peak_usage_hours": 1,
        },

        {
            "network_name": "Sample_WiFi",
            "rssi_dbm": -50,
            "signal_std_dbm": 2,
            "distance_to_ap_m": 80,
            "connected_devices": 20,
            "avg_download_mbps": 75,
            "peak_usage_hours": 0,
        },

        {
            "network_name": "Library_WiFi",
            "rssi_dbm": -60,
            "signal_std_dbm": 4,
            "distance_to_ap_m": 60,
            "connected_devices": 35,
            "avg_download_mbps": 55,
            "peak_usage_hours": 0,
        },
    ]

    task = "gaming"

    candidates = filter_candidates(
        test_networks,
        task
    )

    print("=== WiSense Candidate Filtering ===")
    print()
    print(f"Selected task: {task}")
    print()

    if not candidates:

        print(
            "No suitable networks found."
        )

    else:

        print("Suitable networks:")

        for candidate in candidates:

            print(
                f"{candidate['network_name']} "
                f"-> "
                f"{candidate['suitability_score']}/100"
            )
