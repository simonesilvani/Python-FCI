from socket import *

serverPort = 12001

welcomeSocket = socket(AF_INET, SOCK_STREAM)
welcomeSocket.bind(("", serverPort))
welcomeSocket.listen(1)
print("SERVER : Welcome Socket pronta a ricevere connessioni client")

while True :
    connectionSocket, clientAddress = welcomeSocket.accept()
    print("SERVER : il client si è connesso, ", clientAddress)

    while True :
        request = connectionSocket.recv(1024)
        requestDecode = request.decode("utf-8")
        print("SERVER : il client ha inviato : ", requestDecode)

        if requestDecode == "." :
            print("SERVER : il client ", clientAddress, "è stato disconesso")
            break

        answer = requestDecode.upper()
        connectionSocket.send(answer.encode("utf-8"))

    print("SERVER : chiudo la connection socket")
    connectionSocket.close()








