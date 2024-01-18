class eredmeny:
    def __init__(self,sor:str) -> None:
        adatok=sor.split(";")
        self.nev=adatok[0]
        self.rajtszam=adatok[1]
        self.kategoria=adatok[2]
        self.versenyido=adatok[3]
        self.tavszazalek=int(adatok[4])

        ido_adatok=self.versenyido.split(":")
        self.oraban=int(ido_adatok[0])+int(ido_adatok[1])/60+int(ido_adatok[2])/3600