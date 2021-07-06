from tkinter import *
import requests
import json
import local_time_buttons


# STARTING API INFORMATION
def initial_api():
    global hour_
    global change
    # ACCESS API
    api_request = requests.get("http://worldtimeapi.org/api/timezone/Asia/Jakarta")

    # GET CONTENT FROM API
    api = json.loads(api_request.content)
    api_contet = str(api["datetime"])

    # SELECT CONTENT FROM API
    hour = api_contet[11 : 13]

    hour_ = hour

    # OPTION BUTTON
    change = 1

    # UPDATE API EVERY SECOND
    update_api()





# FUNCTION TO RECIEVE NEW INFO FROM API EVERY SECOND
def update_api():
    # GLOBAL VARIABLES
    global time_now
    global api_contet
    ########################################################################################## API

    # ACCESS API
    api_request = requests.get("http://worldtimeapi.org/api/timezone/Asia/Jakarta")

    # GET CONTENT FROM API
    api = json.loads(api_request.content)
    api_contet = str(api["datetime"])

    # SELECT CONTENT FROM API
    hour = api_contet[11 : 13]

    minute_and_seconds = api_contet[13 : 19]

    ########################################################################################## API
    
    # TIME NOW LABEL
    time_now = Label(local_time_buttons.root, text = hour_ + minute_and_seconds, font = ("times 20", 72))
    time_now.grid(row = 0, column = 0, pady = (89,0))
    

    # CHANGE TIME FORMAT
    if change == 0 :
        change_format

    
    # CALL FUNCTION EVERY 0.5 SECOND
    local_time_buttons.root.after(500, update_api)
    
    
    
# FUNCTION TO CHANGE TIME FORMAT
def change_format(event):
    global hour_
    global change
    
    # GET FORMAT
    time_format = local_time_buttons.option.get()

    # SEPERATE CURRENT TIME
    hour = api_contet[11 : 13]

    # CHANGE TIME FORMAT
    if time_format == "24 Hour" :
        hour_ = hour
    else: 
        
        if time_format == "12 Hour" :
            change = 0
            
            if int(hour) > 12 :
                
                if int(hour) == 13 :
                    hour_ = " 1 "
                else:
                    
                    if int(hour) == 14 :
                        hour_ = " 2 "
                    else:
                        
                        if int(hour) == 15 :
                            hour_ = " 3 "
                        else:
                            
                            if int(hour) == 16 :
                                hour_ = " 4 "
                            else:
                                
                                if int(hour) == 17 :
                                    hour_ = " 5 "
                                else:
                                    
                                    if int(hour) == 18 :
                                        hour_ = " 6 "
                                    else:
                                        
                                        if int(hour) == 19 :
                                            hour_ = " 7 "
                                        else:

                                            if int(hour) == 20 :
                                                hour_ = " 8 "
                                            else:
                                                
                                                if int(hour) == 21 :
                                                    hour_ = " 9 "
                                                else:
                                                    
                                                    if int(hour) == 22 :
                                                        hour_ = "10"
                                                    else:
                                                        
                                                        if int(hour) == 23 :
                                                            hour_ = "11"
                                                        else:

                                                            if int(hour) == 00 :
                                                                hour_ =  "12"
            else:
                hour_ = hour
        



                
    



