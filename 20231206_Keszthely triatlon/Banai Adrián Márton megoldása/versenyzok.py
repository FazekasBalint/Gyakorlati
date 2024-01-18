
from versenyzo import Versenyzo
import math

versenyzok_listaja: list[Versenyzo] = []


def beolvas(filename):
    file = open(filename, 'r', encoding='utf8')
    for sor in file:
        versenyzok_listaja.append(Versenyzo(sor.strip()))
    file.close

def versenyzok_szama():
    return len(versenyzok_listaja)

def elit_junior(keresett):
    darab = 0
    for v in versenyzok_listaja:
        if v.kategoria == keresett:
            darab += 1
    return darab

def atlag_eletkor():
    osszeg = 0
    for v in versenyzok_listaja:
        eletkor = 2014 - v.szuletesi_ev
        osszeg += eletkor
    return osszeg / len(versenyzok_listaja)

def kategoria_keres(kategoria):
    kategoria_lista = []
    for v in versenyzok_listaja:
        if v.kategoria == kategoria:
            kategoria_lista.append(v.rajtszam)
    return kategoria_lista

def gyoztes(nem: str) -> Versenyzo:
    gyoztes_versenyzo_ideje = math.inf #infinity = végtelen
    gyoztes_versenyzo = None
    for v in versenyzok_listaja:
        if (v.nem == nem and v.osszido < gyoztes_versenyzo_ideje):
            gyoztes_versenyzo_ideje = v.osszido
            gyoztes_versenyzo = v
    return gyoztes_versenyzo