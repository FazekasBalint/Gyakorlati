def atvalt(hossz:int)->[]:
    ora=hossz//60 #73perc->73 // 60=>1
    perc=hossz%60 # 73%60=>13
    return[ora,perc]


for i in range(3):
    cim=input("Adj meg egy film címet: ")
    hossz=int(input("Hány perces a film?"))
    ido=atvalt(hossz)
    print(f"A {cim} cimu film {ido[0]} ora {[ido[1]]} perc hosszu")