from socket import *


serverIp = "localhost"
serverPort = 12000
serverAddress = (serverIp, serverPort)


#   SOCKET CLIENT
#   SOCKET_STREAM for TCP
clientSocket = socket(AF_INET, SOCK_STREAM)


#   CONNETTO AL SERVER
print("CLIENT: provo a connettermi al server")
clientSocket.connect(serverAddress)
print("CLIENT: connesso al server!!!")


#   INVIARE MESSAGGIO send
request = input("CLIENT: inserisci una frase: ")
clientSocket.send(request.encode("utf-8"))
print("CLIENT: ho inviato il messaggio")


#   RISPOSTA SERVER
# no from perchè so già che sono connesso a quel server
serverAnswer = clientSocket.recv(1024) # BIT CHE POSSO LEGGERE
print("CLIENT: ricevuto la risposta dal server")
serverAnswerDecode = serverAnswer.decode("utf-8")
print("CLIENT: codificato la risposta")


#   STAMPO RISPOSTA CODIFICATA
print("CLIENT: il server ha risposto : ", serverAnswerDecode)


#   CHIUDO SOCKET
clientSocket.close()


#COSA CAMBIA IN TCP
#   SOCK_STREAM
#   CONNECT
#   SEND
#   RECV

