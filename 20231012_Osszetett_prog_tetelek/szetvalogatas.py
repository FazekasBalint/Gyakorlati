# Válogassuk szét a páros és a páratlan számokat!

from random import randint

szamok = []

for i in range(20):
    szamok.append(randint(-100, 100))
print(szamok)

# szétválogatás
paros_szamok = []
paratlan_szamok = []
for szam in szamok:
    if szam % 2 == 0:
        paros_szamok.append(szam)
    else:
        paratlan_szamok.append(szam)
print('Páros számok: ', paros_szamok)
print('Páratlan számok: ', paratlan_szamok)