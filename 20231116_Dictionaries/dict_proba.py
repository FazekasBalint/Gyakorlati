szotar = {'alma': 'apple', 'szék': 'chair', 'ajtó': 'door', 'kék': 'blue'}

print(szotar)
print(szotar['kék'])

for szo in szotar.keys():
    print(szo)

for szo in szotar.values():
    print(szo)

for szo in szotar.items():
    print(szo)

#új elem hozzáadása
szotar['piros'] = 'red'

#ha olyan elemnek adok értéket amelyik már létezik, akkor felülírja
szotar['kék'] = 'navy'

#dictionary bejárása úgy, hogy key-value párokat kapunk
for key, value in szotar.items():
    print(f'{key} - {value}')

# Hiba: olyan indexre hivatkozok ami nem létezik
# print(szotar['zöld'])

#keresés a dict kulcsai között
keresett_szo = input('Keresett szó: ')
if keresett_szo in szotar.keys():
    print(f'{keresett_szo} - {szotar[keresett_szo]}')
else:
    print(f'A {keresett_szo} nincs benne a szótárban')
    if input('Szertené belerakni? (i/n): ') == 'i':
        jelentes = input('Jelentése: ')
        szotar[keresett_szo] = jelentes

print(szotar)

