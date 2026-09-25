from typing import Literal

from pydantic import BaseModel

class NetworkObservation(BaseModel):
    network_name: str
    rssi_dbm: float
    signal_std_dbm: float
    distance_to_ap_m: float
    connected_devices: int
    avg_download_mbps: float
    peak_usage_hours: int


class RecommendationRequest(BaseModel):
    task: Literal[
        "general",
        "browsing",
        "social_media",
        "video_call",
        "download",
        "gaming",
    ]
    networks: list[NetworkObservation]