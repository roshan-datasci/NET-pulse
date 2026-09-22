# WiSense

## An Intelligent Wi-Fi Connectivity Recommendation System Using Unsupervised Learning

WiSense is a web-based connectivity recommendation system that analyzes Wi-Fi observations and geographic information to identify suitable connectivity conditions and recommend nearby locations with better connectivity.

The project combines:

- Unsupervised Machine Learning
- Wi-Fi connectivity analysis
- Geographic data
- Distance-based recommendation
- Web technologies

## Problem Statement

Students on college campuses may have access to multiple Wi-Fi networks but still experience poor or unstable connectivity depending on their physical location.

Signal strength alone does not always represent the actual quality of a connection. Factors such as network congestion, signal stability, throughput, access-point distance, and physical obstacles can affect connectivity.

WiSense aims to analyze these observations and identify connectivity patterns using unsupervised learning. The system can then combine these patterns with geographic information to recommend a suitable nearby location.

## Project Objectives

The main objectives of WiSense are:

1. Analyze Wi-Fi connectivity observations.
2. Identify connectivity patterns using K-Means clustering.
3. Represent connectivity conditions geographically.
4. Recommend suitable Wi-Fi networks or locations.
5. Consider geographic distance when selecting a suitable location.
6. Provide a simple web-based interface for users.
7. Explore how machine learning can be integrated into a practical application.

## Planned Machine Learning Approach

The core machine learning component uses **K-Means clustering**.

Potential features include:

- RSSI / signal strength
- Signal stability
- Download speed
- Connected device count
- Network usage
- Frequency
- Distance information where available

The clustering model will be evaluated using techniques such as the **Elbow Method** and **Silhouette Score**.

## Technology Stack

### Backend
- Python
- FastAPI
- Uvicorn

### Machine Learning
- pandas
- NumPy
- scikit-learn
- Matplotlib
- Seaborn

### Frontend
- React
- Vite
- Tailwind CSS

### Geographic Features
- Leaflet
- OpenStreetMap
- GPS/location data

### Database
- SQLite

## Project Structure

```text
WiSense/
├── backend/
├── frontend/
├── ml/
├── data/
├── docs/
├── scripts/
├── requirements.txt
├── README.md
└── LICENSE