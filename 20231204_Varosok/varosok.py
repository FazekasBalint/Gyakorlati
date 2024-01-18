from Varos import Varos

varosok_listaja : list[Varos] = []

def beolvas(fajlnev: str):
    fajl = open(fajlnev, 'r', encoding='utf8')
    fajl.readline()
    for sor in fajl:
        varosok_listaja.append(Varos(sor.strip()))
    fajl.close()

def varosok_szama():
    return len(varosok_listaja)

def orszag_lakossaga(orszag: str) -> int:
    osszeg = 0
    for v in varosok_listaja:
        if v.orszag == orszag:
            osszeg += v.lakossag
    return osszeg

def legnagyobb_varos() -> Varos:
    legnagyobb = varosok_listaja[0]
    for v in varosok_listaja[1:]:
        if v.lakossag > legnagyobb.lakossag:
            legnagyobb = v
    return legnagyobb

def orszag_keres(orszag: str) -> bool:
    for v in varosok_listaja:
        if v.orszag == orszag:
            return True
    return False

def szokozos_varosok_szama(szokozok_szama: int) -> int:
    darab = 0
    for v in varosok_listaja:
        if v.szokozok_szama() == szokozok_szama:
            darab += 1
    return darab

def orszag_statisztika() -> dict[str, int]:
    stat : dict[str, int] = {}
    for v in varosok_listaja:
        if v.orszag in stat.keys():
            stat[v.orszag] += 1
        else:
            stat[v.orszag] = 1
    return stat

def orszag_mentes(fajlnev: str, orszag: str):
    fajl = open(fajlnev, 'w', encoding='utf8')

    for v in varosok_listaja:
        if v.orszag == orszag:
            fajl.write(f'{v.varos};{int(v.lakossag/1000)}\n')

    fajl.close()