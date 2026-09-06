import socket

serverPort = 12000

serverSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
serverSocket.bind(('', serverPort))
print("Server started on port ", serverPort)

while True:
    print("waiting for message")

    message, clientAddress = serverSocket.recvfrom(2048)
    print("Message received from ", clientAddress)

    messageDecode = message.decode("utf-8")
    print("Client message : ", messageDecode)

    input("Press any key to continue")
    answer = "Good job man, you succeeded to give me a message"

    serverSocket.sendto(answer.encode("utf-8"), clientAddress)

