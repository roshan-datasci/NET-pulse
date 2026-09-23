import os

import joblib
import pandas as pd

from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler


DATASET_PATH = "data/synthetic/wifi_observations.csv"

MODEL_PATH = "ml/models/kmeans_model.joblib"
SCALER_PATH = "ml/models/scaler.joblib"


FEATURES = [
    "rssi_dbm",
    "signal_std_dbm",
    "distance_to_ap_m",
    "connected_devices",
    "avg_download_mbps",
    "peak_usage_hours",
]


def train_model():
    """Train K-Means and save the model and scaler."""

    # Load dataset
    df = pd.read_csv(DATASET_PATH)

    # Select ML features
    X = df[FEATURES]

    # Standardize features
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    # Create K-Means model
    model = KMeans(
        n_clusters=3,
        random_state=42,
        n_init=10
    )

    # Train the model
    model.fit(X_scaled)

    # Make sure the model directory exists
    os.makedirs("ml/models", exist_ok=True)

    # Save trained K-Means model
    joblib.dump(
        model,
        MODEL_PATH
    )

    # Save the scaler used during training
    joblib.dump(
        scaler,
        SCALER_PATH
    )

    print("=== WiSense Model Training ===")
    print()

    print(f"Training observations: {len(df)}")
    print()

    print(f"Features: {FEATURES}")
    print()

    print(f"Clusters: {model.n_clusters}")
    print()

    print(
        f"Saved K-Means model to: "
        f"{MODEL_PATH}"
    )

    print(
        f"Saved scaler to: "
        f"{SCALER_PATH}"
    )


if __name__ == "__main__":
    train_model()