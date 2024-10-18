# Id discord to first part of token
# Mozi Spy U

import time
import os
import fade 
from fade import *
import base64
try:
    from colorama import Fore, init
except:
    os.system("py -m pip install colorama")
    from colorama import Fore, init
init()

banner = """

 ▄█  ████████▄           ███      ▄██████▄           ███      ▄██████▄     ▄█   ▄█▄    ▄████████ ███▄▄▄▄   
███  ███   ▀███      ▀█████████▄ ███    ███      ▀█████████▄ ███    ███   ███ ▄███▀   ███    ███ ███▀▀▀██▄ 
███▌ ███    ███         ▀███▀▀██ ███    ███         ▀███▀▀██ ███    ███   ███▐██▀     ███    █▀  ███   ███ 
███▌ ███    ███          ███   ▀ ███    ███          ███   ▀ ███    ███  ▄█████▀     ▄███▄▄▄     ███   ███ 
███▌ ███    ███          ███     ███    ███          ███     ███    ███ ▀▀█████▄    ▀▀███▀▀▀     ███   ███ 
███  ███    ███          ███     ███    ███          ███     ███    ███   ███▐██▄     ███    █▄  ███   ███ 
███  ███   ▄███          ███     ███    ███          ███     ███    ███   ███ ▀███▄   ███    ███ ███   ███ 
█▀   ████████▀          ▄████▀    ▀██████▀          ▄████▀    ▀██████▀    ███   ▀█▀   ██████████  ▀█   █▀  
                                                                          ▀                                
"""
                                                                                 

banner = fade.purpleblue(banner)
print(banner)
userid = input(" USER ID : ")
encodedBytes = base64.b64encode(userid.encode("utf-8"))
encodedStr = str(encodedBytes, "utf-8")
print(f'\n [Première Partie] TOKEN : {encodedStr}')
wait_time = 10
time.sleep(wait_time) 
os.system("python main.py")