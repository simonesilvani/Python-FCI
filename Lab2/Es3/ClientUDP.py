from socket import *

serverName= "localhost"
serverPort = 12000
serverAddress = (serverName, serverPort)

clientSocket = socket(AF_INET, SOCK_DGRAM)

timeLimit = 3
clientSocket.settimeout(timeLimit)

message = input("inserire un numero: ")
message = (message.encode("utf-8"))

clientSocket.sendto(message, serverAddress)

try:
    responseMessage , serverAddress = clientSocket.recvfrom(2040)
    codeResponseMessage = responseMessage.decode("utf-8")
    print("server answer ", codeResponseMessage)

except socket.timeout:
    print("TIMEOUT SCADUTO: SERVER NOT RESPONDED IN ", timeLimit)

finally:
    clientSocket.close()
