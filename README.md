## Botquake
Botquake è un progetto per il corso di Quality Development
### Cosa ci proponiamo di realizzare
Ciò che si intende realizzare è un BOT Telegram, ovvero una applicazione eseguita sulla nostra macchina la quale comportandosi da server estenderà le funzionalità del server di Telegram, al quale un utente potrà inviare comandi mediante l'interfaccia di chat messa a disposizione dal client di Telegram. Il comando sarà reindirizzato alla nostra macchina che darà risposta tramite il server Telegram al client dal quale l'utente ha inviato il comando.
#### Specifiche dell'applicazione Botquake
L'applicazione elaborerà i dati forniti sul sito https://terremoti.ingv.it/ dall'Ingv,sotto licenTza Creative Commons Attribution 4.0 International https://creativecommons.org/licenses/by/4.0/.
I dati fanno parte di una database di eventi relativi a diverse reti di rilevazione mondiale di terremeventi sismici, per il nostro scopo restringeremo la zona di interesse all'area Etnea.
L'utente potrà interagire con il Bot tramite appositi comandi, in particolare potra richiedere i dati sull'ultimo terremoto avvenuto nell'area di interesse, nonchè potra affinare la ricerca con un apposito comando impostando una magnitudine massima.
![botfather](images/botquake_01.jpg)
Alla richiesta il bot risponderà con i dati dell'ultimo terremoto relativo al comando inviato.
Seguirà una mappa relativa al luogo dell'evento con il grado di magnitudine dell'evento sismico rilevato.
![botfather](images/botquake_02.jpg)


 
### BotFather 
#### Inizializzazione del Bot
##### Ottenere la chiave API per il BOT:
Dobbiamo aprire la versione desktop o la versione mobile di Telegram, quindi cercare 'BotFather' come mostrato nella figura.
![botfather](images/botfather_01.jpg)
Bisogna per prima cosa inizializzare attraverso la chat di Telegram BotFather la chat Bot per il nostro progetto, impostare il nome del Bot e l'identificativo che deve terminare con il suffisso bot, per fare questo basta seguire l'albero dei comandi come dalla figura sotto.
![botfather](images/botfather_02.jpg)
#### Chiave di autenticazione del Bot
Una volta finito il primo step, BotFather ci assegnerà un token che sarà la chiave di autenticazione del nostro progetto sul server Telegram.
>[!Note]
>Qualora si voglia eseguire il bot localmente decommentare la riga 130
>`token_bot = "IL_TUO_TOKEN_BOT`
>del file src/bot_quake.py e inserire il Token Telegram al posto di "IL_TUO_TOKEN_BOT", >contestualmente commentare la riga successiva,
>`token_bot = os.environ.get("TELEGRAM_BOT")`.
>Altrimenti andare su "SETTINGS" e scegliere "SECURITY" e di seguito "Secrets and Variables"
>quindi in "Repository" creare un nuovo "Repository secrets" chiamarlo 'TELEGRAM_BOT' e assegnargli il token del bot fornito da Telegram.

#### Libreria telegram per python
La libreria python-telegram-bot https://pypi.org/project/python-telegram-bot/ ci servirà per interagire con le API di Telegram questa permetterà di impostare la comunicazione tra la il server telegram e l'applicazione in esecuzione sulla nostra macchina.

## Requisiti
Python versione 3.12
python-telegram-bot 21.0.1
### Librerie Python relative al linter
pylint
### Librerie Python per i test
<ul>
    <li>pytest 8.0.2</li>
    <li>pytest_mock 3.6.1</li>
</ul>


#### Comandi utili
<ul>
    <li>python --version : ritorna la versione di python installata sul sistema</li>
    <li>pip3 list : ritorna la lista delle librerie python installate</li>
    <li>python -m  pipreqs.pipreqs : crea un file requirements.txt con le librerie extra installate </li>
</ul>







