from tuomari import Tuomari
from tekoaly_parannettu import TekoalyParannettu
from kps import KiviPaperiSakset


class KPSParempiTekoaly(KiviPaperiSakset):
    def __init__(self):
        super().__init__()
        self.historia = []

    def _toisen_siirto(self, ensimmaisen_siirto):
        if ensimmaisen_siirto:
            self.historia.append(ensimmaisen_siirto)

        if not self.historia:
            valinta = "k"
        else:
            valinta = max(set(self.historia), key=self.historia.count)

        print(f"Parempi tekoäly valitsi: {valinta}")
        return valinta
