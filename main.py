import requests
import os
from twilio.rest import Client

# Set the API and AUT token in the OS Environment
api_key = os.environ.get("OWM_API")
account_sid = "AC6422b3f7002bc04ec38fda00bcc5f356"
auth_token = os.environ.get("AUTH_TOK")
# api.openweathermap.org/data/2.5/forecast?lat={lat}&lon={lon}&appid={API key}
params_input = {
    'lat': '41.499321',
    'lon': '-81.694359',
    'appid': api_key,
    'cnt': 4,
}

def call_weather():
    """
    This function will send the message to if it rains
    """
    lat = requests.get(url='https://api.openweathermap.org/data/2.5/forecast', params=params_input)
    lat.raise_for_status()
    data=lat.json()
    for hour in data['list']:
        condition_code = (hour['weather'][0]['id'])
        if int(condition_code) < 700:
            will_rain = True
    if will_rain:
        client = Client(account_sid, auth_token)
        message = client.messages \
                    .create(
                        body="It's going to rain. Remember to Bring Umbrella ☂️.",
                        from_='+18446070316',
                        to='Your Number'
                    )
        print(message.status)
        

call_weather()

