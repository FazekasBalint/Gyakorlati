print('LNKO kivonásos algoritmussal')
a = int(input('a = '))
b = int(input('b = '))

if a > b:
    nagyobb = a
    kisebb = b
else:
    nagyobb = b
    kisebb = a

while nagyobb != kisebb:
    nagyobb -= kisebb
    if nagyobb < kisebb:
        nagyobb,kisebb = kisebb,nagyobb

print(f'LNKO({a},{b}) = {nagyobb}')