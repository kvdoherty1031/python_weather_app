import forecastio
from geopy.geocoders import Nominatim
import os
from slacker import Slacker
from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())

def get_weather(api_key_func, address):
	geolocator = Nominatim()
	loc = geolocator.geocode(address)
	forecast = forecastio.load_forecast(api_key_func, loc.latitude, loc.longitude)
	# print(forecast.currently().temperature)
	weather = 'Its %d degrees in Central Park right now' % forecast.currently().temperature
	return weather

	# slack.chat.post_message('#bots', weather, username="KD from OMPython", icon_url="https://s3.amazonaws.com/one-month-rails-production/assets/files/000/000/797/original/heavy_rain_showers.png")

# get_weather(api_key, address)

