import requests
import datetime as dt

MY_LAT = 27.503561
MY_LONG = -99.507553

response = requests.get(url='http://api.open-notify.org/iss-now.json')
response.raise_for_status()
data = response.json()

iss_latitude = float(data['iss_position']["latitude"])
iss_longitude = float(data['iss_position']["longitude"])

parameters = {
  "lat": MY_LAT,
  "lng": MY_LONG,
  "formatted": 0
}

response = requests.get('https://api.sunrise-sunset.org/json', params=parameters)
response.raise_for_status()
data = response.json()
sunrise = int(data["results"]["sunrise"].split("T").split(':')[0])
sunset = int(data["results"]["sunset"].split("T").split(':')[0])

time_now = dt.datetime.now()