"""
from supabase import create_client
from app.core.config import settings

supabase = create_client(settings.SUPABASE_URL, settings.SUPABASE_KEY)


def insert_sensor(data: dict):
    return supabase.table("sensors").insert(data).execute()


def get_sensor_history(device_id: str):
    return supabase.table("sensors").select("*").eq("deviceId", device_id).execute()
"""

"""
from dotenv import load_dotenv
from supabase import create_client, Client
from supabase.client import ClientOptions

load_dotenv()

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
"""
