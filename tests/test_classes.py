from src.utils.helper.classes import ZoneMap

def test_get_coordinates():
    zone = ZoneMap()
    coordinates = zone.get_coordinates()
    assert coordinates.minlat == 37
    assert coordinates.maxlat == 38
    assert coordinates.minlon == 14.5
    assert coordinates.maxlon == 15.5