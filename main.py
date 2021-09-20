# send http request using python
import requests
import tkinter as t

# creating window with title
window = t.Tk()
window.title('CITY WEATHER')
window.geometry("500x500")

api_key = "0f58bcad68872a7810670c2a0037e298"
url = "http://api.openweathermap.org/data/2.5/weather?"

# textbox for user input
text = t.Text(window, font=("Calibri", 20), height = 7, width = 500)
text.pack()

def weather():
    # access text from: first line 0th index character, up to last_character-1 index as last character is newline
    city = text.get("1.0", "end-1c")
    full_url = url + "q=" + city + "&appid=" + api_key
    content = requests.get(full_url)
    # convert content to jason format
    info = content.json()
    # print(info)

    if info["cod"] == "404":
        box.config(text="City not found!")
    else:
        x = info["main"]
        temperature = round((x["temp"] - 273.15), 2)  # kelvin to degrees
        pressure = x["pressure"]
        humidity = x["humidity"]
        z = info["weather"]
        weather_description = z[0]["description"]

        s = ""
        s += "Temperature: " + str(temperature) + " C \n"
        s += "Humidity: " + str(humidity) + " % \n"
        s += "Weather description: " + weather_description
        box.config(text=s)


# search button
submit = t.Button(window, text=" SEARCH ", command=weather, bg="green", fg="black", font=("Calibri", 20))
submit.pack()

# create display box to display text
box = t.Label(window, bg="black", fg="yellow", font=("Calibri", 20), height = 7, width = 500)
# location of display box set to center of the screen
box.pack(side=t.LEFT)

t.mainloop()
