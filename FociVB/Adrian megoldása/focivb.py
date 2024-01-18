class FociVb:
    def __init__(self, sor: str) -> None:
        adatok = sor.split(';')
        self.Csapat = adatok[0]
        self.Részvételek_száma = int(adatok[1])
        self.Első_részvétel = int(adatok[2])
        self.Legutóbbi_részvétel = adatok[3]
        self.Legjobb_eredmény = adatok[4]