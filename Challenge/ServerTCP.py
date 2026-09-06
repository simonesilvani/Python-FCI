from socket import *

serverPort = 12000

serverSocket = socket(AF_INET, SOCK_STREAM)

serverSocket.bind(('', serverPort))

serverSocket.listen(1)
print("Server started on port ", serverPort)

voc = ["A", "E", "I", "O", "U", "a", "e", "i", "o", "u"]

while True:
    connectionSocket, clientAddress = serverSocket.accept()
    print("client connected")

    request = connectionSocket.recv(2048)
    requestDecode = request.decode("utf-8")

    print("Client send me  : ", requestDecode)

    num = len(requestDecode)
    for i in voc:
        num = num - requestDecode.count(i)

    answer = "num di cons : " + str(num)
    connectionSocket.send(answer.encode("utf-8"))

    connectionSocket.close()



