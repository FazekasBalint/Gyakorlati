from tizproba import *

print(f'A versenyen {versenyzok_szama()} versenyző indult.')
print(f'{legalabb_darab(8600)} versenyző ért el legalább 8600 pontot.')
print(f'A versenyzők által elért pontszámok átlaga: {atlag_pontszam():.0f}')
# gyoztes = gyoztes_index()
# gyoztes = gyoztes_index2()
gyoztes = gyoztes()
print(f'A verseny győztese: {gyoztes[0]} {gyoztes[1]} pontos eredménnyel.')
versenyzo = input('Versenyző neve: ')
talalat = versenyzo_keres(versenyzo)
if talalat == False:
    print('\tA versenyző neve nem szerepel a listában.')
else:
    print(f'\tA versenyző pontszáma: {pontok[talalat]}')