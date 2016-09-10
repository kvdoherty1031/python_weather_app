from flask import Flask, render_template, request
from weather_stuff import *
import os
app = Flask(__name__)

from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())

@app.route("/")
def index():
	api_key =os.environ['FORECAST_API_KEY']
	zipcode = request.values.get('zipcode')
	weather = None
	if zipcode:
		weather = get_weather(api_key, zipcode)
	return render_template('index.html', weather=weather)

@app.route("/about")
def about():
	return render_template('about.html')

if __name__ == "__main__":
    app.run()