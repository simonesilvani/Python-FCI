from socket import *
import json
import os

server_ip = os.getenv("FCI_SERVER_IP", "127.0.0.1")
server_port = 13000
server_address = (server_ip, server_port)

client_socket = socket(AF_INET, SOCK_DGRAM)

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
    "msg_code": "rif7d6o8z9k"
}

for i in range(4):
    print(f"Invio messaggio {i + 1}/3...")

    message = json.dumps(data)
    client_socket.sendto(message.encode("utf-8"), server_address)


    try:

        client_socket.settimeout(2.0)

        server_reply, server_add = client_socket.recvfrom(1024)
        print(f"Risposta {i + 1}: {server_reply.decode('utf-8')}")

    except timeout:
        print(f"Errore: Il server non ha risposto al messaggio {i + 1}")
        break

client_socket.close()