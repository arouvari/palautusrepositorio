import unittest
from unittest.mock import Mock, ANY
from kauppa import Kauppa
from viitegeneraattori import Viitegeneraattori
from varasto import Varasto
from tuote import Tuote
from ostoskori import Ostoskori
from tuote import Tuote

class TestKauppa(unittest.TestCase):
    def test_ostoksen_paaytyttya_pankin_metodia_tilisiirto_kutsutaan(self):
        pankki_mock = Mock()
        viitegeneraattori_mock = Mock()

        # palautetaan aina arvo 42
        viitegeneraattori_mock.uusi.return_value = 42

        varasto_mock = Mock()

        # tehdään toteutus saldo-metodille
        def varasto_saldo(tuote_id):
            if tuote_id == 1:
                return 10

        # tehdään toteutus hae_tuote-metodille
        def varasto_hae_tuote(tuote_id):
            if tuote_id == 1:
                return Tuote(1, "maito", 5)

        # otetaan toteutukset käyttöön
        varasto_mock.saldo.side_effect = varasto_saldo
        varasto_mock.hae_tuote.side_effect = varasto_hae_tuote

        # alustetaan kauppa
        kauppa = Kauppa(varasto_mock, pankki_mock, viitegeneraattori_mock)

        # tehdään ostokset
        kauppa.aloita_asiointi()
        kauppa.lisaa_koriin(1)
        kauppa.tilimaksu("pekka", "12345")

        # varmistetaan, että metodia tilisiirto on kutsuttu
        pankki_mock.tilisiirto.assert_called()
        # toistaiseksi ei välitetä kutsuun liittyvistä argumenteista
   
    def test_ostoksen_paaytyttya_pankin_tilisiirtoa_kutsutaan_oikeilla_arvoilla(self):
        pankki_mock = Mock()
        viitegeneraattori_mock = Mock()

        viitegeneraattori_mock.uusi.return_value = 42

        varasto_mock = Mock()
    
        def varasto_saldo(tuote_id):
            if tuote_id == 1:
                return 10

        def varasto_hae_tuote(tuote_id):
            if tuote_id == 1:
                return Tuote(1, "maito", 5)

        varasto_mock.saldo.side_effect = varasto_saldo
        varasto_mock.hae_tuote.side_effect = varasto_hae_tuote

        kauppa = Kauppa(varasto_mock, pankki_mock, viitegeneraattori_mock)

        kauppa.aloita_asiointi()
        kauppa.lisaa_koriin(1)
        kauppa.tilimaksu("pekka", "12345")

        pankki_mock.tilisiirto.assert_called_with("pekka", 42, "12345", "33333-44455", 5)
    
    def test_kahden_ostoksen_paaytyttya_pankin_tilisiirtoa_kutsutaan_oikeilla_arvoilla(self):
        pankki_mock = Mock()
        viitegeneraattori_mock = Mock()

        viitegeneraattori_mock.uusi.return_value = 42

        varasto_mock = Mock()
    
        def varasto_saldo1(tuote_id):
            if tuote_id == 1:
                return 10
        
        def varasto_saldo2(tuote_id):
            if tuote_id == 2:
                return 5

        def varasto_hae_tuote1(tuote_id):
            if tuote_id == 1:
                return Tuote(1, "maito", 5)
        
        def varasto_hae_tuote2(tuote_id):
            if tuote_id == 2:
                return Tuote(2, "voi", 3)

        varasto_mock.saldo.side_effect = varasto_saldo1
        varasto_mock.hae_tuote.side_effect = varasto_hae_tuote1

        kauppa = Kauppa(varasto_mock, pankki_mock, viitegeneraattori_mock)

        kauppa.aloita_asiointi()
        kauppa.lisaa_koriin(1)
        varasto_mock.saldo.side_effect = varasto_saldo2
        varasto_mock.hae_tuote.side_effect = varasto_hae_tuote2
        kauppa.lisaa_koriin(2)
        kauppa.tilimaksu("pekka", "12345")

        pankki_mock.tilisiirto.assert_called_with("pekka", 42, "12345", "33333-44455", 8)
    
    def test_kahden_ostoksen_paaytyttya_pankin_tilisiirtoa_kutsutaan_oikeilla_arvoilla(self):
        pankki_mock = Mock()
        viitegeneraattori_mock = Mock()

        viitegeneraattori_mock.uusi.return_value = 42

        varasto_mock = Mock()
    
        def varasto_saldo(tuote_id):
            if tuote_id == 1:
                return 10
            if tuote_id == 2:
                return 5

        def varasto_hae_tuote(tuote_id):
            if tuote_id == 1:
                return Tuote(1, "maito", 5)
            if tuote_id == 2:
                return Tuote(2, "voi", 3)
    

        varasto_mock.saldo.side_effect = varasto_saldo
        varasto_mock.hae_tuote.side_effect = varasto_hae_tuote

        kauppa = Kauppa(varasto_mock, pankki_mock, viitegeneraattori_mock)

        kauppa.aloita_asiointi()
        kauppa.lisaa_koriin(1)
        kauppa.lisaa_koriin(2)
        kauppa.tilimaksu("pekka", "12345")

        pankki_mock.tilisiirto.assert_called_with("pekka", 42, "12345", "33333-44455", 8)

    def test_kahden_saman_tuotteen_paaytyttya_pankin_tilisiirtoa_kutsutaan_oikeilla_arvoilla(self):
        pankki_mock = Mock()
        viitegeneraattori_mock = Mock()

        viitegeneraattori_mock.uusi.return_value = 42

        varasto_mock = Mock()
    
        def varasto_saldo(tuote_id):
            if tuote_id == 1:
                return 10

        def varasto_hae_tuote(tuote_id):
            if tuote_id == 1:
                return Tuote(1, "maito", 5)
        
        varasto_mock.saldo.side_effect = varasto_saldo
        varasto_mock.hae_tuote.side_effect = varasto_hae_tuote

        kauppa = Kauppa(varasto_mock, pankki_mock, viitegeneraattori_mock)

        kauppa.aloita_asiointi()
        kauppa.lisaa_koriin(1)
        kauppa.lisaa_koriin(1)
        kauppa.tilimaksu("pekka", "12345")

        pankki_mock.tilisiirto.assert_called_with("pekka", 42, "12345", "33333-44455", 10)



    def test_yhden_ostoksen_ja_hylatyn_paaytyttya_pankin_tilisiirtoa_kutsutaan_oikeilla_arvoilla(self):
        pankki_mock = Mock()
        viitegeneraattori_mock = Mock()

        viitegeneraattori_mock.uusi.return_value = 42

        varasto_mock = Mock()
    
        def varasto_saldo(tuote_id):
            if tuote_id == 1:
                return 10
            if tuote_id == 2:
                return 0

        def varasto_hae_tuote(tuote_id):
            if tuote_id == 1:
                return Tuote(1, "maito", 5)
            if tuote_id == 2:
                return Tuote(2, "voi", 3)
    

        varasto_mock.saldo.side_effect = varasto_saldo
        varasto_mock.hae_tuote.side_effect = varasto_hae_tuote

        kauppa = Kauppa(varasto_mock, pankki_mock, viitegeneraattori_mock)

        kauppa.aloita_asiointi()
        kauppa.lisaa_koriin(1)
        kauppa.lisaa_koriin(2)
        kauppa.tilimaksu("pekka", "12345")

        pankki_mock.tilisiirto.assert_called_with("pekka", 42, "12345", "33333-44455", 5)
    
    def test_aloita_asiointi_nollaa_ostoskorin(self):
        pankki_mock = Mock()
        viitegeneraattori_mock = Mock()

        viitegeneraattori_mock.uusi.return_value = 42

        varasto_mock = Mock()
    
        def varasto_saldo(tuote_id):
            if tuote_id == 1:
                return 10

        def varasto_hae_tuote(tuote_id):
            if tuote_id == 1:
                return Tuote(1, "maito", 5)
    
    

        varasto_mock.saldo.side_effect = varasto_saldo
        varasto_mock.hae_tuote.side_effect = varasto_hae_tuote

        kauppa = Kauppa(varasto_mock, pankki_mock, viitegeneraattori_mock)

        kauppa.aloita_asiointi()
        kauppa.lisaa_koriin(1)
        kauppa.aloita_asiointi()
        kauppa.lisaa_koriin(1)
        kauppa.tilimaksu("pekka", "12345")

        pankki_mock.tilisiirto.assert_called_with("pekka", 42, "12345", "33333-44455", 5)
    

    def test_uusi_viitenumero_jokaiseen_maksuun(self):
        pankki_mock = Mock()
        viitegeneraattori_mock = Mock()
        viitegeneraattori_mock.uusi.side_effect = [1, 2, 3]

        varasto_mock = Mock()
    
        def varasto_saldo(tuote_id):
            if tuote_id == 1:
                return 10

        def varasto_hae_tuote(tuote_id):
            if tuote_id == 1:
                return Tuote(1, "maito", 5)

        varasto_mock.saldo.side_effect = varasto_saldo
        varasto_mock.hae_tuote.side_effect = varasto_hae_tuote

        kauppa = Kauppa(varasto_mock, pankki_mock, viitegeneraattori_mock)

        kauppa.aloita_asiointi()
        kauppa.lisaa_koriin(1)
        kauppa.tilimaksu("pekka", "12345")
        pankki_mock.tilisiirto.assert_called_with("pekka", 1, "12345", "33333-44455", 5)
        kauppa.aloita_asiointi()
        kauppa.lisaa_koriin(1)
        kauppa.tilimaksu("markku", "123456")
        pankki_mock.tilisiirto.assert_called_with("markku", 2, "123456", "33333-44455", 5)
        kauppa.aloita_asiointi()
        kauppa.lisaa_koriin(1)
        kauppa.tilimaksu("matti", "1234567")
        pankki_mock.tilisiirto.assert_called_with("matti", 3, "1234567", "33333-44455", 5)

        self.assertEqual(viitegeneraattori_mock.uusi.call_count, 3)


    def test_lisaa_koriin_ei_toimi_kun_tuotetta_ei_ole_varastossa(self):
        pankki_mock = Mock()
        viitegeneraattori_mock = Mock()

        viitegeneraattori_mock.uusi.return_value = 42

        varasto_mock = Mock()

        def varasto_saldo(tuote_id):
            if tuote_id == 1:
                return 0

        def varasto_hae_tuote(tuote_id):
            if tuote_id == 1:
                return Tuote(1, "maito", 5)

        varasto_mock.saldo.side_effect = varasto_saldo
        varasto_mock.hae_tuote.side_effect = varasto_hae_tuote

        kauppa = Kauppa(varasto_mock, pankki_mock, viitegeneraattori_mock)

        kauppa.aloita_asiointi()
        kauppa.lisaa_koriin(1)
        
        self.assertEqual(kauppa._ostoskori.hinta(), 0)
        varasto_mock.ota_varastosta.assert_not_called()

    def test_tilimaksu_ei_tapaa_maksua_ilman_ostoksia(self):
        pankki_mock = Mock()
        viitegeneraattori_mock = Mock()

        viitegeneraattori_mock.uusi.return_value = 42

        varasto_mock = Mock()

        kauppa = Kauppa(varasto_mock, pankki_mock, viitegeneraattori_mock)

        kauppa.aloita_asiointi()
        kauppa.tilimaksu("pekka", "12345")

        pankki_mock.tilisiirto.assert_not_called()

    def test_ostokset_ja_koriin_lisaaminen_kun_asiointi_on_nollattu(self):
        pankki_mock = Mock()
        viitegeneraattori_mock = Mock()

        viitegeneraattori_mock.uusi.return_value = 42

        varasto_mock = Mock()

        def varasto_saldo(tuote_id):
            if tuote_id == 1:
                return 10

        def varasto_hae_tuote(tuote_id):
            if tuote_id == 1:
                return Tuote(1, "maito", 5)

        varasto_mock.saldo.side_effect = varasto_saldo
        varasto_mock.hae_tuote.side_effect = varasto_hae_tuote

        kauppa = Kauppa(varasto_mock, pankki_mock, viitegeneraattori_mock)

        kauppa.aloita_asiointi()
        kauppa.lisaa_koriin(1)
        kauppa.aloita_asiointi()
        kauppa.lisaa_koriin(1)
        kauppa.tilimaksu("pekka", "12345")

        pankki_mock.tilisiirto.assert_called_with("pekka", 42, "12345", "33333-44455", 5)
    
    def test_uusi_viitenumero_jokaiseen_maksuun(self):
        pankki_mock = Mock()
        viitegeneraattori_mock = Mock()
        viitegeneraattori_mock.uusi.side_effect = [1, 2, 3]

        varasto_mock = Mock()

        def varasto_saldo(tuote_id):
            if tuote_id == 1:
                return 10

        def varasto_hae_tuote(tuote_id):
            if tuote_id == 1:
                return Tuote(1, "maito", 5)

        varasto_mock.saldo.side_effect = varasto_saldo
        varasto_mock.hae_tuote.side_effect = varasto_hae_tuote

        kauppa = Kauppa(varasto_mock, pankki_mock, viitegeneraattori_mock)

        kauppa.aloita_asiointi()
        kauppa.lisaa_koriin(1)
        kauppa.tilimaksu("pekka", "12345")
        pankki_mock.tilisiirto.assert_called_with("pekka", 1, "12345", "33333-44455", 5)
        kauppa.aloita_asiointi()
        kauppa.lisaa_koriin(1)
        kauppa.tilimaksu("markku", "123456")
        pankki_mock.tilisiirto.assert_called_with("markku", 2, "123456", "33333-44455", 5)
        kauppa.aloita_asiointi()
        kauppa.lisaa_koriin(1)
        kauppa.tilimaksu("matti", "1234567")
        pankki_mock.tilisiirto.assert_called_with("matti", 3, "1234567", "33333-44455", 5)

        self.assertEqual(viitegeneraattori_mock.uusi.call_count, 3)
    
    def test_lisaa_koriin_ei_riittavaa_saldoa(self):
        pankki_mock = Mock()
        viitegeneraattori_mock = Mock()
        viitegeneraattori_mock.uusi.return_value = 42

        varasto_mock = Mock()

        def varasto_saldo(tuote_id):
            return 0

        def varasto_hae_tuote(tuote_id):
            return Tuote(1, "maito", 5)

        varasto_mock.saldo.side_effect = varasto_saldo
        varasto_mock.hae_tuote.side_effect = varasto_hae_tuote

        kauppa = Kauppa(varasto_mock, pankki_mock, viitegeneraattori_mock)
        kauppa.aloita_asiointi()
        kauppa.lisaa_koriin(1)
    
        self.assertEqual(len(kauppa._ostoskori._tuotteet), 0)

    def test_tilimaksu_ei_tapaa_maksua_ilman_ostoksia(self):
        pankki_mock = Mock()
        viitegeneraattori_mock = Mock()
        viitegeneraattori_mock.uusi.return_value = 42

        varasto_mock = Mock()
    
        varasto_mock.saldo.side_effect = lambda x: 0 
        varasto_mock.hae_tuote.side_effect = lambda x: Tuote(1, "maito", 5)

        kauppa = Kauppa(varasto_mock, pankki_mock, viitegeneraattori_mock)
        kauppa.aloita_asiointi()
        kauppa.tilimaksu("pekka", "12345")
    
    
        pankki_mock.tilisiirto.assert_not_called()
    def test_poista_korista(self):
        pankki_mock = Mock()
        viitegeneraattori_mock = Mock()
        viitegeneraattori_mock.uusi.return_value = 42

        varasto_mock = Mock()
    
        def varasto_saldo(tuote_id):
            if tuote_id == 1:
                return 10

        def varasto_hae_tuote(tuote_id):
            return Tuote(1, "maito", 5)

        varasto_mock.saldo.side_effect = varasto_saldo
        varasto_mock.hae_tuote.side_effect = varasto_hae_tuote

        kauppa = Kauppa(varasto_mock, pankki_mock, viitegeneraattori_mock)
        kauppa.aloita_asiointi()
        kauppa.lisaa_koriin(1)

        self.assertEqual(len(kauppa._ostoskori._tuotteet), 1)
        kauppa.poista_korista(1)
        self.assertEqual(len(kauppa._ostoskori._tuotteet), 0)
        varasto_mock.palauta_varastoon.assert_called_with(Tuote(1, "maito", 5))



class TestOstoskori(unittest.TestCase):

    def test_lisaa_tuote_koriin(self):
        ostoskori = Ostoskori()
        tuote = Tuote(1, "maito", 5)
        ostoskori.lisaa(tuote)

        self.assertEqual(len(ostoskori._tuotteet), 1)
        self.assertEqual(ostoskori._tuotteet[0], tuote)

    def test_poista_tuote_korista(self):
        ostoskori = Ostoskori()
        tuote1 = Tuote(1, "maito", 5)
        tuote2 = Tuote(2, "voi", 3)
        ostoskori.lisaa(tuote1)
        ostoskori.lisaa(tuote2)
        ostoskori.poista(tuote1)

        self.assertEqual(len(ostoskori._tuotteet), 1)
        self.assertEqual(ostoskori._tuotteet[0], tuote2)

    def test_poista_tuote_jota_ei_ole_korissa(self):
        ostoskori = Ostoskori()
        tuote1 = Tuote(1, "maito", 5)
        tuote2 = Tuote(2, "voi", 3)

        ostoskori.lisaa(tuote1)

        ostoskori.poista(tuote2)

        self.assertEqual(len(ostoskori._tuotteet), 1)
        self.assertEqual(ostoskori._tuotteet[0], tuote1)

    def test_hinta_lasketaan_oikein(self):
        ostoskori = Ostoskori()
        tuote1 = Tuote(1, "maito", 5)
        tuote2 = Tuote(2, "voi", 3)

        ostoskori.lisaa(tuote1)
        ostoskori.lisaa(tuote2)

        self.assertEqual(ostoskori.hinta(), 8)

    def test_hinta_kun_kori_on_tyhja(self):
        ostoskori = Ostoskori()

        self.assertEqual(ostoskori.hinta(), 0)

class TestTuote(unittest.TestCase):

    def test_str_tuote(self):
        tuote = Tuote(1, "maito", 5)
        
        self.assertEqual(str(tuote), "maito")

    def test_tuote_comparison(self):
        tuote1 = Tuote(1, "maito", 5)
        tuote2 = Tuote(2, "voi", 3)
        tuote3 = Tuote(1, "maito", 5)
        
        self.assertTrue(tuote1 == tuote3)
        self.assertFalse(tuote1 == tuote2)

    def test_tuote_hash(self):
        tuote1 = Tuote(1, "maito", 5)
        tuote2 = Tuote(2, "voi", 3)
        
        self.assertEqual(hash(tuote1), hash(Tuote(1, "maito", 5)))
        self.assertNotEqual(hash(tuote1), hash(tuote2))



