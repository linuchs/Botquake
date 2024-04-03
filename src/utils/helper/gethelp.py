"""Helper module"""
from datetime import date, timedelta
from typing import List
from utils.helper.classes import ZoneMap




def get_date_range(d_range: int) -> List[date]:
    """la funzione imposta i valori temporali dei dati da scaricare
    in un range che va dal giorno attuale indietro di un valore d_range"""
    date_range: List[date] = [None] * 2
    today: date = date.today()
    if d_range < 0:
        days_inthe_past: date = today - timedelta(days=7)
    else:
        days_inthe_past: date = today - timedelta(days=d_range)
    date_range[0] = days_inthe_past
    date_range[1] = today
    return date_range


def generate_url(intervallo_date: List[date], massima_magnitudo: float, zona: ZoneMap) -> str:
    """Genera l'url per la richiesta dei dati sismici"""
    filename = (
        f"https://webservices.ingv.it/fdsnws/event/1/query?starttime="
        f"{intervallo_date[0]}T00%3A00%3A00"
        f"&endtime={intervallo_date[1]}T23%3A59%3A59&minmag=-1&maxmag="
        f"{massima_magnitudo}&mindepth=-10"
        f"&maxdepth=1000&minlat={zona.minlat}&maxlat={zona.maxlat}"
        f"&minlon={zona.minlon}&maxlon={zona.maxlon}"
        f"&minversion=100&orderby=time-asc&format=text&limit=100"
    )
    return filename
