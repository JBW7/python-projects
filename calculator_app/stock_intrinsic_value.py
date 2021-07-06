from tkinter import *
import requests
import json
from PIL import ImageTk, Image
from tkinter import messagebox


root = Tk()
root.title("Intrinsic Value")
root.geometry("500x400")

# INITIAL VARIALES
mror_label = Entry(root)
mror_entry = Entry(root)
percent_symbol = Label(root)

mos_label = Label(root)
mos_entry = Entry(root)
percent_symbol_ = Label(root)

symbol_entry = Entry(root)

eps = 0
growth_rate = 0
pe_ratio = 0
stock_price = 0







def get_intrinsic_value():
    min_rate_of_return = mror_entry.get()
    if min_rate_of_return == "" :
        min_rate_of_return = 15
    
    else :
        
        #try :
            
        if float(min_rate_of_return) <= 0 :
            # ERROR MESSAGE BOX
            messagebox.showerror(" ERROR ", "MINUMUM RATE OF RETURN MUST BE > 0")
            mror_entry.delete(0, END)
        else :

            min_rate_of_return = float(min_rate_of_return) / 100
            
            margin_of_safety = mos_entry.get()
            if margin_of_safety == "" :
                margin_of_safety = 50
            
            else :

                if float(margin_of_safety) > 99 :
                    # ERROR MESSAGE BOX
                    messagebox.showerror(" ERROR ", "MARGIN OF SAFETY MUST BE < 100")
                    mos_entry.delete(0, END)
                else :

                    if float(margin_of_safety) <= 0 :
                        # ERROR MESSAGE BOX
                        messagebox.showerror(" ERROR ", "MARGIN OF SAFETY MUST BE > 0")
                        mos_entry.delete(0, END)

                    else :
                        # CLEAR ALL PREVIOUS WIDGETS
                        mror_label.grid_forget()
                        mror_entry.grid_forget()
                        percent_symbol.grid_forget()
                        
                        mos_label.grid_forget()
                        mos_entry.grid_forget()
                        percent_symbol_.grid_forget()

                        intrinsic_value_button.grid_forget()

            
                        margin_of_safety = float(margin_of_safety) / 100



                        ## GET INTRINSIC VALUE
                        # CURRENT VALUE
                        y_1 = eps
                        y_2 = y_1 + (y_1 * growth_rate)
                        y_3 = y_2 + (y_2 * growth_rate)
                        y_4 = y_3 + (y_3 * growth_rate)
                        y_5 = y_4 + (y_4 * growth_rate)
                        y_6 = y_5 + (y_5 * growth_rate)
                        y_7 = y_6 + (y_6 * growth_rate)
                        y_8 = y_7 + (y_7 * growth_rate)
                        y_9 = y_8 + (y_8 * growth_rate)
                        y_10 = y_9 + (y_9 * growth_rate)

                        # FUTURE VALUE
                        y10 = y_10 * pe_ratio
                        y9 = y10 / (1 + min_rate_of_return)
                        y8 = y9 / (1 + min_rate_of_return)
                        y7 = y8 / (1 + min_rate_of_return)
                        y6 = y7 / (1 + min_rate_of_return)
                        y5 = y6 / (1 + min_rate_of_return)
                        y4 = y5 / (1 + min_rate_of_return)
                        y3 = y4 / (1 + min_rate_of_return)
                        y2 = y3 / (1 + min_rate_of_return)
                        y1 = y2 / (1 + min_rate_of_return)

                        # INTRINSIC VALUE
                        intrinsic_value = y1
                        
                        # BUY PRICE
                        buy_price = intrinsic_value * margin_of_safety
                        
                        # FORMAT ANSWER
                        intrinsic_value = '{:,.2f}'.format(intrinsic_value)
                        buy_price = '{:,.2f}'.format(buy_price)


                        # SHOW ANSWERS
                        # SYMBOL LABEL
                        symbol_title = Label(root, text = symbol, font = ("Courier New", 40))
                        symbol_title.grid(row = 0, column = 0, pady = (20, 10), padx = (50, 0))

                        # CURRENT PRICE
                        current_price = Label(root, text = "Current Price = " + "$" + str(stock_price), font = ("Courier New", 30))
                        current_price.grid(row = 1, column = 0, pady = 10, padx = (50, 0))
                        
                        
                        # INTRINSIC VALUE
                        intrinsic_value_label = Label(root, text = "Intrinsic Value = " + "$" + str(intrinsic_value), font = ("Courier New", 30), anchor = CENTER)
                        intrinsic_value_label.grid(row = 2, column = 0, pady = 10, padx = (20, 0))

                        # BUY PRICE
                        buy_price_label = Label(root, text = "Buy Price = " + "$" + str(buy_price), font = ("Courier New", 30))
                        buy_price_label.grid(row = 3, column = 0, pady = 10, padx = (50, 0))
            
'''
except :
    # ERROR MESSAGE BOX
    messagebox.showerror(" ERROR ", "INPUT MUST BE A INTEGER")
    mror_entry.delete(0, END)
'''

                                
    



def collect_data():
    # GET SYMBOL
    global symbol
    symbol = symbol_entry.get().upper()

    
    # REMOVE PREVIOUS WIDGETS
    symbol_label.grid_forget()
    symbol_entry.grid_forget()
    symbol_button.grid_forget()

    
    ### NEW WIDGETS
    # MARGIN OF SAFETY LABEL
    global mos_label
    mos_label = Label(root, text = "Margin Of \nSafety", font = ("Courier New", 30))
    mos_label.grid(row = 0, column = 0, padx = (80, 0), pady = (60, 10))

    # MARGIN OF SAFETY ENTRY
    global mos_entry
    mos_entry = Entry(root, width = 5, font = ("Courier New", 30), justify = CENTER)
    mos_entry.grid(row = 0, column = 1, pady = (60, 10))
    mos_entry.insert(0, 50)

    # PERCENT SYMBOL
    global percent_symbol
    percent_symbol = Label(root, text = "%", font = ("Courier New", 30))
    percent_symbol.grid(row = 0, column = 2, pady = (60, 10))

    
    # MINIMUM RATE OF RETURN LABEL
    global mror_label
    mror_label = Label(root, text = "Minimum Rate \nOf Return", font = ("Courier New", 30))
    mror_label.grid(row = 1, column = 0, padx = (80, 0), pady = 10)

    # MINIMUM RATE OF RETURN ENTRY
    global mror_entry
    mror_entry = Entry(root, width = 5, font = ("Courier New", 30), justify = CENTER)
    mror_entry.grid(row = 1, column = 1, pady = 10)
    mror_entry.insert(0, 15)

    # PERCENT SYMBOL
    global percent_symbol_
    percent_symbol_ = Label(root, text = "%", font = ("Courier New", 30))
    percent_symbol_.grid(row = 1, column = 2, pady = 10)

    
    # GET INTRINSIC VALUE BUTTON
    global intrinsic_value_button
    intrinsic_value_button = Button(root, text = "Get Intrinsic Value", font = ("Courier New", 30), command = get_intrinsic_value)
    intrinsic_value_button.grid(row = 2, column = 0, columnspan = 5, padx = (40, 0), pady = 20)


    ####################################################################################################################################### EPS (TTM)
    # API
    eps_url = "https://apidojo-yahoo-finance-v1.p.rapidapi.com/market/get-quotes"

    querystring_e = {"region":"US", "lang":"en", "symbols":symbol}

    headers_e = {
        'x-rapidapi-host': "apidojo-yahoo-finance-v1.p.rapidapi.com",
        'x-rapidapi-key': "2be47bec07msh989077a6a9c07fap1a9a56jsnc1c636619d07"
        }

    eps_content = requests.request("GET", eps_url, headers = headers_e, params = querystring_e)

    eps_content = eps_content.text

    # GET EPS
    eps_substring = '"epsTrailingTwelveMonths"'
    eps_index_ = eps_content.find(eps_substring)
    eps_substring_ = eps_content[eps_index_ + 26: ]
    last_element_index_e = eps_substring_.find(",")
    last_element_index_e = last_element_index_e + eps_index_ + 26
    ######
    global eps
    eps = eps_content[eps_index_ + 26 : last_element_index_e]
    print (eps)
    
    try :
        eps = float(eps)
        ######
        ####################################################################################################################################### EPS (TTM)



        ####################################################################################################################################### GET GROWTH RATE
        # API 
        growth_rate_url = "https://apidojo-yahoo-finance-v1.p.rapidapi.com/stock/v2/get-analysis"

        querystring_g = {"symbol":symbol}

        headers_g = {
            'x-rapidapi-host': "apidojo-yahoo-finance-v1.p.rapidapi.com",
            'x-rapidapi-key': "2be47bec07msh989077a6a9c07fap1a9a56jsnc1c636619d07"
            }

        growth_rate_content = requests.request("GET", growth_rate_url, headers = headers_g, params = querystring_g)

        growth_rate_content = growth_rate_content.text

        # GET GROWTH RATE
        growth_rate_substring = """{"maxAge":1,"period":"+5y","endDate":null,"growth":"""
        growth_rate_index_ = growth_rate_content.find(growth_rate_substring) 
        growth_rate_substring_ = growth_rate_content[growth_rate_index_ + 52 : ]
        last_element_index_g = growth_rate_substring_.find("}")
        last_element_index_g = last_element_index_g + growth_rate_index_ + 52
        raw_fmt = growth_rate_content[growth_rate_index_ + 52 : last_element_index_g]
        fmt_index = raw_fmt.find("fmt")
        fmt_index = growth_rate_index_ + 52 + fmt_index
        fmt_text = growth_rate_content[fmt_index: last_element_index_g]
        colon_index = fmt_text.find(":")
        colon_index = fmt_index + colon_index + 2
        percent_index = fmt_text.find("%")
        percent_index = fmt_index + percent_index
        ######
        global growth_rate
        growth_rate = growth_rate_content[colon_index : percent_index]
        growth_rate = float(growth_rate)
        growth_rate = growth_rate / 100
        ######

        ####################################################################################################################################### GET GROWTH RATE



        ####################################################################################################################################### GET STOCK PRICE
        # API
        price_url = "https://apidojo-yahoo-finance-v1.p.rapidapi.com/market/get-quotes"

        querystring_s = {"region":"US","lang":"en","symbols": symbol}

        headers_s = {
            'x-rapidapi-host': "apidojo-yahoo-finance-v1.p.rapidapi.com",
            'x-rapidapi-key': "2be47bec07msh989077a6a9c07fap1a9a56jsnc1c636619d07"
            }

        price_content = requests.request("GET", price_url, headers = headers_s, params = querystring_s)
        price_content = price_content.text

        # GET STOCK PRICE
        price_substring = '"regularMarketPrice":'
        price_index = price_content.find(price_substring)
        price_substring_ = price_content[price_index + 21 :]
        last_element_s = price_substring_.find(",")
        last_element_index_s = last_element_s + 21 + price_index
        ######
        global stock_price
        stock_price = price_content[price_index + 21 : last_element_index_s]      
        stock_price = float(stock_price)
        stock_price = '{:,.2f}'.format(stock_price)
        ######
        
        ####################################################################################################################################### GET STOCK PRICE
        
        
        
        ####################################################################################################################################### GET PE RATIO
        # API 
        pe_ratio_url = "https://apidojo-yahoo-finance-v1.p.rapidapi.com/stock/v2/get-analysis"

        querystring_p = {"symbol":symbol}

        headers_p = {
            'x-rapidapi-host': "apidojo-yahoo-finance-v1.p.rapidapi.com",
            'x-rapidapi-key': "2be47bec07msh989077a6a9c07fap1a9a56jsnc1c636619d07"
            }

        pe_content = requests.request("GET", pe_ratio_url, headers = headers_p, params = querystring_p)

        pe_content = pe_content.text

        # GET PE RATIO
        pe_ratio_substring = '"trailingPE"'
        pe_ratio_index_ = pe_content.find(pe_ratio_substring)
        pe_ratio_substring_  = pe_content[pe_ratio_index_ + 20 :]
        last_element_index_p = pe_ratio_substring_.find("}")
        last_element_index_p = last_element_index_p + pe_ratio_index_ + 20
        raw_fmt_subtsring = pe_content[pe_ratio_index_ + 20 : last_element_index_p]
        fmt_index_p = raw_fmt_subtsring.find("fmt")
        fmt_index_p = fmt_index_p + pe_ratio_index_ + 20
        fmt_substring_p = pe_content[fmt_index_p : last_element_index_p]
        ######
        global pe_ratio
        pe_ratio  = fmt_substring_p[6 : ]
        pe_ratio = pe_ratio.replace('"', "")
        ######

        try :
            
            pe_ratio = float(pe_ratio)
            
        except :
            # ERROR MESSAGE BOX
            messagebox.showerror(" ERROR ", "NOT ENOUGH DATA PROVIDED \nBY YAHOO FINANCE")
            
            # CLEAR ALL WIDGETS
            mos_label.grid_forget()
            mos_entry.grid_forget()
            percent_symbol.grid_forget()
            mror_label.grid_forget()
            mror_entry.grid_forget()
            percent_symbol_.grid_forget()
            intrinsic_value_button.grid_forget()

            # SHOW PREVIOUS WIDGETS
            symbol_label.grid(row = 0, column = 0, pady = 175, padx = (25, 0))
            symbol_entry.grid(row = 0, column = 1, pady = 175)
            symbol_button.grid(row = 0, column = 2, padx = (2, 0))


            
        
        

        ####################################################################################################################################### GET PE RATIO
    except :
        # ERROR MESSAGE BOX
        messagebox.showerror(" ERROR ", "INVALID SYMBOL")

        # CLEAR ENTRY
        symbol_entry.delete(0, END)

        # CLEAR ALL WIDGETS
        mos_label.grid_forget()
        mos_entry.grid_forget()
        percent_symbol.grid_forget()
        mror_label.grid_forget()
        mror_entry.grid_forget()
        percent_symbol_.grid_forget()
        intrinsic_value_button.grid_forget()

        # SHOW PREVIOUS WIDGETS
        symbol_label.grid(row = 0, column = 0, pady = 175, padx = (25, 0))
        symbol_entry.grid(row = 0, column = 1, pady = 175)
        symbol_button.grid(row = 0, column = 2, padx = (2, 0))







    
    
    
    

   



# SYMBOL : LABEL
symbol_label = Label(root, text = "Symbol:", font = ("Courier New", 40))
symbol_label.grid(row = 0, column = 0, pady = 175, padx = (25, 0))

# SYMBOL ENTRY
symbol_entry = Entry(root, width = 7, font = ("Courier New", 40), justify = CENTER, borderwidth = 3)
symbol_entry.grid(row = 0, column = 1, pady = 175)

### SYMBOL BUTTON
# IMAGE
search_icon = ImageTk.PhotoImage(Image.open("/Users/jonathan/Desktop/python/python_pics/search_icon.png"))

# BUTTON
symbol_button = Button(root, image = search_icon, borderwidth = 0, command = collect_data)
symbol_button.grid(row = 0, column = 2, padx = (2, 0))





# API SOURCE
# https://rapidapi.com/apidojo/api/yahoo-finance1?endpoint=apiendpoint_ef6248fb-33e7-42ea-a8a6-58a7ef7f2177

# note
# if unable to search symbol go to api link, unsubscribe then subcribe



root.mainloop()















