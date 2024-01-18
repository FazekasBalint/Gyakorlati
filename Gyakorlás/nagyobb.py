a=int(input("Adjon meg egy számot: "))
b=int(input("Adjon meg egy másik számot: "))

if a>b:
    print(f"{a} nagyobb mint a {b}")
elif b>a:
    print(f"{b} nagyobb mint a {a}")
else:
    print("A két szám egyenlő")
