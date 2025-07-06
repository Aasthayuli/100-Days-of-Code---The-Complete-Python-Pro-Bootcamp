import os
import requests
from twilio.rest import Client


OMW_Endpoint = "https://api.openweathermap.org/data/2.5/forecast"
api_key = "671cbbd25ec6086aaf2664044e7b93d4"

account_sid = os.environ.get("TWILIO_ACCOUNT_SID")

auth_token = 'a5c53dee5f96f347f991467284a31459'

weather_params ={
    "lat":21.462448,
    "lon":80.220978,
    "appid":api_key,
    "cnt":4,
}
response = requests.get(OMW_Endpoint,params=weather_params)
response.raise_for_status()
weather_data = response.json()

# print(weather_data["list"][0]["weather"][0]["id"])

will_rain = False
for hour_data in weather_data["list"]:
    condition_code = int(hour_data["weather"][0]["id"])
    if condition_code < 700:
        will_rain = True
if will_rain:
    print("Bring an Umbrella.")
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        messaging_service_sid='MG4b71851572c9c52cb6c1a68f20300cdb',
        body="It's going to rain today. Remember to bring an umbrella",
        to='+919576357966'
    )
    print(message.status)

