def ido_masodpercben(ido: str) -> float:
    """
    A paraméterben stringként megadott időt átváltja másodpercre.
    """
    idok = ido.split(':')
    return int(idok[0]) * 60 + int(idok[1]) + int(idok[2]) / 1000

def versenyzok_szama(koridok: list) -> int:
    """
    Visszaadja, hogy hágy elem van a listában (a versenyzők száma).
    """
    return len(koridok)

def koridok_masodpercben(koridok: list[str]) -> list[float]:
    """
    A köridőket sztringből floattá konvertálja.
    """
    koridok_mp = []
    for korido in koridok:
        koridok_mp.append(ido_masodpercben(korido))
    return koridok_mp

def leggyorsabb_rajtszama(koridok: list[float]) -> int:
    """
    Visszadja a leggyorsabb versenyző rajtszámát.
    """
    leggyorsabb_indexe = 0
    for i in range(len(koridok)):
        if koridok[i] < koridok[leggyorsabb_indexe]:
            leggyorsabb_indexe = i
    return leggyorsabb_indexe

def atlagos_korido(koridok: list[float]) -> float:
    osszeg = 0
    for korido in koridok:
        osszeg += korido
    return osszeg / len(koridok)

def lassabb_mint_atlag(koridok: list[float]) -> int:
    """
    Megszámolja hány olyan versenyző van, aki lasabb az átlagnál.
    """
    atlag = atlagos_korido(koridok)
    darab = 0
    for korido in koridok:
        if korido > atlag:
            darab += 1
    return darab