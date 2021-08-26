import socket as soc
import threading as thread
import os
import pyfiglet
os.system("clear")

os.system("tput setaf 6")
os.system("color 7")
title = pyfiglet.figlet_format("\t\t! WELCOME TO THE UDP CHAT APP FOR LINUX ! \n")
print(title)
print("\n ####################################################################### \n")
print("\n\t\t LET'S START COMMUNICATING BY SENDING OUR FIRST MESSAGE \n")
print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$ \n")
your_ip = input("ENTER THE YOUR IP ADDRESS HERE : ")
your_port = int(input("ENTER THE YOUR PORT NUMBER HERE : "))
frd_ip = input("ENTER THE FRIEND'S IP ADDRESS HERE : ")
frd_port = int(input("ENTER THE FRIEND'S PORT NUMBER HERE : "))

# TO CREATE A SOCKET AND BIND IP AND PORT NUMBER :

skt2 = soc.socket(soc.AF_INET, soc.SOCK_DGRAM)
skt2.bind((your_ip, your_port))
# WE CAN USE THIS FUNCTION TO RECIEVING AND PRINTING THE MESSAGE :
def recieve_msg():
    while True:
        os.system("tput setaf 2")
        msgRcv = skt2.recvfrom(1024)
        if msgRcv[0].decode() == "quit" or msgRcv[0].decode() == "bye" or msgRcv[0].decode() == "exit":
            print("NOW YOUR FRIEND HAS GONE OFFLINE.....")
            os._exit(1)
        print("\n\t\t\t YOUR FRIEND'S MESSAGE --->" + msgRcv[0].decode())# WE CAN USE THIS FUNCTION TO SENDING THE MESSAGE :
def send_msg():
    while True:
        data = input().encode()
        msgSent = skt2.sendto(data, (frd_ip, frd_port))
        if data.decode() == "quit" or data.decode() == "bye" or data.decode() == "exit":
            os._exit(1)
# WE CAN USE THIS THREAD FOR SENDING THE MESSAGE FUNCTION :
t3 = thread.Thread(target=send_msg)
# WE CAN USE THIS THREAD FOR RECIVING THE MESSAGE FUNCTION :
t4 = thread.Thread(target=recieve_msg)
# WE CAN USE THIS FUNCTION TO STARTING OUR THREADS :
t3.start()
t4.start()
