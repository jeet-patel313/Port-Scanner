#!/bin/python3

import sys
import socket
from datetime import datetime

#Defining the Traget
if len(sys.argv) == 2:
	target = socket.gethostbyname(sys.argv[1]) #Translates hostname to IPv4
else:
	print("Invalid amount of arguments.")
	print("Syntax: python3 scanner.py <ip>")

#Adding a banner
print("#" * 75)
print("             ___     ____              ____                      ")
print("            |_ _|   / __ \ _ __ ___   |  _ \  ___  _ __   ___    ")
print("             | |   / / _` | '_ ` _ \  | | | |/ _ \| '_ \ / _ \   ")
print("             | |  | | (_| | | | | | | | |_| | (_) | |_) |  __/   ")
print("            |___|  \ \__,_|_| |_| |_| |____/ \___/| .__/ \___|   ")
print("                    \____/                        |_|            ")
print("									")
print("                       # coded by Jeet Patel                     ")  
print("#" * 75)

print("Scanning Target "+target)
print("Scan started on: "+str(datetime.now()))

try:
	for port in range(1,65535):
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		socket.setdefaulttimeout(1)
		result = s.connect_ex((target,port)) #returns an error indicator
		if result == 0:
			print("Port {} is open".format(port))
		s.close()

except KeyboardInterrupt:
	print("\nKeyboardInterrupt Exiting Scan")
	sys.exit()

except socket.gaierror:
	print("Hostname could not be resolved")
	sys.exit()

except socket.error:
	print("Couldn't connect to server")
	sys.exit()



