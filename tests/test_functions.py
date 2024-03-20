# CHIEDERE SE IL CODICE DI TESTINNG DOBBIAMO RIULASCIARLO NELLA REPOSITORY DEL PROGETTO
"""Modulo per testare le funzioni del bot"""
from datetime import date, timedelta
from pytest_mock import MockerFixture
import pytest
from telegram.ext import Application
from utils.helper.gethelp import generate_url, get_date_range
from utils.helper.classes import ZoneMap
from data.testuale import TESTO_01
from data.testuale import MENU
from data.testuale import BENVENUTO
import bot_quake

from bot_quake import info, file_reader, start, handle_message # pylint: disable=unused-import


# dizionario di test per la funzione getdaterange
tests1_dict = [
    {
        "input": 1,
        "output": [date.today() - timedelta(days=1), date.today()]
    },
    {
        "input": 2,
        "output": [date.today() - timedelta(days=2), date.today()]
    },
    {
        "input": 3,
        "output": [date.today() - timedelta(days=3), date.today()]
    },
    {
        "input": 4,
        "output": [date.today() - timedelta(days=4), date.today()]
    },
    {
        "input": 5,
        "output": [date.today() - timedelta(days=5), date.today()]
    },
    {
        "input": 0,
        "output": [date.today(), date.today()]
    },
    {
        "input": -2,
        "output": [date.today() - timedelta(days=7), date.today()]
    },
    {
        "input": -100,
        "output": [date.today() - timedelta(days=7), date.today()]
    },
    {
        "input": 100,
        "output": [date.today() - timedelta(days=100), date.today()]
    },
    {
        "input": 1000,
        "output": [date.today() - timedelta(days=1000), date.today()]
    }
]


# testo la funzione get_date_range
@pytest.mark.parametrize("tests", tests1_dict)
def test_get_date_range(tests: dict) -> None:
    """Effettua il test della funzione get_date_range"""
    # get date range deve tornare un array dobe il primo è data-timedelta
    # il secondo è il giorno di oggi
    mock_value = tests["input"]

    result = get_date_range(mock_value)

    assert result == tests["output"]


# dizionario di test per la funzione generate_url
zona = ZoneMap()
tests2_dict = [
    {
        "input1": 0,
        "input2": get_date_range(0),
        "input3": zona,
        "output": (
            f"https://webservices.ingv.it/fdsnws/event/1/query?starttime="
            f"{get_date_range(0)[0]}T00%3A00%3A00"
            f"&endtime={get_date_range(0)[1]}T23%3A59%3A59&minmag=-1&maxmag="
            f"{0}&mindepth=-10"
            f"&maxdepth=1000&minlat={zona.minlat}&maxlat={zona.maxlat}"
            f"&minlon={zona.minlon}&maxlon={zona.maxlon}"
            f"&minversion=100&orderby=time-asc&format=text&limit=100"
        ),
    },
    {
        "input1": 1,
        "input2": get_date_range(1),
        "input3": zona,
        "output": (
            f"https://webservices.ingv.it/fdsnws/event/1/query?starttime="
            f"{get_date_range(1)[0]}T00%3A00%3A00"
            f"&endtime={get_date_range(1)[1]}T23%3A59%3A59&minmag=-1&maxmag="
            f"{1}&mindepth=-10"
            f"&maxdepth=1000&minlat={zona.minlat}&maxlat={zona.maxlat}" # pylint: disable=too-few-public-methods
            f"&minlon={zona.minlon}&maxlon={zona.maxlon}"
            f"&minversion=100&orderby=time-asc&format=text&limit=100"
        ),
    },
    {
        "input1": -2,
        "input2": get_date_range(-2),
        "input3": zona,
        "output": (
            f"https://webservices.ingv.it/fdsnws/event/1/query?starttime="
            f"{get_date_range(-2)[0]}T00%3A00%3A00"
            f"&endtime={get_date_range(-2)[1]}T23%3A59%3A59&minmag=-1&maxmag="
            f"{-2}&mindepth=-10"
            f"&maxdepth=1000&minlat={zona.minlat}&maxlat={zona.maxlat}"
            f"&minlon={zona.minlon}&maxlon={zona.maxlon}"
            f"&minversion=100&orderby=time-asc&format=text&limit=100"
        ),
    },
    {
        "input1": 10,
        "input2": get_date_range(100),
        "input3": zona,
        "output": (
            f"https://webservices.ingv.it/fdsnws/event/1/query?starttime="
            f"{get_date_range(100)[0]}T00%3A00%3A00"
            f"&endtime={get_date_range(100)[1]}T23%3A59%3A59&minmag=-1&maxmag="
            f"{10}&mindepth=-10"
            f"&maxdepth=1000&minlat={zona.minlat}&maxlat={zona.maxlat}"
            f"&minlon={zona.minlon}&maxlon={zona.maxlon}"
            f"&minversion=100&orderby=time-asc&format=text&limit=100"
        ),
    }
]


# testo la funzione generate url
@pytest.mark.parametrize("tests2", tests2_dict)
def test_generateurl(tests2: dict) -> None:
    """Effettua il test della funzione generate_url"""
    output_function = generate_url(tests2["input2"], tests2["input1"], tests2["input3"])
    assert output_function == tests2["output"]


@pytest.mark.asyncio
async def test_start(mocker: MockerFixture):
    """Effettua il test della funzione start"""
    update = (
        mocker.AsyncMock()
    )   # come se creiamo un oggetto fittizio update
        # l'oggetto fittizio sa come vengono eseguiti isuoi metodi
        # e verifica se i metodi vengono chiamati come devono esserli fatti
    update.message.reply_text = mocker.AsyncMock()

    await bot_quake.start(
        update, None
    )  # invochiamo la funzione che al suo interno invoca update.message.reply_text

    response = (
        BENVENUTO
        + MENU
    )
    update.message.reply_text.assert_called_once_with(
        response
    )  # vediamo se la funzione mockata viene invocata e con quali parametri


@pytest.mark.asyncio
async def test_send_info(mocker: MockerFixture):
    """Effettua il test della funzione send_info"""
    update = (
        mocker.AsyncMock()
    )   # come se creiamo un oggetto fittizio update
        #(l'oggetto fittizio sa come vengono eseguiti i suoi metodi
        # e verifica se i metodi vengono chiamati come devono esserli fatti)
    update.message.reply_text = mocker.AsyncMock()

    await bot_quake.info(
        update, None
    )  # invochiamo la funzione che al suo interno invoca update.message.reply_text

    response = (
        TESTO_01
        + MENU
    )

    update.message.reply_text.assert_called_once_with(
        response
    )  # vediamo se la funzione mockata viene invocata e con quali parametri


@pytest.mark.asyncio
async def test_handle_message(mocker: MockerFixture):
    """Effettua il test della funzione handle_message"""
    # creiamo un oggetto fittizio update
    # (l'oggetto fittizio sa come vengono eseguiti isuoi metodi
    # e verifica se i metodi vengono effettivmanrte chimati come devono esserli fatti)
    # questo ci pemrette di evitare di isolare tutte le dipendenze dell oggetto,
    # in questo caso update, così che testiamo solo la parte di codice che ci interessa
    #(in questo caso handle_message)
    update = mocker.AsyncMock()
    update.message.text = (
        "Messaggio Inviato"  # col mock possiamo presettare un valore che ci serve
    )
    # senza mock non sapremmo che messaggio ci invia l'utente quindi non potremmo testare
    # con il mock creiamo un oggetto fittizo update e gli impostiamo dei valori prestabiliti
    # così da testare la funzionalità di handle_message

    # creiamo una funzione fittizzia così che per testarla
    # non c'è bisongo che effettivamente esge la funzione per mandrae messaggi
    # ( darebbe errori perche non siamo connessi...)
    # ma testiamo solo se essa effettivamente viene chiamata e con quali parametri
    update.message.reply_text = mocker.AsyncMock()

    await bot_quake.handle_message(
        update, None
    )  # invochiamo la funzione che al suo interno invoca update.message.reply_text

    response = (
        f"Hai scritto {update.message.text}, usa / seguito da un comando valido\n"
    ) + MENU
    update.message.reply_text.assert_called_once_with(
        response
    )  # vediamo se la funzione mockata viene invocata e con quali parametri



@pytest.mark.asyncio
async def test_file_reader_with_range_error(mocker: MockerFixture):
    """Effettua il test della funzione test_file_reader"""

    update = mocker.AsyncMock()
    update.message.text = (
        "recente 20"  # col mock possiamo presettare un valore che ci serve
    )

    update.message.reply_text = mocker.AsyncMock()

    await bot_quake.file_reader(
        update, None
    )  # invochiamo la funzione che al suo interno invoca update.message.reply_text

    update.message.reply_text.assert_called_once_with(
        "Inserire un numero da 1 a 10"
    )  # vediamo se la funzione mockata viene invocata e con quali parametri

@pytest.mark.asyncio
async def test_file_reader_with_type_error(mocker: MockerFixture):
    """Effettua il test della funzione test_file_reader"""

    update = mocker.AsyncMock()
    update.message.text = (
        "recente a"  # col mock possiamo presettare un valore che ci serve
    )

    update.message.reply_text = mocker.AsyncMock()

    await bot_quake.file_reader(
        update, None
    )  # invochiamo la funzione che al suo interno invoca update.message.reply_text

    update.message.reply_text.assert_called_once_with(
         "Inserire un numero da 1 a 10 rilevati caratteri non numerici"
    )  # vediamo se la funzione mockata viene invocata e con quali parametri

@pytest.mark.asyncio
async def test_file_reader_with_none_message_error(mocker: MockerFixture):
    """Effettua il test della funzione test_file_reader"""

    update = mocker.AsyncMock()
    update.message.text = (
        None # col mock possiamo presettare un valore che ci serve
    )

    update.message.reply_text = mocker.AsyncMock()

    await bot_quake.file_reader(
        update, None
    )  # invochiamo la funzione che al suo interno invoca update.message.reply_text

    update.message.reply_text.assert_called_once_with(
         MENU
    )  # vediamo se la funzione mockata viene invocata e con quali parametri
def test_build_bot(mocker: MockerFixture):
    """Effettua il test della funzione build_bot"""
    Application.builder = mocker.Mock()

    # oss: si potrebbe testare .token.build()

    bot_quake.build_bot("token")

    Application.builder.assert_called_once()
    # vediamo se la funzione builder è chiamata almeno una volta

def test_setup_bot(mocker: MockerFixture):
    """Effettua il test della funzione setup_bot"""
    application = mocker.Mock()
    application.add_handler = (
        mocker.Mock()
    )  # mockiamo la funzione add_handler così che il suo comportamento non ci interessa

    bot_quake.setup_bot(application)  # richiamiamo set_up bot

    assert (
        application.add_handler.call_count == 4
    )  # vediamo se effttivamente è chiamata una volta

# ci manca da testare get_coordinates della classe
