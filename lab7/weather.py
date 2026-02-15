import requests
import json
api_key = '2eca31d854ea1a5e0dc43636f66132e6'
city_name = input('Enter your city name (default - Saint-Petersburg): ')
if city_name == "":
    city_name = "Saint-Petersburg"
resp_coord = requests.get(f"http://api.openweathermap.org/geo/1.0/direct?q={city_name}&appid={api_key}")
lat = resp_coord.json()[0]["lat"]
lon = resp_coord.json()[0]["lon"]
resp_weather = requests.get(f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api_key}")
weather_data = resp_weather.json()
print("-"*10,"Weather in", city_name, "-"*10)
print("Weather: ", weather_data["weather"][0]["main"])
print("Pressure: ", weather_data["main"]["pressure"], "bar")
print("Humidity: ", weather_data["main"]["humidity"], "%")