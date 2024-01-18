from cbadas import CBadás

cbadasok : list[CBadás] = []

def beolvas(fajlnev: str) -> None:
    fajl = open(fajlnev, 'r', encoding='utf8')
    fajl.readline()
    for sor in fajl:
        cbadasok.append(CBadás(sor.strip()))
    fajl.close()

def bejegzesek_szama(nev: str) -> int:
    darab = 0
    for c in cbadasok:
        if c.Nev == nev:
            darab += 1
    return darab

def legtobb_adas() -> int:
    legtobb = cbadasok[0].AdasDb
    for c in cbadasok:
        if c.AdasDb > legtobb:
            legtobb = c.AdasDb
    return legtobb

def mentes(fajlnev: str) ->None:
    fajl = open(fajlnev, 'w', encoding='utf8')
    fajl.write('Kezdes;Nev;AdasDb\n')
    for c in cbadasok:
        perc = c.Ora * 60 + c.Perc
        fajl.write(f'{perc};{c.Nev};{c.AdasDb}\n')
    fajl.close()