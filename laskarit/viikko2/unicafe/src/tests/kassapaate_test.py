import unittest
from kassapaate import Kassapaate
from maksukortti import Maksukortti

class TestKassapaate(unittest.TestCase):
    def setUp(self):
        self.kassapaate=Kassapaate()

    def test_oikea_maara(self):
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
        self.assertEqual(self.kassapaate.edulliset, 0)
        self.assertEqual(self.kassapaate.maukkaat, 0)
    
    def test_kateisosto_edullinen_onnistuu(self):
        self.assertEqual(self.kassapaate.syo_edullisesti_kateisella(240), 0)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100240)
        self.assertEqual(self.kassapaate.edulliset, 1)

    def test_kateisosto_edullinen_ei_onnistu(self):
        self.assertEqual(self.kassapaate.syo_edullisesti_kateisella(100), 100)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
        self.assertEqual(self.kassapaate.edulliset, 0)
    
    def test_kateisosto_maukas_onnistuu(self):
        self.assertEqual(self.kassapaate.syo_maukkaasti_kateisella(400), 0)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100400)
        self.assertEqual(self.kassapaate.maukkaat, 1)

    def test_kateisosto_maukas_ei_onnistu(self):
        self.assertEqual(self.kassapaate.syo_maukkaasti_kateisella(300), 300)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
        self.assertEqual(self.kassapaate.maukkaat, 0)

    def test_syo_edullisesti_kortilla_toimii(self):
        kortti=Maksukortti(240)
        self.assertEqual(self.kassapaate.syo_edullisesti_kortilla(kortti), True)
        self.assertEqual(kortti.saldo, 0)
        self.assertEqual(self.kassapaate.edulliset, 1)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_syo_edullisesti_kortilla_ei_toimi(self):
        kortti=Maksukortti(100)
        self.assertEqual(self.kassapaate.syo_edullisesti_kortilla(kortti), False)
        self.assertEqual(kortti.saldo, 100)
        self.assertEqual(self.kassapaate.edulliset, 0)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_syo_maukkaasti_kortilla_toimii(self):
        kortti=Maksukortti(400)
        self.assertEqual(self.kassapaate.syo_maukkaasti_kortilla(kortti), True)
        self.assertEqual(kortti.saldo, 0)
        self.assertEqual(self.kassapaate.maukkaat, 1)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_syo_maukkaasti_kortilla_ei_toimi(self):
        kortti=Maksukortti(100)
        self.assertEqual(self.kassapaate.syo_maukkaasti_kortilla(kortti), False)
        self.assertEqual(kortti.saldo, 100)
        self.assertEqual(self.kassapaate.maukkaat, 0)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_lataa_rahaa_kortille_onnistuu(self):
        kortti=Maksukortti(0)
        self.kassapaate.lataa_rahaa_kortille(kortti,100)
        self.assertEqual(kortti.saldo, 100)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100100)

    def test_lataa_rahaa_kortille_ei_onnistu(self):
        kortti=Maksukortti(0)
        self.kassapaate.lataa_rahaa_kortille(kortti,-1)
        self.assertEqual(kortti.saldo, 0)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)