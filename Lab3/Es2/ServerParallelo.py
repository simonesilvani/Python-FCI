from socket import *
from threading import Thread

def gestisciClient(connSocket):
    while True:
        request = connSocket.recv(1024)
        requestDecode = request.decode("utf-8")
        print("SERVER : ricevuto : ", requestDecode)
        if requestDecode == ".":
            print("SERVER : client vuole chiudere")
            break



serverPort = 12001
welcomeSocket = socket(AF_INET, SOCK_STREAM)
welcomeSocket.bind(("", serverPort))
welcomeSocket.listen(1)

while True:
    connectionSocket, clientAddress = welcomeSocket.accept()
    #   GENERO THREAD
    thread = Thread(target= gestisciClient, args=((connectionSocket, )))
    thread.start()

