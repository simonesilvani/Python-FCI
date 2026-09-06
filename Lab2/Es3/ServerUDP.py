from socket import *
import math

def numero_primo (number):
    if number < 2:
        return "non è primo"

    for i in range(2, int(math.sqrt(number)) + 1):
        if number % i == 0:
            return "non è primo"

    return "è primo"

serverPort = 12000
serverAddress = ('', serverPort)

serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind(serverAddress)

print("SERVED STARTED ON GATE : ", serverPort)

while True:
    message, clientAddress = serverSocket.recvfrom(2040)
    messageDecode = message.decode("utf-8")
    print("il client: ",clientAddress, ", ha scritto '",messageDecode,"'")

    answer = numero_primo(int(messageDecode))
    serverSocket.sendto(answer.encode("utf-8"),clientAddress)
    print("ho riposto al client: ", answer)