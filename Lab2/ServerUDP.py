from socket import *

#   NON CI INTERESSA CONOSCERE L'INDIRIZZO IP
serverPort = 12000 #STESSA DEL CLIENT CHE CONOSCE

#   DEFINISCO LA SOCKET
serverSocket = socket(AF_INET, SOCK_DGRAM)

#    ASSOCIARE LA PORTA CORRETTA ALLA SOCKET (DUPLA)
serverSocket.bind(('', serverPort))
print("Server started on port ", serverPort)

#   LOOP INFINITO
while True:
    #   RICEVO LA RICHIESTA DAL CLIENT
    message , clientAddress = serverSocket.recvfrom(2040)

    #   DECODIFICO E STAMPO
    messageDecode = message.decode("utf-8")
    print("il client", clientAddress, " ha scritto : ",messageDecode)

    #   DECODIFICA TUTTA IN MAIUSCIOLO
    answer = messageDecode.upper()

    # VOGLIO CHE IL SERVER SI BLOCCHI PRIMA DI INVIARE AL CLIENT E ASPETTI UN SEGNALE
    # IL SERVER VEDE IL MESSAGGIO SCRITTO
    # input("sono bloccato finchè non premi invio")
    serverSocket.sendto(answer.encode("utf-8"), clientAddress)


    print("ho risposto al client : ", answer)


#   NON CHIUDO LA SOCKET PERCHè DEVE ESSERE SEMPRE ATTIVO PER I CLIENT
#   NUMERO DI PORTA CAMBIA DEL SECONDO SERVER