# 🌋 Localized GeoQuake Alerts – Earthquake & Volcano Alert Bot  

🚀 **GeoQuake Alerts** is an open-source Telegram bot that fetches real-time earthquake data from USGS and sends alerts directly to your chat.  

## 🔥 Features  
✅ Fetches real-time **earthquake data** from USGS  
✅ Sends **Telegram alerts** for recent seismic activity  
✅ Customizable **location filters** (default: Washington, USA)  
✅ Runs **continuously** with automatic updates every 10 minutes  

---

## 🛠️ Setup & Installation  

### **1️⃣ Clone the Repository**  
```sh
git clone https://github.com/Izayarara/LocalizedGeoAlerts.git
cd geoquake-alerts
2️⃣ Install Dependencies
Ensure you have Python installed, then run:

sh
Copy
Edit
pip install python-telegram-bot requests python-dotenv
3️⃣ Set Up API Keys
Create a .env file inside the project folder and add:

ini
Copy
Edit
TELEGRAM_TOKEN=your_telegram_bot_token_here
CHAT_ID=your_chat_id_here
💡 Tip: You can get your CHAT_ID by messaging @userinfobot on Telegram.

4️⃣ Run the Bot
sh
Copy
Edit
python geolerts.py
The bot will check for earthquakes every 10 minutes and send alerts if new events occur.

⚙️ Customization
Change the Monitored Location
Modify these values in geolerts.py:

python
Copy
Edit
region_bounds = {
    'max_lat': 49.5,  # Max latitude (North)
    'min_lat': 46.0,  # Min latitude (South)
    'max_lon': -116.5, # Max longitude (East)
    'min_lon': -124.0  # Min longitude (West)
}
Change them to your preferred region! 🌍

Adjust Update Frequency
In geolerts.py, modify the interval (in seconds):

python
Copy
Edit
await asyncio.sleep(600)  # 600 seconds = 10 minutes
📜 License
This project is open-source under the MIT License.
