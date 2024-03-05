#CHIEDERE SE IL CODICE DI TESTINNG DOBBIAMO RIULASCIARLO NELLA REPOSITORY DEL PROGETTO
from utils.helper.gethelp import get_date_range
from datetime import date, timedelta
import pytest 

#testo la funzione get_date_range
def test_get_date_range() -> None:
    #get date range deve tornare un array dobe il primo è data-timedelta il secondo è il giorno di oggi 
    result = get_date_range(2)
    assert result[0] == date.today()-timedelta(days=2)
    assert result[1] == date.today() 