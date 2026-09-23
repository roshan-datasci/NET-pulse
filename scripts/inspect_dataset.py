import pandas as pd


DATASET_PATH = "data/synthetic/wifi_observations.csv"


def inspect_dataset():
    df = pd.read_csv(DATASET_PATH)

    print("=== WiSense Dataset Inspection ===")
    print()

    print(f"Rows: {len(df)}")
    print(f"Columns: {len(df.columns)}")
    print()

    print("=== Data Types ===")
    print(df.dtypes)
    print()

    print("=== Missing Values ===")
    print(df.isnull().sum())
    print()

    print("=== Numeric Summary ===")
    print(df.describe())
    print()

    print("=== Network Distribution ===")
    print(df["network_name"].value_counts())
    print()

    print("=== Correlation with Download Speed ===")

    numeric_columns = [
        "rssi_dbm",
        "signal_std_dbm",
        "distance_to_ap_m",
        "connected_devices",
        "avg_download_mbps",
        "peak_usage_hours",
        "frequency_mhz",
    ]

    print(
        df[numeric_columns]
        .corr()["avg_download_mbps"]
        .sort_values(ascending=False)
    )


if __name__ == "__main__":
    inspect_dataset()