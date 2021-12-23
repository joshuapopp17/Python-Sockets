from socket import *
from datetime import datetime
from time import sleep
import time
import random

num = 0

# socket Info
serverName = 'localhost'
serverPort = 12000
clientSocket = socket(AF_INET, SOCK_DGRAM)
clientSocket.connect((serverName, serverPort))

while True:
    val = random.randint(0, 100)
    if val < 5:
        break
    else:
        sleepVal = 5  # send after 5 seconds
        num = num + 1
        message = "heartbeat pulse " + str(num)
        clientSocket.sendto(message.encode(), (serverName, serverPort))
        clientSocket.settimeout(1.00000)
        try:
            print(message)
        except:
            print("Request timed out")
    sleep(sleepVal)

clientSocket.close()
