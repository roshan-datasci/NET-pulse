from recommendation_service import get_recommendation


observations = [
    {
        "network_name": "Network_A",
        "rssi_dbm": -55,
        "signal_std_dbm": 2.5,
        "distance_to_ap_m": 40,
        "connected_devices": 20,
        "avg_download_mbps": 70,
        "peak_usage_hours": 0,
    },
    {
        "network_name": "Network_B",
        "rssi_dbm": -68,
        "signal_std_dbm": 4.5,
        "distance_to_ap_m": 80,
        "connected_devices": 45,
        "avg_download_mbps": 35,
        "peak_usage_hours": 1,
    },
    {
        "network_name": "Network_C",
        "rssi_dbm": -78,
        "signal_std_dbm": 7.0,
        "distance_to_ap_m": 120,
        "connected_devices": 70,
        "avg_download_mbps": 12,
        "peak_usage_hours": 1,
    },
]


task = "gaming"

result = get_recommendation(
    observations,
    task
)

print("WiSense Recommendation")
print("------------------------")
print(f"Task: {result['task']}")
print(f"Status: {result['status']}")
print(f"Network: {result['network_name']}")
print(f"Suitability: {result['suitability_score']}/100")
print(f"Distance: {result['distance_to_ap_m']} m")

print("\nReasons:")

for reason in result["reasons"]:
    print(f"- {reason}")
