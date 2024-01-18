from versenyzok import *

beolvas('Eredmenyek.txt')
print(f'2.feladat: A versenyt {versenyzok_szama()} versenyző fejezte be.')
print(f"3.feladat: Versenyzők száma: az 'elit junior' kategóriában: {elit_junior('elit junior')} fő")
print(f'4.feladat: Átlagéletkor: {atlag_eletkor():.1f} év')
kategoria = input('5.feladat: Kérek egy kategóriát: ')
if len((kategoria_keres(kategoria))) == 0:
    print('\tRajtszámok(ok): Nincs ilyen kategória!')    
else:
    print(f'\tRajtszámok(ok): {kategoria_keres(kategoria)}')

print(f'6. feladat: A legjobb időt {gyoztes("n").nev} érte el.')