from auto import auto

'''
az_en_autom = auto # példányosítás
# az_en_autom - objektum, osztály példány
az_en_autom.rendszam = 'AA-AA-000'
az_en_autom.szin = 'piros'
az_en_autom.telejesitmeny = 123
az_en_autom.tipus = 'Skoda Octavia'

'''

# az_en_autom = auto('Skoda Octavia', 'AA-BB-123', 'piros', 123)
# print(az_en_autom.rendszam)

autok: list[auto] = [] # az autok egy olyan lista, amelyben auto osztály példányok vannak

egy_auto = auto('Skoda Octavia', 'AA-BB-123', 'piros', 123, 8.8)
autok.append(egy_auto)
egy_auto = auto('Skoda Fabia', 'AB-BB-123', 'fehér', 88, 10.2)
autok.append(egy_auto)
egy_auto = auto('Skoda Rapid', 'AC-BB-123', 'zöld', 178, 9.6)
autok.append(egy_auto)

# print(autok)

for egy_auto in autok:
    print(egy_auto.tipus, egy_auto.rendszam, egy_auto.szin, egy_auto.teljesitmeny, egy_auto.gyorsulas)

# legnagyobb teljesítményű autó
legnagyobb_teljesitmenyu_auto = autok[0]
for egy_auto in autok:
    if egy_auto.teljesitmeny > legnagyobb_teljesitmenyu_auto.teljesitmeny:
        legnagyobb_teljesitmenyu_auto = egy_auto

print('A legnegyobb teljesítményű autó:')
print(f'\tRendszáma: {legnagyobb_teljesitmenyu_auto.rendszam}')
print(f'\tTeljesítménye: {legnagyobb_teljesitmenyu_auto.teljesitmeny}')
print(f'\tSzíne: {legnagyobb_teljesitmenyu_auto.szin}')
print(f'\tTípusa: {legnagyobb_teljesitmenyu_auto.tipus}')

# keressünk egy adott rendszámot 
rendszam = input('Keresett rendszám: ')
for egy_auto in autok:
    if egy_auto.rendszam.upper() == rendszam.upper():
        print(f'\tA keresett autó típusa: {egy_auto.teljesitmeny}')
        print(f'\tA keresett autó színe: {egy_auto.szin}')
        print(f'\tA keresett autó teljesítménye: {egy_auto.teljesitmeny}')
        print(f'\tA keresett autó gyorsulása: {egy_auto.gyorsulas}')
        break
else:
    print('\tNincs ilyen rendszámú autó.')