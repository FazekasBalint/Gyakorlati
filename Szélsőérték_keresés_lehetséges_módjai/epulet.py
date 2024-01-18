class Epulet:
    def __init__(self, sor) -> None:
        adatok = sor.split(';')
        self.név = adatok[0]
        self.város = adatok[1]
        self.ország = adatok[2]
        self.magasság = float(adatok[3].replace(',', '.'))
        self.emelet = int(adatok[4])
        self.épült = int(adatok[5])