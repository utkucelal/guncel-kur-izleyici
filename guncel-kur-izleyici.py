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
from playsound import playsound
import sys
import time
from datetime import datetime
from gtts import gTTS
import webbrowser
import platform as p
import os
sys.path.append("..")
clear = lambda: os.system('cls')
system = p.system()
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

mod=input("belirleyece??iniz saniyede bir bildirim g??nderen \n dolar ve euro kuru izleyicisi i??in 1 \n g??ncel kurlar?? internetde g??rmek i??in 2 \n istedi??iniz bir kur de??erini (crypto val??klarda dahil) takip etmek i??in 3 \n yaz??n: ")
clear()

if int(mod) == 1 :
    retimer=input("ka?? saniyede bir bildirim gelsin saniye cinsnden yaz??n \n (1 saat= 3600 30 dakika= 1800): ")
    
    clear()
    while a == 1:

    
     eur = requests.get('https://cdn.jsdelivr.net/gh/fawazahmed0/currency-api@1/latest/currencies/eur/try.json')
     usd = requests.get('https://cdn.jsdelivr.net/gh/fawazahmed0/currency-api@1/latest/currencies/usd/try.json')


     for currency in eur and usd:
         eurjson = eur.json()
         usdjson = usd.json()
         try_usd= str(usdjson['try'])
         try_eur= str(eurjson['try'])
         basic_try_usd = try_usd.split(".")
         basic_try_eur = try_eur.split(".")


         now = datetime.now()
         dt_string = now.strftime("%d/%m/%Y %H:%M:%S")

         print("euro: ",try_eur,"dolar: ",try_usd,"zaman: ",dt_string)

         tts = gTTS(text=f'??uan euro {basic_try_eur[0]} dolar {basic_try_usd[0]}', lang='tr')
         tts.save("cur.mp3")
         playsound("cur.mp3")
         os.remove("cur.mp3")


         time.sleep(int(retimer))
        

if int(mod) == 2:
    webbrowser.open("https://www.google.com/search?q=dolar")
    webbrowser.open("https://www.google.com/search?q=euro")

if int(mod) == 3:
    cur_DB = requests.get('https://cdn.jsdelivr.net/gh/fawazahmed0/currency-api@1/latest/currencies.json')
    cc1= input("??evirmek istedi??iniz kur de??erleri i??in o para biriminin ???? haneli kodunu bilmeniz gerekir ????renmek i??in enter bas??n e??er biliyorsan??z \n para biriminin kodunu girin: ")
    if cc1 == "" :
        clear()
        webbrowser.open("https://cdn.jsdelivr.net/gh/fawazahmed0/currency-api@1/latest/currencies.json")
        cc1= input("para biriminin kodunu girin: ")
    curjson = cur_DB.json()
    cc1_name= str(curjson[f'{cc1}']) 


    cc2= input(f'??imdi ise hangi para biriminin {cc1_name} kar???? de??erini g??rmek istiyorsunuz? \n para biriminin kodunu girin: ')
    cc2_name= str(curjson[f'{cc2}'])

    retimer=input("ka?? saniyede bir bildirim gelsin saniye cinsnden yaz??n \n (1 saat= 3600 30 dakika= 1800): ")
    
    clear()
    while a == 1:

    
     cc= requests.get(f'https://cdn.jsdelivr.net/gh/fawazahmed0/currency-api@1/latest/currencies/{cc2}/{cc1}.json')


     for currency in cc:
         ccjson = cc.json()
         cc1_cc2= str(ccjson[f'{cc1}'])
         basic_cc1_cc2 = cc1_cc2.split(".")


         now = datetime.now()
         dt_string = now.strftime("%d/%m/%Y %H:%M:%S")

         print(f'1 {cc2} = {cc1_cc2}{cc1} zaman: ',dt_string)

         tts = gTTS(text=f'??uan 1 {cc2_name} {basic_cc1_cc2[0]}{cc1_name}', lang='tr')
         tts.save("ccur.mp3")
         playsound("ccur.mp3")
         os.remove("ccur.mp3")


         time.sleep(int(retimer))
