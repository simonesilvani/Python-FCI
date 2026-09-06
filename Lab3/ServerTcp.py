from socket import *


serverPort = 12000


#   QUESTA SOCKET GESTISCE SOLO LE CONNESSIONI
#VERSIONE E TIPO
welcomeSocket = socket(AF_INET, SOCK_STREAM)
welcomeSocket.bind(("", serverPort))


#   DIMENSIONE DELLA CODA DEI CLIENT
welcomeSocket.listen(1)
print("SERVER: pronto a ricevere")


#I CLIENT VANNO IN CODA BLOCCANDO LA ACCEPT
while True :
    #ACCETTO LA CONNESSIONE DI UN CLIENT
    #ASPETTO UNA CONNESSIONE E RITORNA LA SOCKET PER SINGOLO E L'INDIRIZZO DEL CLIENT
    connectionSocket, clientAddress = welcomeSocket.accept()
    print("SERVER: il client si è connesso : ", clientAddress)

    request = connectionSocket.recv(1024)
    requestDecode = request.decode("utf-8")
    print("SERVER: il client ha inviato : ", requestDecode)

    print("SERVER: preparo la risposta")

    answer = requestDecode.upper()
    print("SERVER: risposta pronta")

    connectionSocket.send(answer.encode("utf-8"))
    print("SERVER: ho risposto al client")

    connectionSocket.close()
    print("SERVER: socket con il client chiusa, no la welcome")
    print(" ")

#COSA CAMBIA IN TCP
#   ACCEPT







