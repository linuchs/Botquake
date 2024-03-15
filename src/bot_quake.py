""" definisce le funzioni e le classi che servono ad aprire le URLS"""
from urllib.request import urlopen
import ssl
from telegram.ext import Application, CommandHandler, MessageHandler, filters
from telegram import Update
from telegram.ext import ContextTypes
from utils.helper.gethelp import get_date_range
from utils.helper.gethelp import generate_url
from utils.helper.classes import ZoneMap
from data.testuale import TESTO_01
from data.testuale import MENU
from data.testuale import BENVENUTO




# funzioni che verranno assegnate ad un gestore legate ad un certo messaggio


# questa richiamata al messaggio /recente
async def file_reader(update, context) -> None:
    """Inizio impostando la ricerca dei dati fino a 7 giorni indietro"""
    intervallo_date = get_date_range(7)

    # instanzio la zona di interesse ovvero massimo e minimo di latitudine e longitudine
    zona = ZoneMap()

    # Imposto la magnitudo massima che non deve superare 10, questa potra
    massima_magnitudo = 10

    if update.message.text is None:
        comandi = ""
    else:
        comandi = update.message.text
        # Adesso il comando passato è diviso e ne posso gestire le eventuali funzionalità
        splitted_command = comandi.split()
        if len(splitted_command) > 1:
            if splitted_command[1].isnumeric():
                if int(splitted_command[1]) < 10 and int(splitted_command[1]) > 0:
                    massima_magnitudo = splitted_command[
                        1
                    ]  # Impostiamo la magnitudo passata dal comando che poi passeremo all'url
                else:
                    await update.message.reply_text("Inserire un numero da 1 a 10")
                    return
            else:
                await update.message.reply_text(
                    "Inserire un numero da 1 a 10 rilevati caratteri non numerici"
                )
                return

    filename = generate_url(intervallo_date, massima_magnitudo, zona)

    # questo pezzo lo eseguo solo se non sto facendo testing
    if filename:
        context = ssl.create_default_context()  # serve per il certificato ssl
        with urlopen(
            filename, context=context
        ) as f:  # Ricordiamoci ce il filename è remoto
            file_lines = [x.decode("utf8").strip() for x in f.readlines()]
            if len(file_lines) == 0:  # file vuoto quindi non ci sono dati rilevati
                await update.message.reply_text(
                    "Nell'arco di tempo rilevato non ci sono dati relativi ai parametri richiesti"
                )
            else:
                file_header_line = file_lines[0].split("|")
                file_header_line[0] = file_header_line[0].replace("#", "")
                file_body_line = file_lines[1].split("|")  # splitting sulle righe

                reply_string = "Dati relativi all'evento sismico più recente: "
                lunghezza_stringa_comandi = len(file_header_line)
                for i in range(lunghezza_stringa_comandi):
                    file_header_line[i] = file_header_line[i].replace("\n", "")
                    reply_string = (
                        reply_string
                        + "\n"
                        + file_header_line[i]
                        + ": "
                        + file_body_line[i]
                    )
                await update.message.reply_text(reply_string)
                # questi di seguito sono i dati per la creazione della mappa
                await update.message.reply_venue(
                    file_body_line[2],  # latitudine
                    file_body_line[3],  # longitudine
                    file_body_line[12],  # LocationName
                    f"Profondità: {file_body_line[4]}",
                )
                await update.message.reply_text(MENU)


# questa invocata al messaggio /descrizione
async def start(update: Update, _context: ContextTypes.DEFAULT_TYPE) -> None:
    """Mostra una descrizione del bot."""
    response = (
        BENVENUTO
        + MENU
    )
    await update.message.reply_text(response)


# questa invocata al messaggio /info
async def info(update: Update, _context: ContextTypes.DEFAULT_TYPE) -> None:
    """Mostra informazioni sulle licenze dei dati"""
    response = (
        TESTO_01
        + MENU
    )
    await update.message.reply_text(response)


# funzione ausiliaria
async def handle_message(update: Update, _context: ContextTypes.DEFAULT_TYPE) -> None:
    """Risponde a messaggi non validi con un messaggio di aiuto."""
    response = (
        f"Hai scritto {update.message.text}, usa / seguito da un comando valido\n"
    ) + MENU
    await update.message.reply_text(response)


def setup_bot(application: Application) -> Application:
    """Imposta i gestori dei comandi per il bot."""
    application.add_handler(CommandHandler("info", info))
    application.add_handler(CommandHandler("recente", file_reader))
    application.add_handler(CommandHandler("descrizione", start))
    application.add_handler(MessageHandler(filters.TEXT, handle_message))


def build_bot(token_bot: str) -> Application:
    """Crea un bot con i gestori dei comandi."""
    # con pyhton 3.12 e versione python-telegram-bot  20.8
    application = Application.builder().token(token_bot).build()
    setup_bot(application)
    return application


def main() -> None:
    """Funzione principale del bot"""
    token_bot = os.environ[
        "TELEGRAM_BOT"
    ]  # Con questo parametro se invoco il main non nel testing mi parte il bot in attessa
    # senno mi permette di ottenre l'output del testing
    # con pyhton 3.12 e versione python-telegram-bot  20.8
    application = build_bot(token_bot=token_bot)

    application.run_polling()


if __name__ == "__main__":
    # con pyhton 3.12 e versione python-telegram-bot  20.8
    main()
