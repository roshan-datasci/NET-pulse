import joblib
import pandas as pd


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


def load_models():
    """Load the trained K-Means model and scaler."""

    model = joblib.load(MODEL_PATH)
    scaler = joblib.load(SCALER_PATH)

    return model, scaler


def get_cluster_centers():
    """Convert standardized cluster centers back to original units."""

    model, scaler = load_models()

    # Cluster centers produced by K-Means are in
    # standardized feature space.
    centers_scaled = model.cluster_centers_

    # Convert them back to the original feature units.
    centers_original = scaler.inverse_transform(
        centers_scaled
    )

    centers = pd.DataFrame(
        centers_original,
        columns=FEATURES
    )

    centers.index.name = "cluster"

    return centers


def inspect_cluster_centers():
    """Display cluster centers in real-world units."""

    centers = get_cluster_centers()

    print("=== WiSense Cluster Centers ===")
    print()

    print(
        centers.to_string()
    )


if __name__ == "__main__":
    inspect_cluster_centers()