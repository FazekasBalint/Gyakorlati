from varosok import *

beolvas('varosok.txt')
print(f'3. feladat: Városok száma: {varosok_szama()} db')
print(f'4. feladat: indiai nagyvárosok lakosságának összege: {orszag_lakossaga("India")} fő')
print(f'4.1 feladat: kínai nagyvárosok lakosságának összege: {orszag_lakossaga("Kína")} fő')
legnagyobb = legnagyobb_varos()
print('5. feladat: A legnagyobb város adatai: ')
print(f'\tNév: {legnagyobb.varos}')
print(f'\tOrszág: {legnagyobb.orszag}')
print(f'\tLakosság: {legnagyobb.lakossag}')

if orszag_keres('Magyarország'):
    print('6. feladat: Van magyar város adatok között.')
else:
    print('6. feladat: Nincs magyar város adatok között.')

print(f'7. feladat: Városok egy szóközzel: {szokozos_varosok_szama(1)} db.')
print(f'7.1 feladat: Városok kettő szóközzel: {szokozos_varosok_szama(2)} db.')
print(f'7.2 feladat: Egyszavas városok száma: {szokozos_varosok_szama(0)} db.')

print('8. feladat: Ország statisztika')
for key, value in orszag_statisztika().items():
    print(f'\t{key} - {value} db')

orszag_mentes('kina.txt', 'Kína')
