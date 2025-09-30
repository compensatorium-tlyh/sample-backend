"""
import asyncio
from gmqtt import Client as MQTTClient
from app.core.config import settings
from app.services import db_service, logic_service
import json

mqtt_client = MQTTClient("fastapi-backend")


def on_connect(client, flags, rc, properties):
    print("Connected to MQTT broker")
    client.subscribe("devices/+/sensors", qos=1)  # listen for all devices


def on_message(client, topic, payload, qos, properties):
    data = json.loads(payload)
    asyncio.create_task(logic_service.process_sensor_data(data))


async def connect_mqtt():
    mqtt_client.on_connect = on_connect
    mqtt_client.on_message = on_message
    await mqtt_client.connect(
        host=settings.MQTT_BROKER,
        port=settings.MQTT_PORT,
        ssl=False,
        keepalive=60,
        username=settings.MQTT_USERNAME,
        password=settings.MQTT_PASSWORD
    )


async def publish(topic: str, message: dict):
    mqtt_client.publish(topic, json.dumps(message), qos=1)
"""
