class helyezes:
    def __init__(self, sor:str) -> None:
        adatok = sor.split(' ')
        self.helyezes = int(adatok[0])
        self.sportolok_szama = int(adatok[1])
        self.sportag = adatok[2]
        self.versenyszam = adatok[3]

        match self.helyezes:
            case 1: pont = 7
            case 2: pont = 5
            case 3: pont = 4
            case 4: pont = 3
            case 5: pont = 2
            case 6: pont = 1

        self.olimpiai_pont = pont