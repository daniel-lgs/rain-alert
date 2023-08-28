import requests
import smtplib

# Relative to the Weather API
WEATHER_API_KEY = "__YOUR_OWN_API__"
LATITUDE = "__YOUR_OWN_LATITUDE__"
LONGITUDE = "__YOUR_OWN_LONGITUDE__"
# ---------------------------

# Relative to the email sender
EMAIL_SENDER = "__YOUR_OWN_EMAIL_SENDER__"
PASSWORD = "__YOUR_OWN_APP_PASSWORD__"  # Use app passwords > https://support.google.com/mail/answer/185833?hl=en\n"
RECEIVER_EMAIL = "__YOUR_OWN_RECEIVER_EMAIL__"
MESSAGE = "Subject: Weather Alert\n\nIn the next 12 hours it will rain."
# ----------------------------

rain_in_next12h = False


def get_weather_data():
    parameters = {
        "lat": LATITUDE,
        "lon": LONGITUDE,
        "appid": WEATHER_API_KEY
    }
    response = requests.get(url="https://api.openweathermap.org/data/2.5/forecast", params=parameters)
    response.raise_for_status()
    data = response.json()
    return data


def send_email():
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=EMAIL_SENDER, password=PASSWORD)
        connection.sendmail(from_addr=EMAIL_SENDER, to_addrs=RECEIVER_EMAIL, msg=MESSAGE)


weather_data = get_weather_data()
next_12hours_data = weather_data["list"][0:4]
for each_forecast in next_12hours_data:
    if each_forecast["weather"][0]["main"] == "Rain":
        rain_in_next12h = True
        send_email()
        break
        
