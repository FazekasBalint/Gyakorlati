from nevsor import osztalyletszam, leghosszabb_nev, atlag_hossz, van_e, tanulo_szamol, keres

# Hány ember van az osztályban?
print(f'Az osztályban {osztalyletszam()} fő van.')

# Ki a leghosszadbb nevű diák?
print(f'A leghosszabb nevű diák: {leghosszabb_nev()}')

# Átlagosan milyen hosszú egy név az osztályban?
print(f'Az osztályban a nevek átlagos hossza: {atlag_hossz()}')

# Van-e az osztályban József?
# Ha van akkor hány?
# Ha van akkor hányadik a névsorban?
keresett = input('Keresett tanuló neve: ')
if van_e(keresett):
    print(f'Van {keresett} az osztályban, {tanulo_szamol(keresett)} fő.')
    print(f'A névsorban az első {keresett} sorszáma: {keres(keresett)}')
else:
    print(f'Nincs {keresett} az osztályban.')


