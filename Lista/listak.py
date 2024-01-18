# a = 111
# b = 21
# c = 23
# d = 13

# Lista: közös név alatt, sorszámmal indexelve tárolunk elemeket
szamok = [111, 21, 23, 13, 43]
szinek = ['piros', 'fehér', 'zöld']

#Lista elemeinek elérése:
print(szamok) # teljes lista kiíratása
print(*szinek, sep=' - ')


print(f'A lista 1-es indexű eleme: {szamok[1]}')

# A lista indexelés 0-val kezdődik!!!!!
print(f'A lista legelső eleme: {szamok[0]}')

# A lista utolsó eleme
print(f'A lista ultosó eleme: {szamok[-1]}')

# A lista elemszáma
print(f'{len(szamok)} darab elem van a listában.')
print(f'A lista ultosó eleme: {szamok[len(szamok)-1]}')

#Lista bejárása, ha szükségem va a ciklusban az indexekre is
for i in range(len(szamok)): # 5 elemű lista esetén: [0, 1, 2, 3, 4]-es tartományt kapunk
    print(f'A lista {i}. eleme: {szamok[i]}')

#Lista bejárása, ha csak az elemekre van szükség
for szam in szamok:
    print(szam)

for szin in szinek:
    print(szin)