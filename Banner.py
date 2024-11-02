from pyperclip import *
import pyfiglet as ban
from pystyle import *
import platform
import os
import socket
import time

from sympy.plotting.intervalmath import interval
from tqdm import *
from colorama import Fore
import random
# Banner of logo project

print(Fore.LIGHTGREEN_EX,"""
██████╗  █████╗ ███╗   ██╗███╗   ██╗███████╗██████╗ 
██╔══██╗██╔══██╗████╗  ██║████╗  ██║██╔════╝██╔══██╗
██████╔╝███████║██╔██╗ ██║██╔██╗ ██║█████╗  ██████╔╝
██╔══██╗██╔══██║██║╚██╗██║██║╚██╗██║██╔══╝  ██╔══██╗
██████╔╝██║  ██║██║ ╚████║██║ ╚████║███████╗██║  ██║
╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═══╝╚═╝  ╚═══╝╚══════╝╚═╝  ╚═╝
""")
print("\33[39;0m[🚨📢🔔⚠️]\33[91;1m Enter English Only or any language in not arabic\33[39;0m [🚨📢🔔⚠️]\n")
                                                                    #============== END BANNER ============

                                                                #========== SET INPUT to set name banner ============


set_banner_name = input('\33[36;1m[\33[39;0m\33[91m-\33[96;1m]\33[39;0m\33[94;1m Enter Your Name to Create Banner : \33[39;0m')
print("﹌" * 20)
Write.Print('[🟢] OK Continue to Follow Steps...\n',Colors.green,interval=0.1)
print("﹌" * 20)
font_style_list =(""" 
\33[36;1m[\33[39;0m\33[91;1m1\33[96;1m]\33[39;0m >>> SLANT
\33[36;1m[\33[39;0m\33[91;1m2\33[96;1m]\33[39;0m >>> 3-D
\33[36;1m[\33[39;0m\33[91;1m3\33[96;1m]\33[39;0m >>> 5LINEOBLIQUE
\33[36;1m[\33[39;0m\33[91;1m4\33[96;1m]\33[39;0m >>> ALPHABET
\33[36;1m[\33[39;0m\33[91;1m5\33[96;1m]\33[39;0m >>> DOH
\33[36;1m[\33[39;0m\33[91;1m6\33[96;1m]\33[39;0m >>> ISOMETRIC1
""")
print(font_style_list)

# Write.Print('[✅] OK Continue to Follow Steps...',Colors.green,interval=0.1)
#=================================================================== CLOSE CHOOSE OF FONT style ====================================================================

                                                                #========= START INPUT FOR USE OF choose style banner ==============
print("﹌" * 20)
set_font_style = input('\33[36;1m[\33[39;0m\33[91;1m➡️\33[96;1m]\33[39;0m\33[93;2m Enter Number Of Font Style to Banner : \33[39;0m')
print("﹌" * 20)

#==================================

Write.Print('[🟢] OK Continue to Follow Steps...\n',Colors.green,interval=0.1)
print("﹌" * 20)

                                                                #=============== LIST TO CHOOSE COLOR ===================
font_color_list =(""" 
\33[36;1m[\33[39;0m\33[91;1m1\33[96;1m]\33[39;0m >>> LIGHTGREEN_EX
\33[36;1m[\33[39;0m\33[91;1m2\33[96;1m]\33[39;0m >>> LIGHTMAGENTA_EX
\33[36;1m[\33[39;0m\33[91;1m3\33[96;1m]\33[39;0m >>> LIGHTYELLOW_EX
\33[36;1m[\33[39;0m\33[91;1m4\33[96;1m]\33[39;0m >>> BLUE
\33[36;1m[\33[39;0m\33[91;1m5\33[96;1m]\33[39;0m >>> RED
\33[36;1m[\33[39;0m\33[91;1m6\33[96;1m]\33[39;0m >>> CYAN
\33[36;1m[\33[39;0m\33[91;1m7\33[96;1m]\33[39;0m >>> GREEN
\33[36;1m[\33[39;0m\33[91;1m8\33[96;1m]\33[39;0m >>> YELLOW
\33[36;1m[\33[39;0m\33[91;1m9\33[96;1m]\33[39;0m >>> MAGENTA
\33[36;1m[\33[39;0m\33[91;1m10\33[96;1m]\33[39;0m >>> WHITE
\33[36;1m[\33[39;0m\33[91;1m11\33[96;1m]\33[39;0m >>> LIGHTRED_EX
""")

print(font_color_list)
print("﹌" * 20)

                                                        # ===============END LIST TO CHOOSE COLOR===================


                                                            #=====SET INPUT to Choose COLOR=======

set_font_color = input('\33[36;1m[\33[39;0m\33[91;1m➡️\33[96;1m]\33[39;0m\33[95;1m Enet Color Number to Banner : \33[39;0m')
# Write.Print("Note : If Choose any Number",Colors.yellow_to_red,interval=0)
print("﹌" * 20)
Write.Print('[✅] OK Continue to Follow Last Step ...\n', Colors.green, interval=0.1)
print("﹌" * 20)


# START >>> [ IF , ELIF , ELSE ] >>> TO CHOOSE OF USER
if set_font_style == '1':
    banner = ban.figlet_format(set_banner_name,font='slant')


elif set_font_style == '2':
    banner = ban.figlet_format(set_banner_name, font='3-d')

elif set_font_style == '3':
    banner = ban.figlet_format(set_banner_name, font='5lineoblique')

elif set_font_style == '4':
    banner = ban.figlet_format(set_banner_name, font='alphabet')

elif set_font_style == '5':
    banner = ban.figlet_format(set_banner_name, font='doh')

elif set_font_style == '6':
    banner = ban.figlet_format(set_banner_name, font='isometric1')

else:
    print('\33[91;1mError ID number not entered ')


                                                           #====== END INPUTS to Choose font , END IF - ELIF =======

                                                            # ====== START END IF - ELIF TO CHOOSE COLOR =======



if set_font_color == '1':
    print(Fore.LIGHTGREEN_EX,banner)

elif set_font_color == '2':
    print(Fore.LIGHTMAGENTA_EX, banner)


elif set_font_color == '3':
    print(Fore.LIGHTYELLOW_EX, banner)

elif set_font_color == '4':
    print(Fore.BLUE, banner)


elif set_font_color == '5':
    print(Fore.RED, banner)

elif set_font_color == '6':
    print(Fore.CYAN, banner)


elif set_font_color == '7':
    print(Fore.GREEN, banner)

elif set_font_color == '8':
    print(Fore.YELLOW, banner)

elif set_font_color == '9':
    print(Fore.MAGENTA, banner)


elif set_font_color == '10':
    print(Fore.WHITE, banner)


elif set_font_color == '11':
    print(Fore.LIGHTRED_EX, banner)

else:
    print('\n\33[91;1m Error ID number not entered \n')

print("\33[90;3m﹌\33[39;0m" * 20)




