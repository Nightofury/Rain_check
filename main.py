import requests

weather_api_key = 'YOUR API KEY'
weather_url = 'https://api.openweathermap.org/data/2.5/weather'

weather_params = {
    'lat': #YOUR LAAT#,
    'lon': ##YOUR LONG,
    'appid': weather_api_key,
    'units': 'metric'
}

# --- UltraMsg WhatsApp Setup ---
ultramsg_instance_id = 'YOUR INSTANCE'
ultramsg_token = 'YOUR_TOKEN'
receiver_phone = '+9199XXXXXXX9'  # Format: +

ultramsg_url = f"https://api.ultramsg.com/{ultramsg_instance_id}/messages/chat"

# --- Fetch Weather ---
response = requests.get(weather_url, params=weather_params)
response.raise_for_status()
weather_data = response.json()

weather_id = weather_data['weather'][0]['id']
description = weather_data['weather'][0]['description']

# --- Build Message Based on Weather ID ---
if weather_id < 700:
    message = f"☁️ Weather alert: {description.capitalize()} detected in Indirapuram.\nDon't forget to bring an umbrella!"
else:
    message = f"🌤️ Today's weather: {description.capitalize()} in Indirapuram.\nNo umbrella needed — enjoy your day!"

# --- Send WhatsApp Message ---
payload = {
    "token": ultramsg_token,
    "to": receiver_phone,
    "body": message
}

send_response = requests.post(ultramsg_url, data=payload)
send_response.raise_for_status()

print("✅ WhatsApp message sent.")
print("API response:", send_response.text)