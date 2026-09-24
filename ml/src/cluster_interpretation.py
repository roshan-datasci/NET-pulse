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
    """Return cluster centers in original feature units."""

    model, scaler = load_models()

    centers_scaled = model.cluster_centers_

    centers_original = scaler.inverse_transform(
        centers_scaled
    )

    centers = pd.DataFrame(
        centers_original,
        columns=FEATURES
    )

    centers.index.name = "cluster"

    return centers


def interpret_clusters():
    """Assign semantic connectivity labels to clusters."""

    centers = get_cluster_centers()

    # Order clusters by observed download speed.
    # Cluster IDs themselves are arbitrary.
    ordered_clusters = (
        centers["avg_download_mbps"]
        .sort_values(ascending=False)
        .index
        .tolist()
    )

    labels = {}

    if len(ordered_clusters) >= 1:
        labels[ordered_clusters[0]] = "strong"

    if len(ordered_clusters) >= 2:
        labels[ordered_clusters[1]] = "moderate"

    if len(ordered_clusters) >= 3:
        labels[ordered_clusters[2]] = "weak"

    return centers, labels


if __name__ == "__main__":

    centers, labels = interpret_clusters()

    print("=== WiSense Connectivity Interpretation ===")
    print()

    for cluster_id in centers.index:

        print(
            f"Cluster {cluster_id}: "
            f"{labels[cluster_id]}"
        )

        print(
            f"  RSSI: "
            f"{centers.loc[cluster_id, 'rssi_dbm']:.2f} dBm"
        )

        print(
            f"  Download speed: "
            f"{centers.loc[cluster_id, 'avg_download_mbps']:.2f} Mbps"
        )

        print(
            f"  Distance: "
            f"{centers.loc[cluster_id, 'distance_to_ap_m']:.2f} m"
        )

        print(
            f"  Connected devices: "
            f"{centers.loc[cluster_id, 'connected_devices']:.2f}"
        )

        print()
