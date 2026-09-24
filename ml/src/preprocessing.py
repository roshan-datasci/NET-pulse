import pandas as pd
from sklearn.preprocessing import StandardScaler


DATASET_PATH = "data/synthetic/wifi_observations.csv"


FEATURES = [
    "rssi_dbm",
    "signal_std_dbm",
    "distance_to_ap_m",
    "connected_devices",
    "avg_download_mbps",
    "peak_usage_hours",
]


def load_dataset():
    """Load the synthetic Wi-Fi observation dataset."""
    return pd.read_csv(DATASET_PATH)


def prepare_features(df):
    """Select ML features and standardize them."""

    X = df[FEATURES]

    scaler = StandardScaler()

    X_scaled = scaler.fit_transform(X)

    return X_scaled, scaler


if __name__ == "__main__":

    df = load_dataset()

    X_scaled, scaler = prepare_features(df)

    print("=== WiSense Preprocessing ===")
    print()

    print(f"Dataset shape: {df.shape}")
    print(f"Selected features: {FEATURES}")
    print()

    print("Scaled feature shape:")
    print(X_scaled.shape)
    print()

    print("First 5 scaled observations:")
    print(X_scaled[:5])
