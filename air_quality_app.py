from tkinter import *
import requests
import json

screen = Tk()
screen.title("Air Quality (US ONLY)")
screen.geometry("410x100")

# AIRNOW API
# URL : http://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=89129&distance=25&API_KEY=29CBD52F-BA9B-4188-B8FD-5B4540FD5EBF

# DEF ZIPCODE LOOKUP FUNCTION
def zipcode_lookup():
    try:
        # CONNECT TO API
        api_request = requests.get("http://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=" + zip_entry.get() + "&distance=25&API_KEY=29CBD52F-BA9B-4188-B8FD-5B4540FD5EBF")
        api = json.loads(api_request.content)
        # GET INFO
        city = api[0] ["ReportingArea"]
        quality = api[0] ["AQI"]
        category = api[0] ["Category"] ["Name"]

        # SET COLOR
        if category == "Good":
            color = "#0C0"

        elif category == "Moderate":
            color = "FFFF00"

        elif category == "Unhealth for Sensitive Group ":
            color = "ff9900"

        elif category == "Unhealthy":
            color = "FF0000"

        elif category == "Very Unhealthy":
            color = "990066"

        elif category == "Hazardous":
            color = "#660000"

        # CHANGE BACKGROUND COLOR
        screen.configure(background = color)

        label = Label(screen, text = city + " Air Quality " + str(quality) + " " + category, font = ("Helvetica", 25), background = color)
        label.grid(row = 1, column = 0, columnspan = 2)

    except:
        label = Label(screen, text = "INVALID ZIPCODE", font = ("Helvetica", 25), background = "#FF0000")
        label.grid(row = 1, column = 0, columnspan = 2)
        screen.configure(background = "#FF0000")

zip_entry = Entry(screen)
zip_entry.grid(row = 0, column = 0, stick = W + E + N+ S)

zip_button = Button(screen, text = "Lookup Zipcode", command = zipcode_lookup)
zip_button.grid(row = 0, column = 1, stick = W + E + N+ S)



 

screen.mainloop()