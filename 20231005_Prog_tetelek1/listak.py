fruits = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]

# lista[tol:ig] tol - inclusive, ig - exclusive
some_fruits = fruits[1:4] # az 1-es indexű elemetől a 4.-ig részlista (4-es már nincs benne)
some_fruits = fruits[3:] # a 3-as indexű elemtől az összes
some_fruits = fruits[:4] # az elejétől a 4-es indexű elemig (4-es már nincs benne)
some_fruits = fruits[-3:] # az utolsó 3 elem

# print(some_fruits)

fruit = input("Keresett gyümölcs: ")
if fruit in fruits:
    print('Van ilyen gyümölcs')
else:
    print('Nincs ilyen gyümölcs')

