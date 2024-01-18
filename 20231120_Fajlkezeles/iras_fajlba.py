zoldseg = input('Adja meg a zöldség nevét: ')

# fajl = open('zoldsegek.txt','w',encoding='utf8') 
# írásra nyitja meg a fájlt. 
# Ha nem létezik akkor létrehozza.
# Ha létezik akkor felülírja.

fajl = open('zoldsegek.txt','a',encoding='utf8') # a = append - hozzáfűzés
# Ha nem létezik akkor létrehozza.
# Ha létezik, akkor a végéhez hozzáfűz.

fajl.write(zoldseg + '\n')

zoldsegek = ['hagyma', 'burgonya', 'paradicsom', 'zeller']
for z in zoldsegek:
    fajl.write(z + '\n')

fajl.close()