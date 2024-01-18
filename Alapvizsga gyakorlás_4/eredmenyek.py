from eredmeny import eredmeny

eredmenyek:list[eredmeny]=[]

def beolvas(fajlnev:str):
    file=open(fajlnev,"r",encoding="utf-8")
    file.readline()
    for f in file:
        eredmenyek.append(eredmeny(f.strip()))

    file.close()

def celbaert(kategoria)->int:
    osszeg=0
    for e in eredmenyek:
        if e.kategoria==kategoria and e.tavszazalek==100:
            osszeg+=1
    return osszeg

def leghoszabb_nevu()->eredmeny:
    leghoszabb=eredmenyek[0]
    for e in eredmenyek:
        len(e.nev)>len(leghoszabb.nev)
        leghoszabb=e
    return leghoszabb

def atlagido(kategori)->float:
    darab=0
    osszeg=0
    for e in eredmenyek:
        if e.kategoria==kategori and e.tavszazalek==100:
            osszeg+=e.oraban
            darab+=1
    return osszeg/darab
