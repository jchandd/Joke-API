# News and Weather API
# After entering in an API, the program will give you back News and Weather in your area

import requests


weather_key = "cc96d68c73cf139304a381905f85826e" 
news_key = "0ab27a701b0940ccbf34abef718528f7" 

city = input("City: ")

weather = requests.get( # Get weather data from OpenWeatherMap API
    f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={weather_key}&units=metric").json() # Convert the response to JSON format

print("\nWeather:")
print(weather["weather"][0]["description"]) # Weather description
print(str(weather["main"]["temp"]) + "°C")

country = weather["sys"]["country"].lower()


news = requests.get(
    f"https://newsapi.org/v2/top-headlines?country={country}&apiKey={news_key}"
).json()

print("\nNews:")

for article in news["articles"][:5]: # Print the top 5 news articles
    print("- " + article["title"]) 