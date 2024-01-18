nevek = ['BASTIEN Steven', 'dos SANTOS Felipe', 'DUBLER Cedric', 'ERM Johannes', 'HELCELET Adam Sebastian', 'KAZMIREK Kai', 'LEPAGE Pierce', 'MAYER Kevin', 'MOLONEY Ashley', 'ROE Martin', 'SCANTLING Garrett', 'SHKURENYOV Ilya', 'SYKORA Jiri', 'TILGA Karel', 'UIBO Maicel', 'URENA Jorge', 'VICTOR Lindon', 'WARNER Damian', 'WIESIOLEK Pawel', 'ZHUK Vitaliy', 'ZIEMEK Zachery']
pontok = [8236, 7880, 7008, 8213, 8004, 8126, 8604, 8726, 8649, 7863, 8611, 8413, 7943, 7018, 8037, 8322, 8414, 9018, 8176, 8131, 8435]

def versenyzok_szama() -> int:
    return len(nevek)

def legalabb_darab(limit: int) -> int:
    """
    Visszadja, hogy hány olyan versenyző volt, aki legalább limit pontszámot ért el.
    """
    darab = 0
    for pont in pontok:
        if pont > limit:
            darab += 1
    return darab 

def atlag_pontszam() -> float:
    osszeg = 0
    for pont in pontok:
        osszeg += pont
    return osszeg / len(pontok)

def gyoztes_index() -> int:
    """
    Visszadja a győztes versenyző indexét.
    """
    legtobb_indexe = 0
    for i in range(len(pontok)):
        if pontok[i] > pontok[legtobb_indexe]:
            legtobb_indexe = i
    return legtobb_indexe

def gyoztes_index2() -> int:
    legtobb_indexe = 0
    legtobb_pont = pontok[0]
    for i, pont in enumerate(pontok):
        if pont > legtobb_pont:
            legtobb_pont = pont
            legtobb_indexe = i
    return legtobb_indexe

def gyoztes() -> tuple[str, int]:
    """
    Visszadja a győztes nevét és pontszámát
    """
    legtobb_indexe = 0
    legtobb_pont = pontok[0]
    for i, pont in enumerate(pontok):
        if pont > legtobb_pont:
            legtobb_pont = pont
            legtobb_indexe = i
    return nevek[legtobb_indexe], pontok[legtobb_indexe]

def versenyzo_keres(nev: str) -> int|bool:
    for index, egy_nev in enumerate(nevek):
        if egy_nev == nev:
            return index
    return False