# WiSense

## Intelligent Wi-Fi Analysis and Recommendation System

WiSense is a connectivity analysis and recommendation system that evaluates available Wi-Fi observations and recommends the network that is most suitable for a user's intended activity.

Instead of relying on signal strength alone, WiSense considers multiple connectivity factors such as:

- Signal strength (RSSI)
- Signal stability
- Download throughput
- Network congestion
- Usage conditions
- Distance to the access point

The system combines **unsupervised machine learning**, transparent connectivity scoring, and task-based recommendation to help users choose a suitable available network.

> **Example:** A user selects **Gaming**, and WiSense evaluates the available networks and recommends the one with the strongest overall suitability for that activity.

---

## Problem Statement

Users may have access to multiple Wi-Fi networks but experience different connectivity quality depending on signal conditions, congestion, throughput, and location.

Signal strength alone does not always represent the overall quality of a connection. A network with a strong signal may still perform poorly when it is highly congested, while another network with a weaker signal may provide better throughput and stability.

WiSense aims to analyze multiple connectivity observations, discover connectivity patterns using unsupervised learning, calculate a transparent suitability score, and recommend an appropriate network based on the user's intended activity.

---

## How WiSense Works

The current system follows this pipeline:

Wi-Fi Observations
        |
        v
Data Validation & Preprocessing
        |
        v
Feature Preparation
       / \
      /   \
     v     v
K-Means   Suitability
Clustering  Score
     |         |
     v         v
Cluster    Task-Based
Interpretation Filtering
       \       /
        \     /
         v   v
     Network Ranking
           |
           v
Recommendation + Reasons