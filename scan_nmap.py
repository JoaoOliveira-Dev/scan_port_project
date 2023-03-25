from pyfiglet import *
import sys
import os
import socket
from datetime import datetime 

print("-*" * 50)
print(Figlet(font='slant').renderText('port Scanner'))
print("*-" * 50)

target = input(str("Host to be scanned: "))

print("-" * 50)
print("Scanning Target: " + target)
print("Time Started: " + str(datetime.now()))
print("-" * 50)

try:
    for port in range(1, 65535):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(0.5)

        #open port
        result = s.connect_ex((target, port))
        if result == 0:
            print("[*] Port {} is open".format(port))
        s.close()
except KeyboardInterrupt:
    print("Exiting Program: ")
    sys.exit()
except socket.error:
    print("Couldn't connect to server")
    sys.exit()