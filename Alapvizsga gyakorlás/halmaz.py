from random import randint

def halmaze(szamak: list[int]) -> bool:
    # halmaz = []
    # for sz in szamak:
    #     if sz not in halmaz:
    #         halmaz.append(sz)

    halmaz = set(szamak)

    if len(halmaz) == len(szamak):
        return True
    return False

print('2. feladat: halmaz-e?')

for j in range(8):
    szamok: list[int] = []
    for i in range(5):
        szamok.append(randint(0, 9))
    print(f'{j + 1}. {szamok}', end=' -> ')
    if halmaze(szamok):
        print('Halmaznak tekinthető.')
    else:
        print('Halmaznak nem tekinthető.')

