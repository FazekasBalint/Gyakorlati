# számoljuk meg, hogy hány elem felel meg egy adott feltételnek

from random import randint

szamok = []

for i in range(randint(10, 40)):
    szamok.append(randint(-100, 100))

print(szamok)

#hány elem van a listában?
print(f'{len(szamok)} darab szám került legenerálásra.')


#hány páros szám van a listában?
darab = 0
for szam in szamok:
    if szam % 2 == 0:
        darab += 1
print(f'{darab} páros szám van a számok között.')


#hány negatív szám van a listában?
darab = 0
for szam in szamok:
    if szam < 0: # csak a feltétel változik a kérdéstől függően
        darab += 1
print(f'{darab} negatív szám van a számok között.')
