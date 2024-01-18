'''
class auto: # osztály
    tipus = '' # jellemzők, attribútumok
    rendszam = ''
    szin = ''
    telejesitmeny = 0
'''

class auto:
    def __init__(self, tipus: str, rendszam: str, szin: str, teljesitmeny: float, gyorsulas: float = 0) -> None: 
    # metódus (az osztály saját függvényei)
    # példányosításkor fut le
    # self - hivatkozás a saját osztályre, minden metódus első paraméterre ez kell legyen
    # gyorsulas - alapértelmezett értéke: 0 -> nem kötelező megadni
        self.tipus = tipus
        self.rendszam = rendszam
        self.szin = szin
        self.teljesitmeny = teljesitmeny
        self.gyorsulas = gyorsulas