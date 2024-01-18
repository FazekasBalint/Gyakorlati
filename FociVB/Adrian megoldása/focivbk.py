from focivb import FociVb

focivb_lista : list[FociVb] = []

def beolvas(filename):
    file = open(filename, 'r', encoding='utf8')
    file.readline()
    for sor in file:
        focivb_lista.append(FociVb(sor.strip()))
    file.close()

def legutobbi_reszvetel(ev):
    csapatok = []
    for f in focivb_lista:
        if f.Legutóbbi_részvétel == ev:
            csapatok.append(f.Csapat)
    return csapatok

def benelux(orszag, orszag2):
    darab = 0
    for f in focivb_lista:
        if f.Csapat == orszag or f.Csapat == orszag2:
            darab += f.Részvételek_száma
    return darab

def elso_vilagbajnoksag():
    elso = 500000
    for f in focivb_lista:
        if f.Első_részvétel < elso:
            elso = f.Első_részvétel
    return elso

def volt_vilagbajnok():
    darab = 0
    for f in focivb_lista:
        if 'Világbajnok' in f.Legjobb_eredmény:
            darab += 1
    return darab

def orszag_legjobb_eredmeny(orszag):
    for f in focivb_lista:
        if f.Csapat == orszag:
            return f

def ki_e_jutott(orszag, ev):
    for f in focivb_lista:
        if f.Csapat == orszag and f.Első_részvétel == ev:
            return True
    return False

def mentes(filename):
    file = open(filename, 'w', encoding='utf8')
    for f in focivb_lista:
        if f.Részvételek_száma >= 10:
            file.write(f'{f.Csapat}: {2021 - f.Első_részvétel}\n')