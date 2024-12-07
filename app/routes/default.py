from flask import render_template
from app import app
import requests
import jsonify


@app.get("/")
def login_page():
    return render_template("login.html")


@app.get("/home")
def home_page():
    return render_template("index.html",
                            menu="Меню",
                            title="Oderman",
                            number="Номер телефону: +1 234 567 890")


@app.get("/weather")
def weather_page():
    weather_data = get_weather()
    if isinstance(weather_data, dict):
        extracted_data = extract_weather_data(weather_data)
    else:
        extracted_data = None
    return render_template("weather.html", weather=extracted_data)


def get_weather():
    url = 'http://api.openweathermap.org/data/2.5/weather?q=Kyiv&appid=72ec0d753684ed7bd284309b8cc2f720&units=metric'
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return None


def extract_weather_data(weather_data):
    main = weather_data["main"]
    extracted_data_def = {
        "temp": main["temp"],
        "feels_like": main["feels_like"],
        "temp_min": main["temp_min"],
        "temp_max": main["temp_max"],
        "weather_main": weather_data["weather"][0]["main"],
        "weather_description": weather_data["weather"][0]["description"],
        "wind_speed": weather_data["wind"]["speed"],
        "clouds": weather_data["clouds"]["all"],
    }
    return extracted_data_def
