
import requests
import os


#REQUEST HTTP
answer = requests.get(os.getenv("FCI_SERVER_IP", "127.0.0.1"))
n_request = 1


#ELAPSED = Header+Dati+RTT+Header
#NON DIPENDE PERò DA QUANTO CONTENUTO C'È

print(answer, "tempo di risposta:"+str( answer.elapsed ), "---> in ms", answer.elapsed.microseconds / 1000)

#stringa che restituisce tutti gli oggetti della pagina in HTML ma il contenuto è identico a quello che vediamo online
#print(answer.content)

