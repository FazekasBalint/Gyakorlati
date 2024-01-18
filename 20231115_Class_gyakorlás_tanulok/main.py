from tanulok import *

tanulok_feltolt(10)

tanulok[0].jegy_beir(5)
tanulok[9].jegy_beir(1)

tanulok_kiir()

legjobb_tanulo = osztály_legjobbja()
print(f'A legjobb tanuló: {legjobb_tanulo.vezeteknev} {legjobb_tanulo.keresztnev}. Átlaga: {legjobb_tanulo.atlag()}')
print(f'{atlag_folott_letszam()} tanuló van az osztályátlag fölött.')