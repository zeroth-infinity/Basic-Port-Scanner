#!bin/python

import sys
import socket
from datetime import datetime

if len(sys.argv) == 2:
    target = socket.gethostbyname(sys.argv[1])
else:
    print("Invalid amount of arguements")
    print("Syntax is python3 scanner.py <ip>")

print("-"*50)
print("scanning target "+target)
print("time started "+str(datetime.now()))
print("-"*50)
try:
    for port in range(1,65535) :
        s= socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)
        result = s.connect_ex((target,port))
        if result == 0:
            print("port {} is open".format(port))
            s.close
except KeyboardInterrupt:
    print("\n Keyboard Interrupt")
    sys.exit()
except socket.gaierror:
    print("could not resolve host")
    sys.exit()
except socket.error:
    print("Can't connect to server")
    sys.exit()

