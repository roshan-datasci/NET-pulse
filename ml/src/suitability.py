import pandas as pd


def normalize(value, minimum, maximum):
    """Convert a value to a 0-1 range."""

    if maximum == minimum:
        return 0.0

    normalized = (value - minimum) / (maximum - minimum)

    return max(0.0, min(1.0, normalized))


def calculate_suitability(observation):
    """
    Calculate a connectivity suitability score from 0 to 100.

    Higher scores indicate more suitable connectivity.
    """

    # RSSI:
    # -40 dBm is treated as very strong.
    # -90 dBm is treated as very weak.
    rssi_score = normalize(
        observation["rssi_dbm"],
        -90,
        -40
    )

    # Lower signal variation means a more stable signal.
    stability_score = 1 - normalize(
        observation["signal_std_dbm"],
        0,
        10
    )

    # Higher download speed is better.
    speed_score = normalize(
        observation["avg_download_mbps"],
        0,
        100
    )

    # Fewer connected devices generally means less congestion.
    congestion_score = 1 - normalize(
        observation["connected_devices"],
        0,
        100
    )

    # Non-peak periods receive a higher score.
    if observation["peak_usage_hours"] == 1:
        usage_score = 0.5
    else:
        usage_score = 1.0

    # Weighted suitability score.
    score = (
        0.25 * rssi_score
        + 0.15 * stability_score
        + 0.30 * speed_score
        + 0.20 * congestion_score
        + 0.10 * usage_score
    )

    return round(score * 100, 2)


if __name__ == "__main__":

    test_observations = {
        "Good connection": {
            "rssi_dbm": -50,
            "signal_std_dbm": 2.0,
            "distance_to_ap_m": 25,
            "connected_devices": 15,
            "avg_download_mbps": 80,
            "peak_usage_hours": 0,
        },

        "Moderate connection": {
            "rssi_dbm": -65,
            "signal_std_dbm": 5.0,
            "distance_to_ap_m": 70,
            "connected_devices": 45,
            "avg_download_mbps": 40,
            "peak_usage_hours": 0,
        },

        "Poor connection": {
            "rssi_dbm": -80,
            "signal_std_dbm": 8.0,
            "distance_to_ap_m": 120,
            "connected_devices": 85,
            "avg_download_mbps": 10,
            "peak_usage_hours": 1,
        },
    }

    print("=== WiSense Suitability Validation ===")
    print()

    for name, observation in test_observations.items():

        score = calculate_suitability(
            observation
        )

        print(f"{name}")
        print(f"  Suitability score: {score}/100")
        print()
