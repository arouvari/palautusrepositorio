from kps_pelaaja_vs_pelaaja import KPSPelaajaVsPelaaja
from kps_tekoaly import KPSTekoaly
from kps_parempi_tekoaly import KPSParempiTekoaly


def luo_peli(tyyppi):
    if tyyppi == "a":
        return KPSPelaajaVsPelaaja()
    elif tyyppi == "b":
        return KPSTekoaly()
    elif tyyppi == "c":
        return KPSParempiTekoaly()
    return None

def main():
    while True:
        print("Valitse pelimuoto:")
        print("(a) Ihminen vs. Ihminen")
        print("(b) Ihminen vs. Tekoäly")
        print("(c) Ihminen vs. Parempi Tekoäly")
        print("Muilla valinnoilla lopetetaan.")

        valinta = input("Valintasi: ")
        peli = luo_peli(valinta)

        if not peli:
            break

        peli.pelaa()


if __name__ == "__main__":
    main()
