from helsinki import *

beolvas('helsinki.txt')
print(f'3.feladat:\nPontszerző helyezések száma: {pontszerzo_helyezesek_szama()}')
print('4. feladat:')
print(f'Arany: {helyezesek_szama(1)}')
print(f'Ezüst: {helyezesek_szama(2)}')
print(f'Branz: {helyezesek_szama(3)}')
print(f'Összesen: {helyezesek_szama(1) + helyezesek_szama(2) + helyezesek_szama(3)}')
print(f'5. feladat:\nOlimpiai pontok száma: {olimpiai_pontok_osszege()}')

uszas = ermek_szama('uszas')
torna = ermek_szama('torna')
print('6. feladat:')
if uszas == torna:
    print('Egyenlő volt az érmek száma.')
elif torna > uszas:
    print('Torna sportágban szereztek több érmet')
else:
    print('Úszás sportágban szereztek több érmet')

mentes('helsinki2.txt')

legtobb = legtobb_sportolo()
print('8. feladat:')
print(f'Helyezés: {legtobb.helyezes}')
print(f'Sportág: {legtobb.sportag}')
print(f'Versenyszám: {legtobb.versenyszam}')
print(f'Sportolók száma: {legtobb.sportolok_szama}')