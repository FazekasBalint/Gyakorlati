# from proba import szamok, a

# print(a)
# print(szamok)

from szamok_modul import szamok, feltolt, van_e_oszthato, atlag, keres, darab_ha_tobb

feltolt(10,1,100)
print(szamok)
oszto = int(input('Milyen osztót keresünk? '))
if van_e_oszthato(oszto):
    print(f'Van olyan szám a listában amely osztható ezzel: {oszto}.')
else:
    print(f'Nincs olyan szám a listában amely osztható ezzel: {oszto}.')


# szamok_atlaga = atlag()
# print(f'A listába szereplő számok átlaga: {szamok_atlaga}')
# ha később nem kell ez az érték sehol, akkor felesleges eltárolni
print(f'A listába szereplő számok átlaga: {atlag()}')


keresett_szam = int(input('Keresett szám: '))
kereses_eredmenye = keres(keresett_szam)
if kereses_eredmenye == False:
    print('A keresett szám nincs a listában.')
else:
    print(f'A keresett szám sorszáma: {kereses_eredmenye + 1}')


print(f'A számok között {darab_ha_tobb(50)} darab 50-nél nagyobb (vagy egyenlő) szám van.')