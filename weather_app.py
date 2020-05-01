from tkinter import *
import requests
import json

screen = Tk()
screen.title("New York ")
screen.geometry("400x40")
screen.configure(background = "green")

# URL : http://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=89129&distance=25&API_KEY=29CBD52F-BA9B-4188-B8FD-5B4540FD5EBF

try:
    api_request = requests.get("http://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=89129&distance=25&API_KEY=29CBD52F-BA9B-4188-B8FD-5B4540FD5EBF")
    api = json.loads(api_request.content)
    city = api[0] ["ReportingArea"]
    quality = api[0] ["AQI"]
    category = api[0] ["Category"] ["Name"]
except Exception as e:
    api = "eroor"

label = Label(screen, text = city + " Air Quality " + str(quality) + " " + category, font = ("Helvetica", 25), background = "green")
label.pack()



screen.mainloop()