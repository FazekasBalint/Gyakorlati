from random import randint

def ez_prím(szam) -> bool:
    if szam == 2:
        return True
    for i in range(2, int(szam / 2)):
        if szam % i == 0:
            return False
    return True

szamok = []

for i in range(10):
    szamok.append(randint(10, 99))
print(szamok)

for szam in szamok:
    if ez_prím(szam):
        print('Van prímszám a lsitában.')
        break
else:
    print('Nincs prímszám a lsitában.')
