import unittest
from varasto import Varasto
from tuote import Tuote
from kirjanpito import kirjanpito as default_kirjanpito

class TestVarasto(unittest.TestCase):
    def setUp(self):
        self.varasto = Varasto()

    def test_hae_tuote_palauttaa_oikean_tuotteen(self):
        tuote = self.varasto.hae_tuote(1)
        self.assertEqual(tuote.nimi, "Koff Portteri")
        self.assertEqual(tuote.hinta, 3)

    def test_hae_tuote_palauttaa_none_jos_tuotetta_ei_ole(self):
        tuote = self.varasto.hae_tuote(999)
        self.assertIsNone(tuote)

    def test_saldo_palauttaa_oikean_arvon(self):
        saldo = self.varasto.saldo(1)
        self.assertEqual(saldo, 100)

    def test_saldo_palauttaa_none_jos_tuotetta_ei_ole(self):
        saldo = self.varasto.saldo(999)
        self.assertIsNone(saldo)

    def test_ota_varastosta_vahentaa_saldoa(self):
        tuote = self.varasto.hae_tuote(1)
        self.varasto.ota_varastosta(tuote)
        uusi_saldo = self.varasto.saldo(1)
        self.assertEqual(uusi_saldo, 99)

    def test_ota_varastosta_kirjaa_tapahtuman(self):
        tuote = self.varasto.hae_tuote(1)
        self.varasto.ota_varastosta(tuote)
        tapahtumat = default_kirjanpito.tapahtumat
        self.assertIn(f"otettiin varastosta {tuote}", tapahtumat)

    def test_palauta_varastoon_kasvattaa_saldoa(self):
        tuote = self.varasto.hae_tuote(1)
        self.varasto.palauta_varastoon(tuote)
        uusi_saldo = self.varasto.saldo(1)
        self.assertEqual(uusi_saldo, 101)

    def test_palauta_varastoon_kirjaa_tapahtuman(self):
        tuote = self.varasto.hae_tuote(1)
        self.varasto.palauta_varastoon(tuote)
        tapahtumat = default_kirjanpito.tapahtumat
        self.assertIn(f"palautettiin varastoon {tuote}", tapahtumat)

    def test_ota_varastosta_ei_toimi_jos_saldo_on_nolla(self):
        uusi_tuote = Tuote(999, "Testituote", 1)
        self.varasto._saldot[uusi_tuote] = 0
        self.varasto.ota_varastosta(uusi_tuote)
        self.assertEqual(self.varasto.saldo(999), 0)

    def test_palauta_varastoon_toimii_uudelle_tuotteelle(self):
        uusi_tuote = Tuote(999, "Testituote", 1)
        self.varasto._saldot[uusi_tuote] = 0
        self.varasto.palauta_varastoon(uusi_tuote)
        self.assertEqual(self.varasto.saldo(999), 1)

if __name__ == "__main__":
    unittest.main()
