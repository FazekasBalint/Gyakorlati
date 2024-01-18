#mennyi egy megadott feltételnek megfelelő számok összege, átlaga...?

from random import randint

# szamok = [randint(-100,100) for i in range(20)]

szamok = []
for i in range(20):
    szamok.append(randint(-100, 100))

print(szamok)

# mennyi a pozitív számok összege?
osszeg = 0
for szam in szamok:
    if szam > 0:
        osszeg += szam
print(f'A pozitív számok összege: {osszeg}.')

# mennyi a páros számok átlaga?
osszeg = 0
darab = 0
for szam in szamok:
    if szam % 2 == 0:
        osszeg += szam
        darab += 1
print(f'A páros számok átlaga: {osszeg/darab}.')
