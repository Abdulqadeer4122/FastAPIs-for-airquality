# app/models/air_quality.py
from pydantic import BaseModel
from typing import Optional

class AirQualityData(BaseModel):
    Latitude: float
    Longitude: float
    pm25_level: float
