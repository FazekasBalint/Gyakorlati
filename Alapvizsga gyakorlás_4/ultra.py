from eredmenyek import *

beolvas("ub2017egyeni.txt")

print(f"3.2 feladat: A futók száma: {len(eredmenyek)} db")

print(f"3.3 feladat: A célba érkező noi sportolok: {celbaert('Noi')} ")

print(f"3.4 feladat: A leghoszabb nevu futo:")
leghoszabb_nev=leghoszabb_nevu()
print(f"\t Név: {leghoszabb_nev.nev}")
print(f"\t Rajtszam: {leghoszabb_nev.rajtszam}")
print(f"\t Versenyidő: {leghoszabb_nev.versenyido}")

print(f"3.5feladat: Férfi sportolok atlagos ideje {atlagido('Ferfi')} óra")