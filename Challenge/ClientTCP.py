from socket import *
import json
import requests
import os

serverAddress = (os.getenv("FCI_SERVER_IP", "127.0.0.1"), 12100)

clientSocket = socket(AF_INET, SOCK_STREAM)

clientSocket.connect(serverAddress)
print("connected server", serverAddress)

# Dati personali: impostali come variabili d'ambiente, non scriverli
# mai nel codice versionato.
#   export FCI_SERVER_IP="ip.del.server"
#   export FCI_EMAIL="tua.email@example.com"
#   export FCI_PERSON_CODE="12345678"
EMAIL = os.getenv("FCI_EMAIL", "nome.cognome@example.com")
PERSON_CODE = int(os.getenv("FCI_PERSON_CODE", "0"))

data = {
    "email": EMAIL,
    "person_code": PERSON_CODE,
    "msg_code" : "ksbp87rd"
}
for i in range(4):
    message = json.dumps(data)


    clientSocket.send(message.encode("utf-8"))
    print("sent message", message)
    serverMessage, serverAddress = clientSocket.recvfrom(2048)
    serverMessage = serverMessage.decode("utf-8")
    print("message server : " + serverMessage)
    clientSocket.close()

