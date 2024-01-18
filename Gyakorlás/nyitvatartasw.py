ido=-1
while ido!="":
    ido=-1
    while ido<0 or ido>23
        ido=input("Adja meg az idopontot")

    if ido>=8 and ido<16:
        print(f"A bolt nyitva van {16-ido} órád van még odaérni")
    else:
        print(f"A bolt zárva van")