# News and Weather API
# After entering in an API, the program will give you back News and Weather in your area

import requests


weather_key = "cc96d68c73cf139304a381905f85826e" 
news_key = "0ab27a701b0940ccbf34abef718528f7" 

city = input("City: ")

weather = requests.get(
    f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={weather_key}&units=metric").json()

print("\nWeather:")
print(weather["weather"][0]["description"])
print(str(weather["main"]["temp"]) + "°C")
