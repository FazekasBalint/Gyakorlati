from fuggvenyek import lista_feltolt, legnagyobb_elem, keres, negativ_atlag

szamok = lista_feltolt(-100, 100, 20)
print(szamok)
print(f'A legnagyobb szám: {legnagyobb_elem(szamok)}')
keresett = int(input('Keresett szám: '))
kereses_eredmenye = keres(keresett, szamok)
if kereses_eredmenye == False:
    print('A keresett elem nincs benne a listában.')
else:
    print(f'A keresett elem sorszáma: {kereses_eredmenye + 1}')
print(f'A negatív számok átlaga: {negativ_atlag(szamok):.2f}')