from fastapi import FastAPI

from backend.app.models.recommendation import RecommendationRequest
from ml.src.recommendation_service import get_recommendation


app = FastAPI(
    title="WiSense API",
    description="Backend API for the WiSense connectivity recommendation system",
    version="0.1.0"
)


@app.get("/")
def root():
    return {
        "message": "Welcome to WiSense API",
        "status": "running"
    }


@app.get("/health")
def health_check():
    return {
        "status": "healthy"
    }


@app.post("/recommend")
def recommend(request: RecommendationRequest):
    observations = [
        network.model_dump()
        for network in request.networks
    ]

    result = get_recommendation(
        observations,
        request.task
    )

    return result