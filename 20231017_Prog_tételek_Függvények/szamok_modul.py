from random import randint

szamok = []

def feltolt(n: int, min: int, max: int) -> None:
    """
    Feltölti a számok listát n darab min és max közé eső számmal.
    """
    for i in range(n):
        szamok.append(randint(min, max))

def van_e_oszthato(oszto: int) -> bool:
    """
    Eldönti, hogy van-e olyan szám a szamok listában amely maradék nélkül osztható az oszto-val.
    """
    for szam in szamok:
        if szam % oszto == 0:
            return True
    return False

def atlag() -> float:
    """
    A számok listában szereplő számok átlagát adja vissza.
    """
    osszeg = 0
    for szam in szamok:
        osszeg += szam
    return osszeg / len(szamok)

def keres(mit: int) -> int|bool:
    """
    Megkeresi a mit paraméterben megadott számot a szamok listában.
    Visszaadja a keresett szám indexét, illetve Flase-t ha nincs benne.
    """
    for i in range(len(szamok)):
        if mit == szamok[i]:
            return i
    return False

def darab_ha_tobb(limit: int) -> int:
    """
    Megszámolja, hogy hány olyan elem van a listában amely a megadott limitnél nagyobb vagy egyenlő.
    """
    darab = 0
    for szam in szamok:
        if szam >= limit:
            darab += 1
    return darab