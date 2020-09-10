## IP-PYTHON v1.0 by blomjoe

## import socket module
import socket

## import requests module
import requests

## getting hostname by socket.gethostname() method
hostname = socket.gethostname()

## getting  IP address using socket.gethostbyname() method
ip_address = socket.gethostbyname(hostname)

## printing the hostname and ip_address
print(f"Hostname: {hostname}")
print(f"IP Address: {ip_address}")

## from module requests we import get
from requests import get

## with help of ipify, we get public ip
ip = get('https://api.ipify.org').text
print('Public IP address: {}'.format(ip))
 
## import modules re & uuid  
import re, uuid 
  
## joins elements of getnode() after each 2 digits. 
## using regex expression
## MAC address output in better formatting 
print ("The MAC address: ", end="") 
print (':'.join(re.findall('..', '%012x' % uuid.getnode())))

## print line break (obvious)
print("-----------------------------------")

## print text to exit program
print("Press enter to exit the program.")

## import keyboard module
import keyboard

## from keyboard module we use wait function to use enter button to exit program on press
keyboard.wait("enter")

## END OF PROGRAM