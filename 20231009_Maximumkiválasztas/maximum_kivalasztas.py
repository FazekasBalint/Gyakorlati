from random import randint
import math

szamok = []

for i in range(20):
    szamok.append(randint(-100,100))

print(szamok)

# 1. Melyik a legnagyobb szám?
legnagyobb = szamok[0]
# for szam in szamok: # van benne egy felesleges vizsgálat: az első elemet önmágával vizsgáljuk
for szam in szamok[1:]: # kihagyjuk a 0. elemet
    if szam > legnagyobb:
        legnagyobb = szam
print(f'A legnagyobb szám: {legnagyobb}')

# 2. Hányadik a legnagyobb szám? -> ebből megmondható az is hogy melyik az.
legnagyobb_indexe = 0 # feltesszük, hogy a 0. elem a legnagyobb
for i in range(1, len(szamok)): # a 0. elemet direkt kihagyjuk
    if szamok[i] > szamok[legnagyobb_indexe]:
        legnagyobb_indexe = i
print(f'A legnagyobb szám {szamok[legnagyobb_indexe]}, sorszáma: {legnagyobb_indexe + 1}')

# 3. Hányadik a legnagyobb páratlan szám?
legnagyobb_indexe = len(szamok) + 1 #olyan elemet kell belerakni, amelyiket biztosa felül fogjuk írni
#szamok[legnagyobb_indexe] # list index out of range
for i in range(len(szamok)):
    if szamok[i] % 2 == 1:
        # if legnagyobb_indexe == len(szamok) + 1: # az eredetileg belerakott rossz érték van benne
        #     legnagyobb_indexe = i
        # elif szamok[i] > szamok[legnagyobb_indexe]:
        #     legnagyobb_indexe = i
        if legnagyobb_indexe == len(szamok) + 1 or szamok[i] > szamok[legnagyobb_indexe]:
            legnagyobb_indexe = i
if legnagyobb_indexe == len(szamok) + 1:
    print('Nincs egyetlen páratlan szám sem.')
else:
    print(f'A legnagyobb páratlan szám {szamok[legnagyobb_indexe]}, sorszáma: {legnagyobb_indexe + 1}')

# 3. Hányadik a legnagyobb páratlan szám?
# megoldás v2:
# legnagyobb_ertek = -9999999999999999 #olyan elemet kell belerakni, amelyiket biztosa felül fogjuk írni
legnagyobb_ertek = -math.inf # végtelen
legnagyobb_indexe = False
for i in range(len(szamok)):
    if szamok[i] % 2 == 1 and szamok[i] > legnagyobb_ertek:
        legnagyobb_ertek = szamok[i]
        legnagyobb_indexe = i
if legnagyobb_indexe != False:
    print(f'A legnagyobb páratlan szám {legnagyobb_ertek}, sorszáma: {legnagyobb_indexe + 1}')
else:
    print('Nincs egyetlen páratlan szám sem.')
