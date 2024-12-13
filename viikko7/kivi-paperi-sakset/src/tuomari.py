class Tuomari:
    def __init__(self):
        self.ekan_pisteet = 0
        self.tokan_pisteet = 0
        self.tasapelit = 0

    def kirjaa_siirto(self, ekan_siirto, tokan_siirto):
        if ekan_siirto == tokan_siirto:
            self.tasapelit += 1
        elif (ekan_siirto == "k" and tokan_siirto == "s") or \
             (ekan_siirto == "s" and tokan_siirto == "p") or \
             (ekan_siirto == "p" and tokan_siirto == "k"):
            self.ekan_pisteet += 1
        else:
            self.tokan_pisteet += 1

    def __str__(self):
        return f"Tilanne: {self.ekan_pisteet}-{self.tokan_pisteet}, tasapelit: {self.tasapelit}"