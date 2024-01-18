from random import randint, choice

nevek = []

file = open('osszesffi.txt','r',encoding='utf8')
for nev in file:
    nevek.append(nev.strip())
file.close()

# print(nevek)

file = open('tavolugras.txt', 'w', encoding='utf8')

for i in range(12):
    nev = choice(nevek)

    file.write(nev + ';')
    for j in range(6):
        ugras = randint(500, 800) / 100
        file.write(str(ugras))
        if j < 5:
            file.write(';')
        else:
            file.write('\n')


file.close()