from flask import Flask, render_template, request
from flask_bootstrap import Bootstrap
import requests

app = Flask(__name__)
Bootstrap(app)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        user_input = request.form['city']
        weather_data = get_weather_data(user_input)
        if weather_data['cod'] == '404':
            error_message = "City not found. Please enter a valid city."
            return render_template('index.html', error_message=error_message)
        else:
            weather = weather_data['weather'][0]['main']
            temp = round(weather_data['main']['temp'])
            humidity = weather_data['main']['humidity']
            wind_speed = weather_data['wind']['speed']
            description = weather_data['weather'][0]['description']
            return render_template('index.html', city=user_input, weather=weather, temperature=temp,
                                   humidity=humidity, wind_speed=wind_speed, description=description)
    return render_template('index.html')

def get_weather_data(city):
    api_key = '30d4741c779ba94c470ca1f63045390a'
    weather_data = requests.get(
        f"https://api.openweathermap.org/data/2.5/weather?q={city}&units=imperial&APPID={api_key}").json()
    print("Weather Data:", weather_data) 
    return weather_data

if __name__ == '__main__':
    app.run(debug=True)