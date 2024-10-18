import os
import fade 
from fade import *

banner = """
 
   ▄▄▄▄███▄▄▄▄    ▄██████▄   ▄███████▄   ▄█          ▄████████    ▄███████▄ ▄██   ▄        ███    █▄  
 ▄██▀▀▀███▀▀▀██▄ ███    ███ ██▀     ▄██ ███         ███    ███   ███    ███ ███   ██▄      ███    ███ 
 ███   ███   ███ ███    ███       ▄███▀ ███▌        ███    █▀    ███    ███ ███▄▄▄███      ███    ███ 
 ███   ███   ███ ███    ███  ▀█▀▄███▀▄▄ ███▌        ███          ███    ███ ▀▀▀▀▀▀███      ███    ███ 
 ███   ███   ███ ███    ███   ▄███▀   ▀ ███▌      ▀███████████ ▀█████████▀  ▄██   ███      ███    ███ 
 ███   ███   ███ ███    ███ ▄███▀       ███                ███   ███        ███   ███      ███    ███ 
 ███   ███   ███ ███    ███ ███▄     ▄█ ███          ▄█    ███   ███        ███   ███      ███    ███ 
  ▀█   ███   █▀   ▀██████▀   ▀████████▀ █▀         ▄████████▀   ▄████▀       ▀█████▀       ████████▀  
                                                                                                                                                                                                                                                                                                                
     
"""

banner = fade.purpleblue(banner)

menu = """
                       †===========================================================================================†
                          [1] SOON               [4] Token checker                         [7] Ip stresser
                          [2] Ip info            [5] Id discord to first part of token     [8] Name tracker
                          [3] Dox Create         [6] Numer Tracker                         [9] Crédit
                          tiktok : mozispy u      crédit : Mozi                            discord : mozispyu
                       †===========================================================================================†
"""

menu = fade.purpleblue(menu)

def main ():
    os.system("cls")
    print(banner)
    print()
    print(menu)
    print()
    choice = input("choix : ")
    if choice == "1":
        os.system("python prgm/program1.py")
    if choice == "2":
        os.system("python prgm/program2.py")
    if choice == "3":
        os.system("python prgm/program3.py")
    if choice == "4":
        os.system("python prgm/program4.py")
    if choice == "5":
        os.system("python prgm/program5.py")
    if choice == "6":
        os.system("python prgm/program6.py")
    if choice == "7":
        os.system("python prgm/program7.py")
    if choice == "8":
        os.system("python prgm/program8.py")
    if choice == "9":
        os.system("python prgm/program9.py")              
    else:
        print("merci de rentrer un numéro valide")
        main()
main()