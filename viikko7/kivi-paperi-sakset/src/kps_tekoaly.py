from tuomari import Tuomari
from tekoaly import Tekoaly
from kps import KiviPaperiSakset


class KPSTekoaly(KiviPaperiSakset):
    def __init__(self):
        super().__init__()
        self.tekoaly_siirto = 0

    def _toisen_siirto(self, ensimmaisen_siirto):
        siirrot = ["k", "p", "s"]
        valinta = siirrot[self.tekoaly_siirto]
        self.tekoaly_siirto = (self.tekoaly_siirto + 1) % 3
        print(f"Tietokone valitsi: {valinta}")
        return valinta
