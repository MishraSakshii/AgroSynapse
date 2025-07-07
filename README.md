# Agro-Geoinformation Crop Recommendation System

## Description
This project uses Google Earth Engine for satellite data, Firebase for cloud storage, and Flask for a simple crop recommendation web app.

## Setup Instructions

1. Clone/download the project
2. Install libraries: `pip install -r requirements.txt`
3. Add your Firebase key as `firebase_config.json`
4. Authenticate Earth Engine: `earthengine authenticate`
5. Run the app: `python main.py`
6. Visit: `http://127.0.0.1:5000`

## Inputs
- NDVI
- Rainfall
- Soil Moisture

## Output
- Recommended Crop
- Data stored to Firebase
