from socket import *
from datetime import datetime
from time import sleep
import time

# variables
minRTT = 0
maxRTT = 0
avgRTT = 0
totalRTT = 0
lostPackets = 0
packetLossPerc = 0
seqNum = 1
runs = input("Enter how many pings: ")
runAmount = int(runs)
print("")
# socket Info
serverName = 'localhost'
serverPort = 12000
clientSocket = socket(AF_INET, SOCK_DGRAM)
clientSocket.connect((serverName, serverPort))

for x in range(runAmount):
    now = datetime.now()
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
    message = "Seq " + str(seqNum) + " " + dt_string
    clientSocket.sendto(message.encode(), (serverName, serverPort))
    start = time.time() * 1000
    clientSocket.settimeout(1.00000)
    try:
        data, sender_addr = clientSocket.recvfrom(1024)
        print("Ping " + str(x+1) + ": " + "host", end="")
        print(" " + str(sender_addr) + " replied: ", end="")
        print(data.decode() + ", RTT = ", end="")
        end = time.time() * 1000
        current = end - start
        RTTcurrent = format(current, '.2f')
        print(str(RTTcurrent) + " ms")
        totalRTT = totalRTT + current
        if(x == 0):
            minRTT = current
            maxRTT = current
        if (current < minRTT):
            minRTT = current
        if(current > maxRTT):
            maxRTT = current
    except:
        print("Ping " + str(x+1) + ": " + "Request timed out")
        lostPackets = lostPackets + 1
    sleep(0)
    seqNum = seqNum + 1

print("")
print("+-+-+-+-+-+-+-+-+-+-+-+-+-+-+")
minRTT = format(minRTT, '.2f')
print("MinRTT: " + str(minRTT) + " ms")
maxRTT = format(maxRTT, '.2f')
print("MaxRTT: " + str(maxRTT) + " ms")
avgRTT = totalRTT / runAmount
avgRTT = format(avgRTT, '.2f')
print("AverageRTT: " + str(avgRTT) + " ms")
packetLossPerc = (lostPackets / runAmount) * 100
packetLossPerc = format(packetLossPerc, '.2f')
print("PacketLoss: " + str(packetLossPerc) + "%")
print("+-+-+-+-+-+-+-+-+-+-+-+-+-+-+")
