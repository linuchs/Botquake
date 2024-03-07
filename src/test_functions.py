
from utils.helper.gethelp import get_date_range
from utils.helper.gethelp import generate_url
from datetime import date, timedelta
import pytest 
from pytest_mock import MockerFixture
from utils.helper.classes import ZoneMap

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



