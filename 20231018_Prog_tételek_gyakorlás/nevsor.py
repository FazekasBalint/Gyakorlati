nevek = ['Péter Gáspár', 'Miléna Deák', 'Tamás Pető', 'József Fehér', 'Tamara Szarvas', 'Gellért Novák', 'Fábián Csizmadia', 'Adrián Jankovics', 'Kitti Rózsa', 'Jakab Markó', 'Mara Kocsis', 'Franciska Bálint', 'Juliska Tolvaj', 'Teodóra Jakab', 'Ágota Katona', 'Jolánka Jakab', 'Péter Borbély', 'Hajni Oláh', 'Zoltán Gabor', 'Laci Benes']

def osztalyletszam() -> int:
    """
    Visszadja a nevek lista hosszát.
    """
    return len(nevek)

def leghosszabb_nev() -> str:
    """
    Visszaadja a leghosszabb nevű embert a nevek listából.
    """
    # Maximim kiválasztás
    leghosszabb = nevek[0]
    for nev in nevek[1:]:
        if len(nev) > len(leghosszabb):
            leghosszabb = nev
    return leghosszabb

def atlag_hossz() -> float:
    """
    Visszaadja a nevek átlagos hosszát.
    """
    osszeg = 0
    for nev in nevek:
        osszeg += len(nev)
    return osszeg / osztalyletszam()

def van_e(keresett_nev: str) -> bool:
    """
    Eldönti, hogy a keresett_nev benne van-e a nevsorban.
    """
    for nev in nevek:
        if keresett_nev.upper() in nev.upper():
            return True
    return False

def tanulo_szamol(keresett_nev: str) -> int:
    """
    Megszámolja hogy keresett_nev nevű tanuló hány van a nevek listában.
    """
    darab = 0
    for nev in nevek:
        if keresett_nev.upper() in nev.upper():
            darab += 1
    return darab

def keres(keresett_nev: str) -> int|bool:
    """
    A keresett_nev nevű tanuló sorszámát adja vissza. Ha nincs ilyen nevű tanuló, akkor False-t.
    """
    for i in range(osztalyletszam()):
        if keresett_nev.lower() in nevek[i].lower():
            return i
    return False