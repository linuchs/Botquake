
class ZoneMap: # pylint: disable=too-few-public-methods
    """ Imposto una porzione del globo terrestre dalla quale estrapolare i dati"""
    def __init__(self, zona=None):
        if zona is None:
            # I dati valori ristretti alle coordinate sotto sono impostati sull'area etnea
            self.minlat = 37
            self.maxlat = 38
            self.minlon = 14.5
            self.maxlon = 15.5
