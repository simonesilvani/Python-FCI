from socket import *

#   PARAMETRI DEL SERVER IP E PORTA
#   va bene anche mettere 127.0.0.1
serverIP = "localhost"
serverPort = 13000

#   DUPLA
serverAddress = (serverIP, serverPort)

clientSocket = socket(AF_INET, SOCK_DGRAM)


#   SETT0 UN TIMEOUT PER VERIFICARE CHE IL SERVER RISPONDE
timeLimit = 3
clientSocket.settimeout(timeLimit)

#   INPUT DA TASTIERA
message = input("Enter your message to send to server: ")

#   INVIA MESSAGGIO CODIFICATO AL SERVER
#   SENDTO INVIA E SPECIFICHIAMO A CHI
#   (   MESSAGGIO DA INVIARE CODIFICATO IN BIT  ,   DUPLA(INDIRIZZO IP E PORTA) )
clientSocket.sendto(message.encode("utf-8"), serverAddress)

#PROVA A FARE QUESTO
try:
    #   RICEVO LA RISPOSTA DAL SERVER
    modifiedMessage, serverAddress = clientSocket.recvfrom(2040) # 2040 LUNGHEZZA DEL BUFFER

    #   CODIFICA MESSAGGE
    modifiedMessage = modifiedMessage.decode("utf-8")

    print("server answer: ",modifiedMessage)

#GESTIAMO LE ECCEZZONI (ESEMPIO: TIMEOUT libreria timeout)
except TimeoutError:
    print("TIMEOUT SCADUTO: SERVER not avaible")

except TypeError:
    print("cosa stai cercando di fare? non posso contatenare stringa e numero")

#ALLA FINE CHIUDI IL SOCKET (PRASSI)
finally:
    #   CHIUDI LA SOCKET
    clientSocket.close()


#CON INPUT NEL SERVER PRIMA DI SENDTO
#SE APRO UNA SECOND CLIENT CHE INVIA UN MESSAGGIO
#E NON HO FATTO INVIO NEL SERVER
#IL MESSAGGIO SI METTE IN CODA