class CBadás:
    def __init__(self, sor:str) -> None:
        adatok = sor.split(';')
        self.Ora = int(adatok[0])
        self.Perc = int(adatok[1])
        self.AdasDb = int(adatok[2])
        self.Nev = adatok[3]