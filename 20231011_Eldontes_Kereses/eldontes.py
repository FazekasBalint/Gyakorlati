# Döntsük el, hogy van-e 13-mal osztható szám a listában!
# Válasz: igen/nem
# A keresést ne folytassa, ha a választ meg tudja adni!
from random import randint

szamok = [11, 26, 33, 12, 3]
# for i in range(100):
#     szamok.append(randint(-100,100))
print(szamok)


# Megoldás v1:
# Hivatalos algoritmus (minden prog. nyelven megvalósítható)
index = 0
while (index < len(szamok)) and (szamok[index] % 13 != 0):
# while feltétele: index kisebb mint az elemszám és az aktuális elem NEM felel meg a feltételnek
    index += 1
if index == len(szamok):
    print('Nincs 13-mal osztható elem a listában')
else:
    print('Van 13-mal osztható elem a listában')


# Megoldás v2:
# Python only
for szam in szamok:
    if szam % 13 == 0:
        print('Van 13-mal osztható elem a listában')
        break
else: # az else ágba akkor megy bele, ha a for ágban nem hajtódott végre break
    print('Nincs 13-mal osztható elem a listában')


# todo: Megoldás v3:
# saját függvény írásával és return használatával