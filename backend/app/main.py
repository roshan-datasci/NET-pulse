from fastapi import FastAPI

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