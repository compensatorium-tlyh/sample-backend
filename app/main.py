from fastapi import FastAPI
from contextlib import asynccontextmanager
from app.routes.v1.mcu_routes import router as mcu_routes

# from app.routes.v1 import sensor_routes
# from app.services.mqtt_service import mqtt_client, connect_mqtt


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup commands
    print("App initiated")
    yield  # Externally, yield may return something, but here mustn't
    # Shutdown commands
    print("App shut down")

app = FastAPI(title="Sample IoT Backend", lifespan=lifespan)

# Include routes
app.include_router(mcu_routes, prefix="/api/v1/mcu")

"""
@app.get("/")
async def root():
    return 
@app.on_event("startup")
async def startup_event():
    await connect_mqtt()
    print("MQTT connected")


@app.on_event("shutdown")
async def shutdown_event():
    await mqtt_client.disconnect()
"""
