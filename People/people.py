from person import Person
from datetime import datetime

people: list[Person] = []

def load_from_file(filename):
    file = open(filename, 'r', encoding='utf8')
    file.readline()
    for row in file:
        people.append(Person(row))

def count_people():
    return len(people)

def print_people():
    for p in people:
        # date = datetime.strptime(p.birthdate_str,"%Y-%m-%d") # str->date
        datestr = datetime.strftime(p.birthdate,"%Y.%m.%d") #date->str
        print(f'{p.first_name} {p.last_name} {datestr} ({p.age} éves)')

def age_diff(person1: Person, person2: Person):
    return person1.birthdate - person2.birthdate