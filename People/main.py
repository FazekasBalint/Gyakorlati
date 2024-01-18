from people import *

load_from_file('people.csv')
print(f'Emberek száma: {count_people()}')
print_people()

print(f'{people[0].last_name}({people[0].birthdate_str}) és {people[1].last_name}({people[1].birthdate_str}) korkülönbsége: {age_diff(people[0], people[1]).days} nap')