import requests

api_key = "PLACE YOUR API KEY HERE"
url = "http://api.openweathermap.org/data/2.5/weather?"

city = input("Enter city name : ")

full_url = url + "q=" + city + "&appid=" + api_key
content = requests.get(full_url)
info = content.json()

# print(info)

if info["cod"] == "404":
    print(" City Not Found ")
else:
    x = info["main"]
    temperature = round((x["temp"] - 273.15), 2)  # kelvin to degrees
    pressure = x["pressure"]
    humidity = x["humidity"]
    z = info["weather"]
    weather_description = z[0]["description"]

    print("Temperature: " + str(temperature) + " C")
    print("Humidity: " + str(humidity) + " %")
    print("Weather description:", weather_description)
