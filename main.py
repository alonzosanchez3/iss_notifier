import requests
import datetime as dt
import smtplib


MY_LAT = 27.503561
MY_LONG = -99.507553

def is_iss_overhead():

  response = requests.get(url='http://api.open-notify.org/iss-now.json')
  response.raise_for_status()
  data = response.json()

  iss_latitude = float(data['iss_position']["latitude"])
  iss_longitude = float(data['iss_position']["longitude"])

  if MY_LAT - 5 <= iss_latitude and iss_latitude <= MY_LAT + 5:
    if MY_LONG - 5 <= iss_longitude and iss_longitude <= MY_LONG + 5:
      return True

def is_night():

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

  time_now = dt.datetime.now().hour

  if time_now >= sunset or time_now <= sunrise:
    return True

if is_iss_overhead() and is_night():
  with smtplib.SMTP('smtp.gmail.com') as connection:
    connection.starttls()
    connection.login('alonzosanchez3@gmail.com', '12345')
    connection.sendmail(from_addr='alonzosanchez3@gmail.com', to_addrs="alonzosanchez3@gmail.com", msg=f"Subject:ISS\n\nThe ISS is above you!")

#project done