# Rain_check
 Weather Alert System with WhatsApp Notification using OpenWeatherMap & UltraMsg
This project uses the OpenWeatherMap API to check the weather for a specific location (e.g., Indirapuram, India), and sends a WhatsApp alert using the UltraMsg API if rain or bad weather is expected.

📌 Features
Fetches real-time weather data using OpenWeatherMap

Identifies precipitation (rain, snow, drizzle, storms)

Sends a WhatsApp message alert if bad weather is detected

Sends a clear weather message otherwise

Fully automated via Python

🔧 Technologies Used
Python 3.x

OpenWeatherMap API (REST)

UltraMsg WhatsApp Messaging API

requests Python library

✅ Prerequisites
Before running the project, ensure you have:

Python 3.x installed

Internet connection

A registered phone number with WhatsApp

🔐 Account Setup
1. OpenWeatherMap API
🔗 Website: https://openweathermap.org/api

Create a free account

Go to your API keys section and copy your personal key

Use this key in your Python script as weather_api_key

2. UltraMsg WhatsApp API
🔗 Website: https://ultramsg.com

Sign up for a free UltraMsg account

Go to the Instances tab

Click "Create Instance"

Copy the following:

Instance ID (e.g., instance27983)

Token

Open your WhatsApp mobile app

Go to Settings → Linked Devices → Scan the QR code from UltraMsg dashboard

🧠 How It Works
The script requests current weather conditions from OpenWeatherMap for a given latitude and longitude.

It extracts the weather condition ID from the API response.

If the condition ID is less than 700, it indicates rain, snow, or storm — and sends a WhatsApp alert.

If not, it sends a clear weather message via WhatsApp.
