import requests
from datetime import datetime
from requests.auth import HTTPBasicAuth
import os

# API credentials
APP_ID = os.environ["NT_APP_ID"]
API_KEY = os.environ["NT_API_KEY"]

# User credentials
USER = os.environ["NT_USER"]
PASSWORD = os.environ["NT_PASSWORD"]

# Endpoint for exercise data
exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

# Get exercise input from user
exercise = input("What exercise you did: ")

# Endpoint for storing exercise data
sheety_endpoint = os.environ["SHEET_ENDPOINT"]

# Headers for the Nutritionix API
headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}

# Parameters for the exercise query
parameters = {
    "query": exercise,
    "gender": "male",
    "weight_kg": 78,
    "height_cm": 175,
    "age": 21
}

# Make a POST request to Nutritionix API to get exercise data
response = requests.post(exercise_endpoint, json=parameters, headers=headers)
result = response.json()

# Get current date and time
today = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")

# Prepare data for Sheety API
for exercise in result["exercises"]:
    sheety_inputs = {
        "workout": {
            "date": today,
            "time": now_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

# Authentication for Sheety API
basic = HTTPBasicAuth(USER, PASSWORD)

# Make a POST request to Sheety API to store exercise data
sheety_response = requests.post(sheety_endpoint, json=sheety_inputs, auth=basic)
print(sheety_response.text)
