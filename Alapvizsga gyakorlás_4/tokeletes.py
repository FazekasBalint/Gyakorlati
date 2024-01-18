def tokeletese(szam)->bool:
    osszeg=0
    for i in range(1,szam):
        if szam%i==0:
            osszeg+=i
    return osszeg==szam



print("2.feladat:Tökéletes számok")
print("Kérek két természetes számot")
tol=int(input("tól:"))
ig=int(input("ig:"))


print(f"Tökéletes szamok {tol} és {ig} között")
volt_tokeletes=False
for i in range(tol,ig+1):
    if tokeletese(i):
        print(i,end="; ")
        volt_tokeletes=True
if not volt_tokeletes:
    print("A megadott tartomanyban nincsen tökéletes szám!")




