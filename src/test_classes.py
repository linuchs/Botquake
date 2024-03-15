"""Effettua il test della classe ZoneMap"""
from utils.helper.classes import ZoneMap


def test_get_coordinates():
    """Effettua il test sul metodo get_coordinates"""
    zone = ZoneMap()
    coordinates = zone.get_coordinates()
    assert coordinates.minlat == 37
    assert coordinates.maxlat == 38
    assert coordinates.minlon == 14.5
    assert coordinates.maxlon == 15.5
