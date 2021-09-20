import requests
import tkinter as t

window = t.Tk()
window.title('CITY WEATHER')
window.geometry("500x500")

api_key = "PLACE YOUR API KEY HERE"
url = "http://api.openweathermap.org/data/2.5/weather?"

text = t.Text(window, font=("Calibri", 20), height = 7, width = 500)
text.pack()

def weather():
    city = text.get("1.0", "end-1c")
    full_url = url + "q=" + city + "&appid=" + api_key
    content = requests.get(full_url)
    info = content.json()

    if info["cod"] == "404":
        box.config(text="City not found!")
    else:
        x = info["main"]
        temperature = round((x["temp"] - 273.15), 2)
        pressure = x["pressure"]
        humidity = x["humidity"]
        z = info["weather"]
        weather_description = z[0]["description"]

        s = ""
        s += "Temperature: " + str(temperature) + " C \n"
        s += "Humidity: " + str(humidity) + " % \n"
        s += "Weather description: " + weather_description
        box.config(text=s)


submit = t.Button(window, text=" SEARCH ", command=weather, bg="green", fg="black", font=("Calibri", 20))
submit.pack()

box = t.Label(window, bg="black", fg="yellow", font=("Calibri", 20), height = 7, width = 500)
box.pack(side=t.LEFT)
t.mainloop()
