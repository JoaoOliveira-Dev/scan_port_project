from pyfiglet import *

# Importing the nmap module
import nmap

# Creating the nmap object
nm = nmap.PortScanner()

# Printing the banner
print(Figlet(font='slant').renderText('Nmap Scanner'))

# Asking the user for the target
target = input("Enter the target IP address: ")

# Asking the user for the port range
port_range = input("Enter the port range (e.g. 1-1000): ")

# Printing the banner
print(Figlet(font='slant').renderText('Scanning...'))

# Scanning the target
nm.scan(target, port_range)

# Printing the results
print(nm.csv())

# Printing the banner
print(Figlet(font='slant').renderText('Done!'))
