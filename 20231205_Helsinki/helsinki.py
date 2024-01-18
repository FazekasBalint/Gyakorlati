from helyezes import helyezes

helyezesek: list[helyezes] = []

def beolvas(fajlnev):
    fajl = open(fajlnev, 'r', encoding='utf8')
    for sor in fajl:
        helyezesek.append(helyezes(sor.strip()))
    fajl.close()

def pontszerzo_helyezesek_szama() -> int:
    return len(helyezesek)

def helyezesek_szama(hely) -> int:
    darab = 0
    for h in helyezesek:
        if h.helyezes == hely:
            darab += 1
    return darab

def olimpiai_pontok_osszege() -> int:
    osszeg = 0
    for h in helyezesek:
        osszeg += h.olimpiai_pont
    return osszeg

def ermek_szama(sportag: str) -> int:
    darab = 0
    for h in helyezesek:
        if h.helyezes <= 3 and h.sportag == sportag:
            darab += 1
    return darab

def mentes(fajlnev):
    fajl = open(fajlnev, 'w', encoding='utf8')

    for h in helyezesek:
        if h.sportag == 'kajakkenu':
            fajl.write(f'{h.helyezes} {h.sportolok_szama} {h.olimpiai_pont} kajak-kenu {h.versenyszam}\n')
        else:
            fajl.write(f'{h.helyezes} {h.sportolok_szama} {h.olimpiai_pont} {h.sportag} {h.versenyszam}\n')

    fajl.close()

def legtobb_sportolo() -> helyezes:
    legtobb = helyezesek[0]
    for h in helyezesek[1:]:
        if h.sportolok_szama > legtobb.sportolok_szama:
            legtobb = h
    return legtobb