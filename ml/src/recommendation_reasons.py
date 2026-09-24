def generate_recommendation_reasons(observation):
    """
    Generate human-readable reasons explaining
    why a network is suitable.
    """

    reasons = []

    # Signal strength
    if observation["rssi_dbm"] >= -60:
        reasons.append("Strong signal")
    elif observation["rssi_dbm"] >= -70:
        reasons.append("Acceptable signal")
    else:
        reasons.append("Weak signal")

    # Download speed
    if observation["avg_download_mbps"] >= 50:
        reasons.append("Good download speed")
    elif observation["avg_download_mbps"] >= 25:
        reasons.append("Moderate download speed")
    else:
        reasons.append("Low download speed")

    # Congestion
    if observation["connected_devices"] <= 30:
        reasons.append("Low congestion")
    elif observation["connected_devices"] <= 60:
        reasons.append("Moderate congestion")
    else:
        reasons.append("High congestion")

    # Signal stability
    if observation["signal_std_dbm"] <= 3:
        reasons.append("Stable signal")
    elif observation["signal_std_dbm"] <= 6:
        reasons.append("Moderately stable signal")
    else:
        reasons.append("Unstable signal")

    return reasons


if __name__ == "__main__":

    test_network = {
        "network_name": "Sample_WiFi",
        "rssi_dbm": -50,
        "signal_std_dbm": 2,
        "distance_to_ap_m": 80,
        "connected_devices": 20,
        "avg_download_mbps": 75,
        "peak_usage_hours": 0,
    }

    reasons = generate_recommendation_reasons(
        test_network
    )

    print("=== WiSense Recommendation Reasons ===")
    print()

    print(
        f"Network: "
        f"{test_network['network_name']}"
    )

    print()

    print("Why this network?")

    for reason in reasons:
        print(f"• {reason}")
