from focivbk import *

beolvas('fociVBk.csv')
print(f'1. feladat: csapatok száma: {len(focivb_lista)}\n')
print(f'2. feladat: 2018-as VB csapatai:', end='')
csapatok = legutobbi_reszvetel("2018")
for index, cs in enumerate(csapatok):
    if index % 4 == 0:
        print()
        print('\t', end='')
    print(f'{str.ljust(cs, 20)}', end='')


print(f'\n3. feladat: A BeNelux országok összesen {benelux("Belgium", "Hollandia")} alkalommal vettek részt a VB-n\n')
print(f'4. feladat: Az első VB-t {elso_vilagbajnoksag()} rendezték\n')
print(f'5. feladat: Eddig {volt_vilagbajnok()} csapata volt világbajnok\n')
print(f'6. feladat: Szlovákia legjobb eredménye: {orszag_legjobb_eredmeny("Szlovákia").Legjobb_eredmény}\n')
ki_jutott_e = ki_e_jutott('Magyarország', 1930)
if ki_jutott_e == True:
    print(f'7. feladat: Magyarország ott volt az első VB-n.\n')
else:
    print(f'7. feladat: Magyarország nem volt ott az első VB-n.\n')
mentes('legtobbszor.txt')
print('8. feladat:  legtobbszor.txt kész!\n')