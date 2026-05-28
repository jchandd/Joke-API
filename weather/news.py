# News and Weather API
# After entering in an API, the program will give you back News and Weather in your area

import requests

weather_key = "cc96d68c73cf139304a381905f85826e"
news_key = "0ab27a701b0940ccbf34abef718528f7"

city = input("City: ")

# Weather request
weather = requests.get(
    f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={weather_key}&units=metric"
).json()

# Check if weather worked
if weather.get("cod") != 200: # If the code is not 200, there was an error
    print("Weather error:")
    print(weather.get("message"))
    exit()

print("\nWeather:")
print(weather["weather"][0]["description"]) # Weather description
print(str(weather["main"]["temp"]) + "°C")

# Country code
country = weather["sys"]["country"].lower()

# News request
news = requests.get( 
    f"https://newsapi.org/v2/top-headlines?country={country}&apiKey={news_key}"
).json()

print("\nNews:")

# Check if news worked
if news.get("status") == "ok" and news.get("articles"): # Check if there are articles
    for article in news["articles"][:5]:
        print("- " + article["title"])
else:
    print("No news found.")
    print(news)