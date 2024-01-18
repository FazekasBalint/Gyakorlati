class Versenyzo:
    def __init__(self, sor: str) -> None:
        # sor = 'Fábián;6.74;7.45;6.5;7.18;7.92;5.17'
        adatok = sor.split(';')
        # adatok = ['Fábián', '6.74', '7.45', '6.5', '7.18', '7.92', '5.17']
        self.nev = adatok[0]
        # self.ugras1 = 0
        # self.ugras2 = 0
        # self.ugras3 = 0
        # self.ugrasok = adatok[1:] # nem jó mert string típusúak az ugrások

        self.ugrasok = []
        for ugras in adatok[1:]:
            self.ugrasok.append(float(ugras))
