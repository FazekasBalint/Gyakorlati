from random import randint

szamok = []

def feltolt(n: int, min: int, max: int) -> None:
    """
    Feltölti a szamok listát n darab min és max közé eső egész számmal.
    """
    for i in range(n):
        szamok.append(randint(min, max))

def osszegzes() -> int:
    """
    A szamok listában lévő számok összegét adja vissza.
    """
    osszeg = 0
    for szam in szamok:
        osszeg += szam
    return osszeg