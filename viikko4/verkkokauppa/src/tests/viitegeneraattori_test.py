import unittest
from viitegeneraattori import Viitegeneraattori

class TestViitegeneraattori(unittest.TestCase):

    def setUp(self):
        self.viitegeneraattori = Viitegeneraattori()

    def test_uusi_antaa_oikeat_viitenumerot(self):
        self.assertEqual(self.viitegeneraattori.uusi(), 2)
        self.assertEqual(self.viitegeneraattori.uusi(), 3)
        self.assertEqual(self.viitegeneraattori.uusi(), 4)

    def test_uusi_palauttaa_kasvavat_viitenumerot(self):
        first_viite = self.viitegeneraattori.uusi()
        second_viite = self.viitegeneraattori.uusi()
        third_viite = self.viitegeneraattori.uusi()
        self.assertGreater(second_viite, first_viite)
        self.assertGreater(third_viite, second_viite)

if __name__ == "__main__":
    unittest.main()
