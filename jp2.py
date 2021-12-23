# udppingserver_no_loss.py
from socket import *
import random
from time import sleep
# Create a UDP socket
serverSocket = socket(AF_INET, SOCK_DGRAM)
# Assign IP address and port number to socket
serverSocket.bind(('localhost', 12000))
while True:
    # Receive the client packet along with the address it is coming from
    message, address = serverSocket.recvfrom(1024)
    val = random.randint(10, 40)
    sleepVal = val/1000
    sleep(sleepVal)
    # # The server responds
    serverSocket.sendto(message, address)
