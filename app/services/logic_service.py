"""
from app.services import db_service
from app.models.mcu import SensorData


async def process_sensor_data(data: dict):
    sensor = SensorData(**data)
    db_service.insert_sensor(sensor.dict())
    # could add extra logic (stats, alerts, etc.)
"""
