"""Effettua il test delle classi"""
from utils.helper.classes import ZoneMap


def test_get_coordinates():
    """effettua il test del metodo get_coordinates della classe ZoneMap"""
    zone = ZoneMap()
    coordinates = zone.get_coordinates()
    assert coordinates.minlat == 37
    assert coordinates.maxlat == 38
    assert coordinates.minlon == 14.5
    assert coordinates.maxlon == 15.5
