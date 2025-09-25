from fastapi import FastAPI
import os
from dotenv import load_dotenv
from supabase import create_client, Client
from supabase.client import ClientOptions
import psycopg2

load_dotenv()
app = FastAPI()


@app.get("/")
async def root():
    print("OK")
    return {"message": "You're not alone"}

url: str = os.environ.get("SUPABASE_URL")
key: str = os.environ.get("SUPABASE_KEY")

print(os.environ.get("SUPABASE_URL"))
supabase: Client = create_client(
    url,
    key,
    options=ClientOptions(
        postgrest_client_timeout=10,
        storage_client_timeout=10,
        schema="public",
    )
)

response = (
    supabase.table("Telemetry")
    .insert({"id": 1, "sensorValue": 123.45, "sensorName": "Voltage"})
    .execute()
)
