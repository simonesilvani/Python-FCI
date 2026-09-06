# Fondamenti di Comunicazione e Internet

Repository dedicata allo studio e allo svolgimento degli esercizi del corso di **Fondamenti di Comunicazione e Internet**.

Il progetto raccoglie implementazioni, esperimenti e simulazioni realizzate in **Python**, con particolare attenzione alla comunicazione di rete, ai protocolli **TCP e UDP**, all'architettura **client-server** e all'analisi dei risultati tramite **grafici**.

---

## 📚 Argomenti

La repository comprende principalmente:

* Modello client-server
* Socket in Python
* Protocollo **TCP**
* Protocollo **UDP**
* Comunicazione tra client e server
* Invio e ricezione di dati
* Visualizzazione dei dati con `matplotlib.pyplot`
* Confronto tra TCP e UDP
* Challenge finale

---

## 🔌 TCP

Gli esercizi TCP sono dedicati allo studio della comunicazione **connection-oriented** tramite socket.

Il modello prevede la presenza di un **server** che rimane in ascolto e di uno o più **client** che stabiliscono una connessione con esso.

### Comunicazione TCP

```text
┌──────────────┐                         ┌──────────────┐
│    CLIENT    │                         │    SERVER    │
│              │                         │              │
│  socket()    │                         │  socket()    │
│  connect()   │ ─────── richiesta ────► │  bind()      │
│              │                         │  listen()    │
│              │ ◄────── risposta ────── │  accept()    │
│  send/recv   │                         │  send/recv   │
└──────────────┘                         └──────────────┘
```

### Caratteristiche

| Caratteristica         | TCP                              |
| ---------------------- | -------------------------------- |
| Tipo di comunicazione  | Connection-oriented              |
| Connessione            | Necessaria                       |
| Affidabilità           | Alta                             |
| Ordinamento dei dati   | Garantito                        |
| Ritrasmissione         | Sì                               |
| Controllo degli errori | Sì                               |
| Overhead               | Maggiore                         |
| Utilizzo tipico        | Trasmissione affidabile dei dati |

---

## 📡 UDP

Gli esercizi UDP analizzano la comunicazione **connectionless** attraverso datagrammi.

A differenza di TCP, UDP non richiede la creazione di una connessione prima dello scambio dei dati.

```text
┌──────────────┐                         ┌──────────────┐
│    CLIENT    │                         │    SERVER    │
│              │                         │              │
│  socket()    │                         │  socket()    │
│              │ ─────── datagram ─────► │  recvfrom()  │
│  sendto()    │ ◄────── datagram ────── │  sendto()    │
└──────────────┘                         └──────────────┘
```

### Caratteristiche

| Caratteristica         | UDP                                    |
| ---------------------- | -------------------------------------- |
| Tipo di comunicazione  | Connectionless                         |
| Connessione            | Non necessaria                         |
| Affidabilità           | Non garantita                          |
| Ordinamento dei dati   | Non garantito                          |
| Ritrasmissione         | No                                     |
| Controllo degli errori | Limitato                               |
| Overhead               | Minore                                 |
| Utilizzo tipico        | Comunicazioni rapide e a bassa latenza |

---

## ⚖️ TCP vs UDP

Il confronto tra i due protocolli rappresenta uno degli aspetti principali degli esperimenti presenti nella repository.

| Aspetto              | TCP                    | UDP                    |
| -------------------- | ---------------------- | ---------------------- |
| Connessione          | Sì                     | No                     |
| Affidabilità         | Sì                     | No                     |
| Ordine dei pacchetti | Garantito              | Non garantito          |
| Perdita dei dati     | Gestita                | Possibile              |
| Ritrasmissione       | Sì                     | No                     |
| Controllo del flusso | Sì                     | No                     |
| Overhead             | Maggiore               | Minore                 |
| Velocità             | Generalmente inferiore | Generalmente superiore |
| Latenza              | Generalmente maggiore  | Generalmente minore    |


---

## 🖥️ Architettura Client-Server

Gli esercizi permettono di comprendere il funzionamento dell'architettura **client-server** attraverso l'utilizzo delle socket.

Il **server** mette a disposizione un servizio e rimane in ascolto delle richieste, mentre il **client** avvia la comunicazione e scambia dati con il server.

### Flusso generale

```text
              CLIENT
                 │
                 │ richiesta
                 ▼
          ┌──────────────┐
          │    SERVER    │
          └──────┬───────┘
                 │
                 │ elaborazione
                 ▼
          ┌──────────────┐
          │   RISPOSTA   │
          └──────┬───────┘
                 │
                 ▼
              CLIENT
```

---

## 🧪 Challenge finale

La repository contiene anche una **challenge finale**, pensata come applicazione pratica delle conoscenze acquisite durante il corso.

La challenge riunisce diversi concetti affrontati negli esercizi precedenti:

* socket;
* comunicazione client-server;
* TCP e UDP;
* gestione dei messaggi;
* raccolta dei dati;
* misurazione delle prestazioni;
* analisi dei risultati;
* creazione di grafici;
* confronto tra protocolli.

### 🎯 Obiettivo

L'obiettivo della challenge è sviluppare una soluzione completa che permetta di applicare concretamente i concetti di comunicazione di rete studiati durante il corso.

La challenge rappresenta il **progetto conclusivo** della repository e permette di integrare le conoscenze teoriche con la loro implementazione pratica in Python.

---

## 👨‍💻 Contributi e obiettivi

Chiunque può contribuire al suo miglioramento attraverso correzioni, nuovi esercizi, esempi, approfondimenti o aggiornamenti del materiale, mantenendola attuale e utile anche per gli studenti degli anni successivi.

L'obiettivo è mettere a disposizione materiale, esercizi ed esempi utili non solo agli studenti che frequentano questo tipo di corso, ma anche a chiunque sia interessato ad approfondire i concetti di reti, protocolli di comunicazione e programmazione client-server.

Attraverso gli esercizi e gli esperimenti presenti nella repository, l'obiettivo è acquisire una conoscenza pratica dei principali concetti di comunicazione e networking, imparando a:

* comprendere il funzionamento delle **socket**;
* comprendere e implementare l'architettura **client-server**;
* distinguere le caratteristiche e il funzionamento di **TCP e UDP**;
* sviluppare applicazioni client-server in **Python**;
* realizzare esperimenti di comunicazione e analizzarne i risultati;
* raccogliere e organizzare i dati ottenuti;
* valutare le prestazioni dei protocolli attraverso parametri e misure significative;
* rappresentare i risultati tramite **grafici e tabelle**;
* confrontare sperimentalmente **TCP e UDP**;
* applicare le conoscenze acquisite nella **challenge finale**.

---


