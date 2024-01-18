class hegycsucs:
    def __init__(self, sor:str) -> None:
        adatok = sor.split(';')
        self.nev = adatok[0]
        self.hegyseg = adatok[1]
        self.magassag = int(adatok[2])
        self.magassag_lab = self.magassag * 3.280839895