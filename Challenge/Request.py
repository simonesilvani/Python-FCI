
import requests
import os

ip = os.getenv("FCI_SERVER_IP", "127.0.0.1")
porta = 80

# PERCORSO E PAYLOAD DELLA CHALLANGE
#   export FCI_CHALLENGE_PATH="/percorso/assegnato"
#   export FCI_CHALLENGE_DATA="codice-assegnato"
path = os.getenv("FCI_CHALLENGE_PATH", "/percorso/della/challenge")
payload = os.getenv("FCI_CHALLENGE_DATA", "")

risposta = requests.post(f"http://{ip}:{porta}{path}", data=payload)

print(risposta.status_code)
print(risposta.text)
print(risposta.json())
