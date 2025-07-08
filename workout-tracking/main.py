import os

import requests
from datetime import datetime
import os

GENDER = "female"
WEIGHT_KG = 46
HEIGHT_CM = 157
AGE = 23

APP_ID = os.environ["APP_ID"]
API_KEY = os.environ["APP_KEY"]
TOKEN = "Bearer"
SHEETY_TOKEN_KEY = os.environ["SHEET_KEY"]

exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

exercise_text = input("Tell me which exercises you did: ")

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
    "Content-Type": "application/json"
}

parameters = {
    "query": exercise_text,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}

# Get exercise data from Nutritionix
response = requests.post(exercise_endpoint, json=parameters, headers=headers)
result = response.json()
print(result)


sheety_headers={
    "Authorization":f"{TOKEN} {SHEETY_TOKEN_KEY}"
}
# For each exercise, send a POST to Sheety with the correct format
for exercise in result["exercises"]:
    sheet_inputs = {
        "workout": {
            "date": datetime.now().strftime("%d/%m/%Y"),
            "time": datetime.now().strftime("%X"),
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

    sheety_response = requests.post(
        url="https://api.sheety.co/9ca66b0704efc05867ce74ea42d77383/copyOfMyWorkouts/workouts",
        json=sheet_inputs,
        headers=sheety_headers
    )

    print(sheety_response.text)
