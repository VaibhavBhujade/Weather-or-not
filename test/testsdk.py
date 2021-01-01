from weatherapi.weatherapi_client import WeatherapiClient
from weatherapi.api_helper import APIHelper

import constants
key = constants.API_SERVICE_KEY

from flask import Flask, render_template ,request, url_for, flash, redirect

app = Flask(__name__)
app.debug = True

@app.route('/', methods=('GET', 'POST'))
def index():
    if request.method == 'POST':
        q = request.form['place']
        lang = request.form['lang']
        weather_info = getWeather(q,lang)
        forecast_info = getForecast(q, 3)
        if(weather_info==None):
            q = "Mumbai"
            lang = "en"
            weather_info = getWeather(q,lang)
            forecast_info = getForecast(q, 3)
            return render_template('index.html', place=weather_info , forecast=forecast_info, error="Invalid place")
        return render_template('index.html', place=weather_info , forecast=forecast_info)
    q = "Mumbai"
    lang = "en"
    weather_info = getWeather(q,lang)
    forecast_info = getForecast(q, 3)
    return render_template('index.html', place=weather_info , forecast=forecast_info)


def getForecast(place, days):
    """
        Returns json Forecast by taking input of place anf number of days
    """

    #Create a client by passing the API key
    client = WeatherapiClient(key)
    ap_is_controller = client.ap_is
    #get forecast raw data
    try:
        forecast= ap_is_controller.get_forecast_weather(place,days)
    except:
        return
    #Convert data to python dictionary
    forecast_info=APIHelper.to_dictionary(forecast)
    return forecast_info


def getWeather(place, lang):
    """
        Returns realtime weather 
    """

    #Create a client by passing the API key
    client = WeatherapiClient(key)
    ap_is_controller = client.ap_is
    #get raw data for weather
    try:
        weather = ap_is_controller.get_realtime_weather(place, lang)
    except:
        return
    #Convert response to python dictionary
    weather_info = APIHelper.to_dictionary(weather)
    return weather_info


from nose.tools import *

@raises(Exception)
def test_weather_with_invalid_place(place="qqqww", lang="en"):
    #test with invalid place to check if it throws error
    client = WeatherapiClient(key)
    ap_is_controller = client.ap_is
    weather = ap_is_controller.get_realtime_weather(place, lang)
    del client

@raises(Exception)
def test_forecast_with_invalid_place(place="qqqq", lang="en"):
    #test with invalid place to check if it throws error
    client = WeatherapiClient(key)
    ap_is_controller = client.ap_is
    weather = ap_is_controller.get_realtime_weather(place, lang)
    del client

@timed(.9)
def test_time_Weather():
    #Test whether the Weather is retrieved within time
    getWeather("Mumbai","en")

@timed(.9)
def test_time_Forecast():
    #Test whether the Forecast is retrieved within time
    getForecast("Mumbai","en")








 