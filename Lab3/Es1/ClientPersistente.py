from socket import *

serverIp = "localhost"
serverPort = 12001

serverAddress = (serverIp, serverPort)

clientSocket = socket(AF_INET, SOCK_STREAM)
print("CLIENT : provo a connettermi al server")
clientSocket.connect(serverAddress)
print("CLIENT : sono connesso al server")

while True :
    request = input("CLIENT : inserisci una stringa (punto per terminare): ")
    clientSocket.send(request.encode("utf-8"))

    if request == ".":
        print("CLIENT : l'utente ha inserito il punto quindi termino ")
        break

    print("CLIENT : Ho inviato la richiesta")
    answer = clientSocket.recv(1024)
    print("CLIENT : Il server ha risposto : ", answer.decode("utf-8"))

clientSocket.close()
print("CLIENT : socket chiusa")





