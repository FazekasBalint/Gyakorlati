# 12 versenyző
# Mindenki 6-ot ugrik
# Szimullajuk le a versenyt
# Ugrások 7 és 8.50 között legyenek, 30% hogy érvénytelen

# 1. versenyző ugrásai: 7.71, 7.81, érvénytelen, 8.01, érvénytelen, 7.66
# 1. versenyző legjobb ugrása: 8.01
# 2. versenyző ...

from random import randint

def ugrasok_general() -> list:
    ugrasok = []
    for i in range(6):
        egy_ugras = randint(700, 850) / 100
        if randint(1,10) <= 3: # 30%
            egy_ugras = 0
        ugrasok.append(egy_ugras)
    return ugrasok

def print_egy_versenyzo(rajtszam:int, ugrasok: list) -> None:
    print(f'{rajtszam}. versenyző ugrásai:', end=' ')
    for ugras in ugrasok:
        if ugras == 0:
            print('Érvénytelen', end=' ')
        else:
            print(ugras, end=' ')
    print(f'\n{rajtszam}. versenyző legjobb ugrása: {versenyzo_legjobb_ugrasa(ugrasok)}')

def versenyzo_legjobb_ugrasa(ugrasok: list) -> float:
    legjobb = ugrasok[0]
    for ugras in ugrasok[1:]:
        if ugras > legjobb:
            legjobb = ugras
    return legjobb

def gyoztes(eredmenyek: list) -> int:
    """
    Megkeresi és visszaadja a győztes versenyző rajtszámát.
    """
    legjobb = 0
    for i in range(len(eredmenyek)):
        if eredmenyek[i] > eredmenyek[legjobb]:
            legjobb = i
    return legjobb + 1

def ervenytelen_ugrasok_szama(ugrasok: list) -> int:
    darab = 0
    for ugras in ugrasok:
        if ugras == 0:
            darab += 1
    return darab