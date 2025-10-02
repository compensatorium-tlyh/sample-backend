from fastapi import APIRouter

router = APIRouter()


@router.get("/summary")
async def summarize():
    return {"message": "You're not alone"}

"""
from app.models.mcu import SensorData, ActuatorCommand
from app.services import db_service, mqtt_service



@router.post("/data")
async def save_sensor(sensor: SensorData):
    db_service.insert_sensor(sensor.dict())
    return {"status": "ok"}


@router.get("/history/{device_id}")
async def get_history(device_id: str):
    result = db_service.get_sensor_history(device_id)
    return result.data


@router.post("/command")
async def send_command(cmd: ActuatorCommand):
    await mqtt_service.publish(f"devices/{cmd.clientId}/commands", cmd.dict())
    return {"status": "sent"}

"""
