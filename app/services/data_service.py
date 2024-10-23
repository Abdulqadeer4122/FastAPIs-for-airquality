# app/services/data_service.py
import pandas as pd
from app.schemas.schema import AirQualityData


class DataService:
    def __init__(self):
        # Load the dataset into memory
        self.data = pd.read_csv("/home/datics/datasets/pm25_data.csv")
        self.data_records = self.data.to_dict(orient="records")

    def get_all_data(self):
        return self.data_records

    def get_data_by_id(self, id: int):
        if id < 0 or id >= len(self.data_records):
            return None
        return self.data_records[id]

    def create_data(self, data: AirQualityData):
        new_record = data.dict()
        self.data_records.append(new_record)
        return new_record

    def update_data(self, id: int, data: AirQualityData):
        if id < 0 or id >= len(self.data_records):
            return None
        self.data_records[id] = data.dict()
        return self.data_records[id]

    def delete_data(self, id: int):
        if id < 0 or id >= len(self.data_records):
            return False
        del self.data_records[id]
        return True

    def filter_data(self, lat: float = None, long: float = None):
        filtered_data = self.data_records
        if lat is not None:
            filtered_data = [d for d in filtered_data if d['Latitude'] == lat]
        if long is not None:
            filtered_data = [d for d in filtered_data if d['Longitude'] == long]
        return filtered_data

    def get_stats(self):
        pm25_levels = [d['pm25_level'] for d in self.data_records]
        return {
            "count": len(pm25_levels),
            "average": sum(pm25_levels) / len(pm25_levels) if pm25_levels else 0,
            "min": min(pm25_levels) if pm25_levels else 0,
            "max": max(pm25_levels) if pm25_levels else 0
        }
