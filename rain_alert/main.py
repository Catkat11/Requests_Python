import requests
from twilio.rest import Client

# OpenWeatherMap API endpoint
OWM_Endpoint = "https://api.openweathermap.org/data/2.5/forecast"

# Twilio authentication credentials
account_sid = "sid"
auth_token = "auth_token"

# API key for accessing OpenWeatherMap data
api_key = "api_key"

# Parameters for requesting weather data
weather_params = {
    "lat": 50.128250,
    "lon": 18.988600,
    "appid": api_key
}

# Request weather forecast from OpenWeatherMap API
response = requests.get(OWM_Endpoint, params=weather_params)
response.raise_for_status()

# Extract weather data from the response
weather_data = response.json()
weather_slice = weather_data["list"][:4]

# Check if it will rain within the next 4 hours
will_rain = False
for hour_data in weather_slice:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True

# If rain is predicted, send a notification via Twilio
if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body="It's going to rain today. Remember to bring an umbrella",
        from_="+15737495194",
        to="+48666666666"
    )
    print(message.status)  # Print the status of the message delivery
