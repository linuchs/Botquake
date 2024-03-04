"""Helper module"""
from datetime import date, timedelta

def get_date_range(d_range):
    """ la funzione imposta i valori temporali dei dati da scaricare
    in un range che va dal giorno attuale indietro di un valore d_range"""
    date_range = [None] * 2
    today = date.today()
    today.strftime("%m/%d/%Y")
    days_inthe_past = today - timedelta(days=d_range)
    date_range[0] = days_inthe_past
    date_range[1] = today
    return date_range
    