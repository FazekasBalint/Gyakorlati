def sikeres(pontszam:int)->bool:
    return pontszam>48
while True:
    nev=input("Add meg a nevét: ")
    if nev=="":
        break
    pontszam=int(input("Add meg a pontszámát: "))

    if sikeres(pontszam):
        print(f"{nev} Sikeres")
    else:
        print(f"{nev} Vizsgaja sikertelen")