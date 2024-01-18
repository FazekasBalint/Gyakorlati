fajl = open('gyumolcsok.txt','r', encoding='UTF8')

egysor = fajl.readline() # beolvas egy sort a fájlból és a fájl mutatót a következő sorra állítja
egysor = egysor.strip() # levágjuk a végéről az Entert
print(egysor)

kovetkezosor = fajl.readline().strip()
print(kovetkezosor)

fajl.close()

print('-----------------------------')

# Összes beolvasása
gyumolcsok = []
fajl = open('gyumolcsok.txt','r', encoding='UTF8')

for sor in fajl:
    gyumolcsok.append(sor.strip())

fajl.close()

print(gyumolcsok)

#A kettő módszer kombinálása
gyumolcsok.clear()
fajl = open('gyumolcsok_fejleccel.txt','r', encoding='UTF8')

# elso_sor = fajl.readline()
fajl.readline() # beolvassuk, de nem tároljuk, mert nincs rá szükségünk
for sor in fajl:
    gyumolcsok.append(sor.strip())

fajl.close()

print(gyumolcsok)