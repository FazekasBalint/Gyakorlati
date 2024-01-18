from random import randint

darab = int(input('Hány szám kell? '))

szamok = []

for i in range(darab):
    szamok.append(randint(10, 99)) # a lista végére beleteszi az elemet

print(szamok)

# szamok.clear() # lista kiürítése
# print(szamok)

szamok.insert(0, 1) # az első paraméterben megadott helyre beszúrja a 2. paraméterben megadott elemet
print(szamok)

szam = szamok.pop() # a lista utolsó elemét kiveszi a listából és visszaadja
print(szam)
print(szamok)

szam = szamok.pop(0) # a lista 0. elemét kiveszi a listából és visszaadja
print(szam)
print(szamok)

torlendo = int(input('Mit szertene törölni? '))
szamok.remove(torlendo) # a megadott elem első előfordulását törli a listából
# ha nincs benne a listában az elem akkor hibaüzenetet kapunk
print(szamok)

szamok.sort() # listát helyben rendezi (növekvőben)
print(szamok)

szamok.sort(reverse=True) # listát helyben rendezi (csökkenőben)
print(szamok)

# masik_szamok = list((1, 2, 3, 4))
masik_szamok = [1, 2, 3, 4]
szamok.extend(masik_szamok) #szamok listához hozzáfűzi a másik_szamok listát
print(szamok)

meg_szamok = [9, 8, 7]
harmadik = masik_szamok + meg_szamok #listákon a + operátor összefűzi a két listát
print(harmadik)