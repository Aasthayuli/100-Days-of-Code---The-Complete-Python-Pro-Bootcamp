import requests
from datetime import datetime

# response = requests.get(url="http://api.open-notify.org/iss-now.json")
# response.raise_for_status()
# data = response.json()
# print(data)
# msg = response.json()["message"]
# print(msg)
# position = response.json()["iss_position"]
# print(position)
# latitude = response.json()["iss_position"]["latitude"]
# print(latitude)

MY_LAT = 25.874460
MY_LONG = 86.593063


parameters = {
    "lat":MY_LAT,
    "lng":MY_LONG,
    "formatted":0,
}

response = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data= response.json()
sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])
time_now = datetime.now()

