import subprocess
import os
import platform
import time

from Demos.win32ts_logoff_disconnected import username
from tqdm import tqdm
import socket
from pystyle import *
# Create Admin Server - Code



def SET_PWD_ADMIN ():
    # Notes ::|
    pwd = ''
    User = "admin"
    PWD = "admin"

    username = input("\nEnter Admin Of Username to Run Server : ").lower()
    Write.Print(f"{username}",Colors.green_to_cyan,interval=.02)
    pwd = input("\nEnter Admin Of PWD to Run Server : ").lower()
    Write.Print(f"{pwd}",Colors.green_to_cyan,interval=.02)

    if username == User and pwd == PWD:
        print ("\n\n\33[32;1mCorrect of Username and Paswword Of Admin....\n")
    else:
        print("\33[31;1mError of This....\33[39;0m")
        exit()
    # if pwd == PWD:
    #     print("\33[32;1mCorrect of PWD..\33[39;0M\n")
    # else:
    #     print("\33[31;1mError of This....\33[39;0m")

SET_PWD_ADMIN()
# print ("\33[35;1mupdate server info....\n\33[39;0m")
def Check_Server ():

        for RUN in tqdm (range(100),desc='\33[36;1mUpdate Server All Data , INFO ===> ....\33[39;0m') :
            time.sleep(.050)



Check_Server()


def RUN_SERVER ():

    for RUN in tqdm (range(100),desc="\33[33;1mRun Server , Commands is Runing ===> ....\33[39;0m"):
        time.sleep(.055)



RUN_SERVER()




# fun to Notes...



def NOTES () :
    # Note ::|
    Write.Print("\n[+] GitHub  ::: https://www.github.com/DARKGITHUBPRO/\n", Colors.yellow_to_red, interval=.03)
    Write.Print("\n[+] Server is Runing  Now..!\n", Colors.green_to_cyan, interval=.03)
    Write.Print("\n[-] SERVER Under Developer\n",Colors.light_gray,interval=.02)
    time.sleep(5)
    exit()





# SET A CREATE ALL CODES - COMMANDS FOR A SERVER , USE socket ⤵️⤵️⤵️

def RUN_SERVER (RUN_SERVER=NOTES()) :

    NOTES()

    # AF_INET ..... IPv4    # UDP
    value_sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM) # يعمل السيرفر علي برتوكول UDP , يعمل السيرفر علي الاصدار الرابع منIP

                    # Set IP ,  PORT
    value_sock.bind(("127.0.0.1",5555)) # ربط عبر IP مع PORT

    #حجم استقبال الداتا# && ip of client + Port of Client , استقبال الداتا
    Resevddata , address = value_sock.recvfrom(1024)

            # decode for data فك الترميز
    decode_data = Resevddata.decode("UTF-8")

    # send message for client
    Data_for_send_by_admin_to_client = "Hellow Client..😊"

    # Encode my send data
    Send_data = Data_for_send_by_admin_to_client.encode("UTF-8")

    # send data for ip , port (FOR - address)
    value_sock.sendto(Send_data,address)


RUN_SERVER()
