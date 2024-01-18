from datetime import datetime

class tanulo:
    def __init__(self, vezeteknev: str, keresztnev: str, szuletes: datetime, jegyek: list[int]) -> None:
        self.vezeteknev = vezeteknev
        self.keresztnev = keresztnev
        # self.szueltesi_datum = datetime.strptime(szuletes,"%Y.%m.%d")
        self.szuletes = szuletes
        self.jegyek = jegyek
    
    def jegy_beir(self, jegy: int) -> None:
        self.jegyek.append(jegy)

    def atlag(self) -> float:
        if len(self.jegyek) == 0:
            return 0

        osszeg = 0
        for jegy in self.jegyek:
            osszeg += jegy
        return osszeg / len(self.jegyek)