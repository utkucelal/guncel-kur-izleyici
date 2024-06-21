import requests
import sys
import time
from datetime import datetime
import webbrowser
import platform as p
import os

"""  
    _   _                _   _                 _     _            _      _ 
      (_) (_)              | | | |               (_)   | |          (_)    (_)
  __ _ _   _ _ __   ___ ___| | | | ___   _ _ __   _ ___| | ___ _   _ _  ___ _ 
 / _` | | | | '_ \ / __/ _ \ | | |/ / | | | '__| | |_  / |/ _ \ | | | |/ __| |
| (_| | |_| | | | | (_|  __/ | |   <| |_| | |    | |/ /| |  __/ |_| | | (__| |
 \__, |\__,_|_| |_|\___\___|_| |_|\_\\__,_|_|    |_/___|_|\___|\__, |_|\___|_|
  __/ |                                                         __/ |         
 |___/                                                         |___/          
                                                   
                    https://github.com/utkucelal                                                       
                                                """

# Import necessary libraries

# Add parent directory to sys.path
sys.path.append("..")

# Define a function to clear the console
clear = lambda: os.system('cls')

# Get the operating system
system = p.system()

# Set a flag variable
a = 1

# Set notification settings
notftime = 10  # Notification duration time

# Print the header

print("""
    _   _                _   _                 _     _            _      _ 
      (_) (_)              | | | |               (_)   | |          (_)    (_)
  __ _ _   _ _ __   ___ ___| | | | ___   _ _ __   _ ___| | ___ _   _ _  ___ _ 
 / _` | | | | '_ \ / __/ _ \ | | |/ / | | | '__| | |_  / |/ _ \ | | | |/ __| |
| (_| | |_| | | | | (_|  __/ | |   <| |_| | |    | |/ /| |  __/ |_| | | (__| |
 \__, |\__,_|_| |_|\___\___|_| |_|\_\\__,_|_|    |_/___|_|\___|\__, |_|\___|_|
  __/ |                                                         __/ |         
 |___/                                                         |___/           
                                                   
                                                   """)

# Ask for the mode of operation
mod = input("Choose the mode of operation:\n"
         "1. Track USD and EUR exchange rates with notifications\n"
         "2. View current exchange rates on the internet\n"
         "3. Track a specific currency value\n"
         "Enter the mode number: ")
clear()

# Mode 1: Track USD and EUR exchange rates with notifications
if int(mod) == 1:
    retimer = input("Enter the notification interval in seconds\n"
              "(1 hour = 3600, 30 minutes = 1800): ")
    if retimer == "":
     retimer = 1800
    
    clear()
    while a == 1:
     # Get the exchange rates for EUR and USD
     eur = requests.get('https://cdn.jsdelivr.net/npm/@fawazahmed0/currency-api@latest/v1/currencies/eur.json')
     usd = requests.get('https://cdn.jsdelivr.net/npm/@fawazahmed0/currency-api@latest/v1/currencies/usd.json')

     # Extract the exchange rates from the response
     eurjson = eur.json()
     usdjson = usd.json()
     try_usd = usdjson["usd"]["try"]
     try_eur = eurjson["eur"]["try"]

     # Get the current time
     now = datetime.now()
     dt_string = now.strftime("%d/%m/%Y %H:%M:%S")

     # Print the exchange rates and time
     print("EUR: ", try_eur, "USD: ", try_usd, "Time: ", dt_string, "These are approximate values.")

     # Wait for the specified interval
     time.sleep(int(retimer))

# Mode 2: View current exchange rates on the internet
if int(mod) == 2:
    # Open the Google search page for USD and EUR exchange rates
    webbrowser.open("https://www.google.com/search?q=dolar")
    webbrowser.open("https://www.google.com/search?q=euro")

# Mode 3: Track a specific currency value
if int(mod) == 3:
    # Get the currency database
    cur_DB = requests.get('https://cdn.jsdelivr.net/npm/@fawazahmed0/currency-api@latest/v1/currencies.min.json')

    # Ask for the currency codes
    cc1 = input("To convert a currency, you need to know the three-letter code of that currency.\n"
          "Press Enter to learn more about currency codes, or enter the code if you already know it.\n"
          "Enter the code of the currency you want to convert from: ")
    if cc1 == "":
     clear()
     # Open the currency database to learn more about currency codes
     webbrowser.open("https://cdn.jsdelivr.net/npm/@fawazahmed0/currency-api@latest/v1/currencies.min.json")
     cc1 = input("Enter the code of the currency you want to convert from: ")

    # Get the currency names from the database
    curjson = cur_DB.json()
    cc1_name = str(curjson[f'{cc1}'])

    cc2 = input(f"Now, enter the code of the currency you want to see the value of in terms of {cc1_name}:\n"
          "Enter the code of the currency you want to convert to: ")
    cc2_name = str(curjson[f'{cc2}'])

    retimer = input("Enter the notification interval in seconds\n"
              "(1 hour = 3600, 30 minutes = 1800): ")
    if retimer == "":
     retimer = 1800
    
    clear()
    while a == 1:
     # Get the exchange rate for the specified currency pair
     cc = requests.get(f'https://cdn.jsdelivr.net/npm/@fawazahmed0/currency-api@2024-03-06/v1/currencies/{cc2}.json')

     # Extract the exchange rate from the response
     ccjson = cc.json()
     cc1_cc2 = ccjson[cc2][cc1]

     # Get the current time
     now = datetime.now()
     dt_string = now.strftime("%d/%m/%Y %H:%M:%S")

     # Convert the exchange rate to an integer
     intc = int(cc1_cc2)
     if intc < 1:
         intc = float(cc1_cc2)

     # Print the exchange rate and time
     print(f'1 {cc2} ≈ {intc} {cc1} Time: ', dt_string, "These are approximate values.")

     # Wait for the specified interval
     time.sleep(int(retimer))
