from fastapi import FastAPI
# from app.routes.v1 import sensor_routes
# from app.services.mqtt_service import mqtt_client, connect_mqtt

app = FastAPI(title="Sample IoT Backend")


@app.get("/")
async def root():
    print("OK")
    return {"message": "You're not alone"}


# Include routes
# app.include_router(sensor_routes.router, prefix="/api/v1/sensors")


"""
@app.on_event("startup")
async def startup_event():
    await connect_mqtt()
    print("MQTT connected")


@app.on_event("shutdown")
async def shutdown_event():
    await mqtt_client.disconnect()
"""
