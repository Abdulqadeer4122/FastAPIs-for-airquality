# app/routes/air_quality.py
from fastapi import APIRouter, HTTPException
from typing import List, Optional
from app.schemas.schema import AirQualityData
from app.services.data_service import DataService

router = APIRouter()
data_service = DataService()

@router.get("/data", response_model=List[AirQualityData])
def get_all_data():
    return data_service.get_all_data()

@router.get("/data/{id}", response_model=AirQualityData)
def get_data_by_id(id: int):
    data = data_service.get_data_by_id(id)
    if not data:
        raise HTTPException(status_code=404, detail="Data not found")
    return data

@router.post("/data", response_model=AirQualityData)
def create_data(data: AirQualityData):
    return data_service.create_data(data)

@router.put("/data/{id}", response_model=AirQualityData)
def update_data(id: int, data: AirQualityData):
    updated_data = data_service.update_data(id, data)
    if not updated_data:
        raise HTTPException(status_code=404, detail="Data not found")
    return updated_data

@router.delete("/data/{id}")
def delete_data(id: int):
    if not data_service.delete_data(id):
        raise HTTPException(status_code=404, detail="Data not found")
    return {"detail": "Data deleted"}

@router.get("/data/filter")
def filter_data(lat: Optional[float] = None, long: Optional[float] = None):
    return data_service.filter_data(lat, long)

@router.get("/data/stats")
def get_stats():
    return data_service.get_stats()
