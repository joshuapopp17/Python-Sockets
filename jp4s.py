# udppingserver_no_loss.py
from socket import *
from time import sleep
import time
# Create a UDP socket
serverSocket = socket(AF_INET, SOCK_DGRAM)
# Assign IP address and port number to socket
serverSocket.bind(('localhost', 12000))

num = 0

while True:
    start = time.time()
    # Receive the client packet along with the address it is coming from
    serverSocket.settimeout(10.00000)
    try:
        message, address = serverSocket.recvfrom(1024)
        end = time.time()
        timeVal = end - start
        timeVal = int(timeVal)
        print("Server received " + message.decode() +
              " Pulse interval was " + str(timeVal) + " seconds")
    except:
        print("No Pulse after 10 seconds. Server Quits")
        break
print("Server Stops.")
serverSocket.close()
