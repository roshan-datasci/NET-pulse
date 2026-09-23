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


def predict_cluster(observation):
    """Predict the connectivity cluster for one observation."""

    model = joblib.load(MODEL_PATH)
    scaler = joblib.load(SCALER_PATH)

    observation_df = pd.DataFrame(
        [observation],
        columns=FEATURES
    )

    observation_scaled = scaler.transform(
        observation_df
    )

    cluster = model.predict(
        observation_scaled
    )[0]

    return cluster


if __name__ == "__main__":

    new_observation = {
        "rssi_dbm": -55,
        "signal_std_dbm": 3.0,
        "distance_to_ap_m": 30,
        "connected_devices": 25,
        "avg_download_mbps": 50,
        "peak_usage_hours": 0,
    }

    cluster = predict_cluster(
        new_observation
    )

    print("=== WiSense Prediction ===")
    print()
    print("New Wi-Fi observation:")
    print(new_observation)
    print()
    print(f"Predicted cluster: {cluster}")