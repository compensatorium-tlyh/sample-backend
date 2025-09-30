"""
from pydantic import BaseModel
from datetime import datetime


class SensorData(BaseModel):
    timestamp: datetime
    deviceId: str
    sensorId: str
    value: float


class ActuatorCommand(BaseModel):
    timestamp: datetime
    clientId: str
    actuatorId: str
    value: float
"""
