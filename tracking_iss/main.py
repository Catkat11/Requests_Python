import requests  # HTTP requests
from datetime import datetime  # Date and time handling
import smtplib  # Email notifications
import time  # Time delays

MY_LAT = 50.128250  # Observer's latitude
MY_LONG = 18.988600  # Observer's longitude
MY_EMAIL = "mail"  # Sender's email
MY_PASSWORD = "password"  # Sender's email password


def positioning():
    # Check if the ISS is near the observer's location.
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()
    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])
    return (MY_LONG - 5) <= iss_longitude <= (MY_LONG + 5) and (MY_LAT - 5) <= iss_latitude <= (MY_LAT + 5)


def is_night():
    # Check if it is currently night time at the observer's location.
    parameters = {"lat": MY_LAT, "lng": MY_LONG, "formatted": 0}
    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    time_now = datetime.now().hour
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])
    return time_now >= sunset or time_now <= sunrise


while True:
    time.sleep(60)  # Delay for 60 seconds before checking again
    if positioning() and is_night():
        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(MY_EMAIL, MY_PASSWORD)
            connection.sendmail(from_addr=MY_EMAIL,
                                to_addrs=MY_EMAIL,
                                msg=f"Subject:ISS OVER YOUR HEAD!!!\n\n"
                                    f"Hi!\nISS is now over your head and you can see it!")
