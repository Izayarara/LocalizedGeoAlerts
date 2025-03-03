import requests
import time
import asyncio
import os
from telegram import Bot
from datetime import datetime, timezone
from dotenv import load_dotenv  # To load API keys from a .env file

# Load environment variables
load_dotenv()
TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

bot = Bot(token=TELEGRAM_TOKEN)

# USGS Earthquake API endpoint
USGS_URL = "https://earthquake.usgs.gov/fdsnws/event/1/query"

def fetch_earthquake_data(region_bounds):
    params = {
        'format': 'geojson',
        'orderby': 'time',
        'limit': 5,
        'maxlatitude': region_bounds['max_lat'],
        'minlatitude': region_bounds['min_lat'],
        'maxlongitude': region_bounds['max_lon'],
        'minlongitude': region_bounds['min_lon']
    }

    response = requests.get(USGS_URL, params=params)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error fetching data: {response.status_code}")
        return None

async def send_telegram_alert(message):
    await bot.send_message(chat_id=CHAT_ID, text=message)

async def process_and_alert(region_bounds):
    data = fetch_earthquake_data(region_bounds)
    if data and "features" in data:
        for earthquake in data["features"]:
            magnitude = earthquake["properties"]["mag"]
            place = earthquake["properties"]["place"]
            time_epoch = earthquake["properties"]["time"]
            time_str = datetime.fromtimestamp(time_epoch / 1000, tz=timezone.utc).strftime('%Y-%m-%d %H:%M:%S')

            alert_message = (f"🚨 Earthquake Alert 🚨\n"
                             f"📍 Location: {place}\n"
                             f"🌍 Magnitude: {magnitude}\n"
                             f"⏰ Time: {time_str} UTC")

            await send_telegram_alert(alert_message)
            print(f"Sent alert for: {place} at {time_str}")

async def main():
    region_bounds = {
        'max_lat': 49.5,
        'min_lat': 46.0,
        'max_lon': -116.5,
        'min_lon': -124.0
    }
    
    while True:
        await process_and_alert(region_bounds)
        await asyncio.sleep(600)

if __name__ == "__main__":
    asyncio.run(main())
