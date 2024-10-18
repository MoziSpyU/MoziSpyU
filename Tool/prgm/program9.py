# Crédit
# Mozi Spy U

import os
import fade
from fade import *
import time
import requests
import webbrowser

credit = """
                       †===============================================================†
                                   [prénom] MoziSpyU             [ville] ?
                                   [nom] ?                       [discord] mozispyu
                                   [age] 16                      [tiktok] mozispyu                   
                       †==============================================================† """

credit = fade.greenblue(credit)
print(credit)
print()
tiktok = "https://www.tiktok.com/@mozispyu?lang=fr"
webbrowser.open(tiktok, new=2)
discord = "https://discord.gg/XxJTAYKP2a"
webbrowser.open(discord, new=2) 
wait_time = 10
time.sleep(wait_time)
os.system("python main.py")