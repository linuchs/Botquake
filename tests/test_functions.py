#CHIEDERE SE IL CODICE DI TESTINNG DOBBIAMO RIULASCIARLO NELLA REPOSITORY DEL PROGETTO
from utils.helper.gethelp import get_date_range
from utils.helper.gethelp import generate_url
from utils.helper.classes import ZoneMap
import bot_quake 

import pytest 
from pytest_mock import MockerFixture

from telegram import Update
from telegram.ext import ContextTypes,Application,CommandHandler
from datetime import date, timedelta

MENU = """
Sotto troverai la lista comandi:
/descrizione -> Descrizione del canale.
/recente -> Per visualizzare evento sismico più recente, se il comando è seguito da un numero da 1 a 10 cambia la magnitudo massima.
/info -> Mostra link utili e informazioni sui dati.
"""

#dizionario di test per la funzione getdaterange
tests1_dict = [{
    "input":1,"output":[date.today()-timedelta(days=1),date.today()],
    "input":2,"output":[date.today()-timedelta(days=2),date.today()],
    "input":3,"output":[date.today()-timedelta(days=3),date.today()],
    "input":4,"output":[date.today()-timedelta(days=4),date.today()],
    "input":6,"output":[date.today()-timedelta(days=5),date.today()],
    "input":0,"output":[date.today(),date.today()],
    "input":-2,"output":[date.today()-timedelta(days=7),date.today()],
    "input":-100,"output":[date.today()-timedelta(days=7),date.today()],
    "input":100,"output":[date.today()-timedelta(days=100),date.today()],
    "input":1000,"output":[date.today()-timedelta(days=1000),date.today()],
}]

#testo la funzione get_date_range
@pytest.mark.parametrize("tests",tests1_dict)
def test_get_date_range(tests :dict) -> None:
    #get date range deve tornare un array dobe il primo è data-timedelta il secondo è il giorno di oggi 
    mock_value = tests["input"]
    
    result = get_date_range(mock_value)

    assert result == tests["output"]


#dizionario di test per la funzione generate_url 
zona = ZoneMap()
tests2_dict = [
    {
        "input1":0,"input2":get_date_range(0),"input3":zona,"output":(f"https://webservices.ingv.it/fdsnws/event/1/query?starttime="
                                                                      f"{get_date_range(0)[0]}T00%3A00%3A00"
                                                                      f"&endtime={get_date_range(0)[1]}T23%3A59%3A59&minmag=-1&maxmag="
                                                                      f"{0}&mindepth=-10"
                                                                      f"&maxdepth=1000&minlat={zona.minlat}&maxlat={zona.maxlat}"
                                                                      f"&minlon={zona.minlon}&maxlon={zona.maxlon}"
                                                                      f"&minversion=100&orderby=time-asc&format=text&limit=100"),
        "input1":1,"input2":get_date_range(1),"input3":zona,"output":(f"https://webservices.ingv.it/fdsnws/event/1/query?starttime="
                                                                      f"{get_date_range(1)[0]}T00%3A00%3A00"
                                                                      f"&endtime={get_date_range(1)[1]}T23%3A59%3A59&minmag=-1&maxmag="
                                                                      f"{1}&mindepth=-10"
                                                                      f"&maxdepth=1000&minlat={zona.minlat}&maxlat={zona.maxlat}"
                                                                      f"&minlon={zona.minlon}&maxlon={zona.maxlon}"
                                                                      f"&minversion=100&orderby=time-asc&format=text&limit=100"),
        "input1":-2,"input2":get_date_range(-2),"input3":zona,"output":(f"https://webservices.ingv.it/fdsnws/event/1/query?starttime="
                                                                      f"{get_date_range(-2)[0]}T00%3A00%3A00"
                                                                      f"&endtime={get_date_range(-2)[1]}T23%3A59%3A59&minmag=-1&maxmag="
                                                                      f"{-2}&mindepth=-10"
                                                                      f"&maxdepth=1000&minlat={zona.minlat}&maxlat={zona.maxlat}"
                                                                      f"&minlon={zona.minlon}&maxlon={zona.maxlon}"
                                                                      f"&minversion=100&orderby=time-asc&format=text&limit=100"),
        "input1":10,"input2":get_date_range(100),"input3":zona,"output":(f"https://webservices.ingv.it/fdsnws/event/1/query?starttime="
                                                                      f"{get_date_range(100)[0]}T00%3A00%3A00"
                                                                      f"&endtime={get_date_range(100)[1]}T23%3A59%3A59&minmag=-1&maxmag="
                                                                      f"{10}&mindepth=-10"
                                                                      f"&maxdepth=1000&minlat={zona.minlat}&maxlat={zona.maxlat}"
                                                                      f"&minlon={zona.minlon}&maxlon={zona.maxlon}"
                                                                      f"&minversion=100&orderby=time-asc&format=text&limit=100")
    }
]

#testo la funzione generate url
@pytest.mark.parametrize("tests2",tests2_dict)
def test_generateurl(tests2:dict) -> None:

    output_function = generate_url(tests2["input2"],tests2["input1"],tests2["input3"])
    assert output_function == tests2["output"]


@pytest.mark.asyncio
async def test_start(mocker: MockerFixture):

    update = mocker.AsyncMock()      #come se creiamo un oggetto fittizio update (l'oggetto fittizio sa come vengono eseguiti isuoi metodi e verifica se i metodi vengono effettivmanrte chimati come devono esserli fatti)
    update.message.reply_text = mocker.AsyncMock()  
 
    await bot_quake.start(update,None)   #invochiamo la funzione che al suo interno invoca update.message.reply_text

    response = """Benvenuto in BOTQUAKE questo è un sistema automatizzato per visualizzare l'ultimo evento 
                  sismico tra gli eventi degli ultimi 7 giorni in una zona di interesse intorno al vulcano
                  Etna.
                  Inserisci un comando e un bot ti invierà le informazioni in base al comando digitato.\n"""+MENU 
    update.message.reply_text.assert_called_once_with(response)   #vediamo se la funzione mockata viene invocata e con quali parametri 

@pytest.mark.asyncio
async def test_send_info(mocker: MockerFixture):

    update = mocker.AsyncMock()      #come se creiamo un oggetto fittizio update (l'oggetto fittizio sa come vengono eseguiti isuoi metodi e verifica se i metodi vengono effettivmanrte chimati come devono esserli fatti)
    update.message.reply_text = mocker.AsyncMock()   
 
    await bot_quake.info(update,None)   #invochiamo la funzione che al suo interno invoca update.message.reply_text

    response = """
           I dati e i risultati pubblicati sulle pagine dall'INGV al link https://terremoti.ingv.it/
           e sono distribuiti sotto licenza Creative Commons Attribution 4.0 International License,
           con le condizioni al seguente link https://creativecommons.org/licenses/by/4.0 \n
           """+MENU 

    update.message.reply_text.assert_called_once_with(response)   #vediamo se la funzione mockata viene invocata e con quali parametri 


@pytest.mark.asyncio
async def test_handle_message(mocker: MockerFixture):
   
    
    update = mocker.AsyncMock()      #come se creiamo un oggetto fittizio update (l'oggetto fittizio sa come vengono eseguiti isuoi metodi e verifica se i metodi vengono effettivmanrte chimati come devono esserli fatti)
    update.message.reply_text = mocker.AsyncMock()  
    update.message.text = "Messaggio Inviato"

    await bot_quake.handle_message(update,None)   #invochiamo la funzione che al suo interno invoca update.message.reply_text

    response = (
        f"Hai scritto {update.message.text}, usa / seguito da un comando valido\n"
        )+MENU
    update.message.reply_text.assert_called_once_with(response)   #vediamo se la funzione mockata viene invocata e con quali parametri 


