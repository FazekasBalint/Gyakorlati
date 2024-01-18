from math import sqrt

print('1. feladat: Háromszög kerülete és területe')
print('Kérem a háromszög oldalait')

a = -1
while a <= 0:
    a = float(input('a = '))

b = -1
while b <= 0:
    b = float(input('b = '))

c = -1
while c <= 0:
    c = float(input('c = '))

if a + b <= c or a + c <= b or b + c <= a:
    print('A háromszög nem létezik.')
else:       
    K = a + b + c
    print(f'A háromszög kerülete = {K}')
    s = K / 2
    T =  sqrt(s*(s-a)*(s-b)*(s-c))
    print(f'A háromszög területe = {T}')