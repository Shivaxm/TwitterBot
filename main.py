import tweepy
import requests

allKeys = open('twitterkeys', 'r').read().splitlines()
apiKey = allKeys[0]
apiKeySecret = allKeys[1]
accessToken = allKeys[2]
accessTokenSecret = allKeys[3]

authenticator = tweepy.OAuthHandler(apiKey, apiKeySecret)
authenticator.set_access_token(accessToken, accessTokenSecret)

api = tweepy.API(authenticator, wait_on_rate_limit=True)

BASE_URL = "https://api.openweathermap.org/data/2.5/weather?"
weatherAPI_KEY = allKeys[4]
CITY = "Philadelphia"

def kelvinToCelsius(kelvin):
    fahrenheit = (kelvin - 273.15) * 9/5 + 32
    return fahrenheit

url = BASE_URL + "appid=" + weatherAPI_KEY + "&q=" + CITY
response = requests.get(url).json()
temp_kelvin = response['main']['temp']
temp_f = kelvinToCelsius(temp_kelvin)

twit_text = "Temperature in " + CITY + ": " + str(round(temp_f, 2)) + "° Fahrenheit"
api.update_status(twit_text)
