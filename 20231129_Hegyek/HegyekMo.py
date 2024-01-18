from hegycsucs import hegycsucs

hegyek : list[hegycsucs] = []

def beolvas(filename):
    file = open(filename, 'r', encoding='utf8')
    file.readline()
    for sor in file:
        hegyek.append(hegycsucs(sor.strip()))
    file.close()

def hegyek_szama():
    return len(hegyek)

def atlag_magassag():
    osszeg = 0
    for h in hegyek:
        osszeg += h.magassag
    return osszeg / hegyek_szama()

def legmagasabb_hegy() -> hegycsucs:
    legmagasabb = hegyek[0]
    for h in hegyek[1:]:
        if h.magassag > legmagasabb.magassag:
            legmagasabb = h
    return legmagasabb

def van_magasabb(magassag) -> bool:
    for h in hegyek:
        if h.magassag > magassag:
            return True
    return False

def darab_magasabb_mint(magassag_lab) -> int:
    darab = 0
    for h in hegyek:
        if h.magassag_lab > magassag_lab:
            darab += 1
    return darab

def hegy_statisztika() -> dict[str, int]:
    stat : dict[str, int] = {}
    for h in hegyek:
        if h.hegyseg in stat.keys():
            stat[h.hegyseg] += 1
        else:
            stat[h.hegyseg] = 1
    return stat

def mentes(hegyseg, filename):
    file = open(filename, 'w', encoding='utf8')
    for h in hegyek:
        if h.hegyseg == hegyseg:
            file.write(f'{h.nev};{h.magassag_lab:.1f}\n')
    file.close()