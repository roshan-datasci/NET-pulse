from candidate_filter import filter_candidates
from recommendation import recommend_network


def main():

    observations = [
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

        {
            "network_name": "Weak_WiFi",
            "rssi_dbm": -82,
            "signal_std_dbm": 8,
            "distance_to_ap_m": 30,
            "connected_devices": 85,
            "avg_download_mbps": 10,
            "peak_usage_hours": 1,
        },
    ]

    task = "gaming"

    print("=== WiSense End-to-End Test ===")
    print()
    print(f"Selected task: {task}")
    print()

    candidates = filter_candidates(
        observations,
        task
    )

    print("Suitable candidates:")
    print()

    for candidate in candidates:

        print(
            f"{candidate['network_name']}: "
            f"{candidate['suitability_score']}/100 "
            f"({candidate['distance_to_ap_m']} m)"
        )

    print()

    recommendation = recommend_network(
        candidates
    )

    if recommendation is None:

        print(
            "No suitable network found."
        )

    else:

        print("=== FINAL RECOMMENDATION ===")
        print()

        print(
            f"🎯 Recommended network: "
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


if __name__ == "__main__":
    main()
