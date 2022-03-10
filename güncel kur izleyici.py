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



import requests
import time
from datetime import datetime
from win10toast import ToastNotifier
import requests
import webbrowser
import platform as p
import os
clear = lambda: os.system('cls')
system = p.system()
toaster = ToastNotifier()
a = 1
#notfication settings
notftime = 10 #notfication settings duration time

print("""\
       _   _                _   _                 _     _            _      _ 
      (_) (_)              | | | |               (_)   | |          (_)    (_)
  __ _ _   _ _ __   ___ ___| | | | ___   _ _ __   _ ___| | ___ _   _ _  ___ _ 
 / _` | | | | '_ \ / __/ _ \ | | |/ / | | | '__| | |_  / |/ _ \ | | | |/ __| |
| (_| | |_| | | | | (_|  __/ | |   <| |_| | |    | |/ /| |  __/ |_| | | (__| |
 \__, |\__,_|_| |_|\___\___|_| |_|\_\\__,_|_|    |_/___|_|\___|\__, |_|\___|_|
  __/ |                                                         __/ |         
 |___/                                                         |___/           
                                                                                       
                                                                                        """)

mod=input("belirleyeceğiniz saniyede bir bildirim gönderen \n dolar ve euro kuru izleyicisi için 1 \n güncel kurları internetde görmek için 2 \n yazın: ")

if int(mod) == 1 :
    retimer=input("kaç saniyede bir bildirim gelsin saniye cinsnden yazın \n (1 saat= 3600 30 dakika= 1800): ")
    
    clear()
    while a == 1:

    
     eur = requests.get('https://cdn.jsdelivr.net/gh/fawazahmed0/currency-api@1/latest/currencies/eur/try.json')
     usd = requests.get('https://cdn.jsdelivr.net/gh/fawazahmed0/currency-api@1/latest/currencies/usd/try.json')


     for currency in eur and usd:
         eurjson = eur.json()
         usdjson = usd.json()
         try_usd= str(usdjson['try'])
         try_eur= str(eurjson['try'])

         now = datetime.now()
         dt_string = now.strftime("%d/%m/%Y %H:%M:%S")

         print("euro: ",try_eur,"dolar: ",try_usd,"zaman: ",dt_string)
         if str(system) == "Windows" :
             toaster.show_toast("bakalım battık mı",f"anlık olarak dolar: {try_usd} euro: {try_eur}",duration=notftime)

else:
    webbrowser.open("https://www.google.com/search?q=dolar")
    webbrowser.open("https://www.google.com/search?q=euro")