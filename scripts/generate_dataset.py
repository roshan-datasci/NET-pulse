import numpy as np
import pandas as pd


# Make the generated dataset reproducible
np.random.seed(42)


# Number of observations to generate
NUM_OBSERVATIONS = 1000


# Example Wi-Fi networks
NETWORKS = [
    "Network_A",
    "Network_B",
    "Network_C",
    "Network_D",
]


def generate_dataset():
    observations = []

    for observation_id in range(1, NUM_OBSERVATIONS + 1):

        # Select a random Wi-Fi network
        network_name = np.random.choice(NETWORKS)

        # Generate a location inside a fictional area
        latitude = 13.0827 + np.random.uniform(-0.002, 0.002)
        longitude = 80.2707 + np.random.uniform(-0.002, 0.002)

        # Approximate distance from the access point
        distance_to_ap = np.random.uniform(5, 150)

        # RSSI generally becomes weaker with distance.
        # Random noise represents walls, interference, antennas, etc.
        rssi = -45 - (distance_to_ap * 0.25)
        rssi += np.random.normal(0, 5)

        # Keep RSSI within a realistic range
        rssi = np.clip(rssi, -90, -40)

        # Signal stability
        signal_std = np.random.uniform(1, 8)

        # Number of connected devices
        connected_devices = np.random.randint(3, 80)

        # Peak usage indicator
        peak_usage_hours = np.random.choice(
            [0, 1],
            p=[0.6, 0.4]
        )

        # Approximate download speed.
        # Higher signal generally helps, while more connected
        # devices and peak usage can reduce available throughput.
        base_speed = 100

        signal_factor = (rssi + 90) / 50
        congestion_factor = 1 - (connected_devices / 120)

        speed = (
            base_speed
            * signal_factor
            * congestion_factor
        )

        if peak_usage_hours == 1:
            speed *= 0.75

        # Add realistic measurement variation
        speed += np.random.normal(0, 8)

        # Prevent impossible values
        speed = max(speed, 1)

        # Common Wi-Fi frequency bands
        frequency_mhz = np.random.choice(
            [2400, 5000]
        )

        # Generate a timestamp
        timestamp = pd.Timestamp("2026-01-01") + pd.to_timedelta(
            np.random.randint(0, 30 * 24 * 60),
            unit="m"
        )

        observations.append({
            "observation_id": observation_id,
            "network_name": network_name,
            "latitude": round(latitude, 6),
            "longitude": round(longitude, 6),
            "rssi_dbm": round(rssi, 2),
            "signal_std_dbm": round(signal_std, 2),
            "distance_to_ap_m": round(distance_to_ap, 2),
            "connected_devices": connected_devices,
            "avg_download_mbps": round(speed, 2),
            "peak_usage_hours": peak_usage_hours,
            "frequency_mhz": frequency_mhz,
            "timestamp": timestamp,
        })

    return pd.DataFrame(observations)


if __name__ == "__main__":

    df = generate_dataset()

    output_path = "data/synthetic/wifi_observations.csv"

    df.to_csv(output_path, index=False)

    print(f"Generated {len(df)} Wi-Fi observations.")
    print(f"Saved dataset to: {output_path}")
    print()
    print(df.head())