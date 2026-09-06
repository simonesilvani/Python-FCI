from socket import *
import json
import threading
import os

server_address = (os.getenv("FCI_SERVER_IP", "127.0.0.1"), 12100)

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
    "msg_code": "ksbp87rd"
}

def send_client(client_id):
    sock = socket(AF_INET, SOCK_STREAM)   # TCP
    sock.settimeout(5.0)
    try:
        sock.connect(server_address)
        message = json.dumps(data).encode("utf-8")
        sock.send(message)
        print(f"[Client {client_id}] Inviato: {message.decode()}")
        reply = sock.recv(2048)
        print(f"[Client {client_id}] Risposta: {reply.decode('utf-8')}")
    except Exception as e:
        print(f"[Client {client_id}] Errore: {e}")
    finally:
        sock.close()

threads = [threading.Thread(target=send_client, args=(i+1,)) for i in range(4)]
for t in threads:
    t.start()
for t in threads:
    t.join()