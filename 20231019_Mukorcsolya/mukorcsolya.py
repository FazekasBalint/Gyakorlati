from random import randint

versenyzok_pontszama = [] 

def random_pontszam() -> float:
    """
    Visszaad egy random pontszámot 0 és 10 között, 0.25-ös lépésközzel
    """
    # return randint(0, 9) + randint(0, 4) / 4
    return randint(0, 40) / 4

def versenyzo_osszes_pontszama() -> list[float]:
    pontszamok = []
    for i in range(7):
        pontszamok.append(random_pontszam())
    return pontszamok

def legjobb_ponszam(pontszamok: list[float]) -> float:
    legnagyobb = pontszamok[0]
    for pont in pontszamok[1:]:
        if pont > legnagyobb:
            legnagyobb = pont
    return legnagyobb

def legrosszabb_pontszam(pontszamok: list[float]) -> float:
    legrosszabb = pontszamok[0]
    for pont in pontszamok[1:]:
        if pont < legrosszabb:
            legrosszabb = pont
    return legrosszabb

def atlag(pontszamok: list[float]) -> float:
    """
    A legrosszabb és a legjobb pontszám kiesik és a többinek az átlagát adja vissza.
    """
    osszeg = 0
    for pont in pontszamok:
        osszeg += pont
    osszeg -= legjobb_ponszam(pontszamok) - legrosszabb_pontszam(pontszamok)
    return osszeg / (len(pontszamok) - 2)

def gyoztes() -> int:
    """
    Visszaadja a győztes versenyző sorszámát.
    """
    gyoztes_indexe = 0
    for i in range(len(versenyzok_pontszama)):
        if versenyzok_pontszama[i] > versenyzok_pontszama[gyoztes_indexe]:
            gyoztes_indexe = i
    return gyoztes_indexe
