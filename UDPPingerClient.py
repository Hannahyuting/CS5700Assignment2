from socket import *
from datetime import datetime
import sys

def main():
    clientSocket = socket(AF_INET, SOCK_DGRAM)
    serverName = 'localhost'
    serverPort = 12000
    clientSocket.settimeout(1)

    for i in range(1, 11):
        t1 = datetime.now()
        message = 'Ping' + str(i) + " " + str(t1)
        clientSocket.sendto(message.encode(), (serverName, serverPort))
        try:
            serverMessage, address = clientSocket.recvfrom(1024)
            print(serverMessage)
            t2 = datetime.now()
            rtt = t2 - t1
            print('RTT: ' + str(rtt) + ' seconds')
        except timeout:
            print('Request timed out')

    clientSocket.close()

main()
