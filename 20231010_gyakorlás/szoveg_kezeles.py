mondat = 'Lorem ipsum dolor sit amet consectetur adipisicing elit. Quibusdam necessitatibus fugiat iure dolorum dicta, delectus distinctio aperiam beatae eveniet fuga ab iusto minima sit labore asperiores eum placeat, praesentium tempora?'
rovid_mondat = 'Lorem ipsum dolor sit amet consectetur adipisicing.'

# Szöveg = karakterek listája

# Milyen hosszú a mondat?
print(f'A mondat {len(mondat)} karakterből áll.')

# Hány szóból áll a mondat? -> megszámoljuk a szóközöket
darab = 0
# for i in range(len(mondat)):
for karakter in mondat:
   if karakter == ' ' :
      darab += 1
print(f'A mondat {darab + 1} szóból áll.')

# Hány szóból áll a mondat? -> megszámoljuk a szóközöket
# megoldás v2
szavak = mondat.split()
print(f'A mondat {len(szavak)} szóból áll.')

# Hány olyan szó van a mondatban, amlyik legalább 10 karakter hosszú?
darab = 0
szo_hossza = 0

for karakter in rovid_mondat:
    if karakter != ' ':
      szo_hossza += 1
    else:
       if szo_hossza >= 10:
          darab += 1
       szo_hossza = 0
    # print(szo_hossza, end=' ')
if szo_hossza >= 10: # az utolsó szót is meg kell vizsgálni
    darab += 1
print(f'A mondatban {darab} darab legalább 10 karakter hosszú szó van.')

# Hány olyan szó van a mondatban, amlyik legalább 10 karakter hosszú?
# megoldás v2
szavak = rovid_mondat.split()
darab = 0
for szo in szavak:
    if len(szo) > 10:
        darab += 1
print(f'A mondatban {darab} darab legalább 10 karakter hosszú szó van.')


# Kérjünk be egy karaktert és mondjuk meg, hogy hány darab van belőle a mondatban!
darab = 0
input_karakter = input('Karakter: ')
for karakter in mondat:
    if karakter.lower() == input_karakter.lower(): # .lower() kisbetűssé konvertál
        darab += 1
print(f'{input_karakter} karakterek szám a mondatban: {darab}')

# Melyik karakterből mennyi van? (Karakter statisztika)

lehetseges_karakterek = 'qwertzuiopőúöüóasdfghjkléáűíyxcvbnm'
karakterek_szama = []

for lehetseges_karakter in lehetseges_karakterek:
    darab = 0
    for karakter in mondat:
        if karakter.lower() == lehetseges_karakter:
            darab += 1
    karakterek_szama.append(darab)
print(karakterek_szama)

print('Karakter statisztika')
for i in range(len(lehetseges_karakterek)):
    print(f'{lehetseges_karakterek[i]}: {karakterek_szama[i]}')


# Melyik karakterből van a legtöbb?
legtobb_indexe = 0
for i in range(1, len(karakterek_szama)):
    if karakterek_szama[i] > karakterek_szama[legtobb_indexe]:
        legtobb_indexe = i
print(f'{lehetseges_karakterek[legtobb_indexe]} karakterből van a legtöbb: {karakterek_szama[legtobb_indexe]} darab')