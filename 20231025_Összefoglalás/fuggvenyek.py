from random import randint

def legnagyobb_elem(lista: list) -> int:
    """
    Visszaadja a lista legnagyobb elemét
    """
    legnagyobb = lista[0]
    for item in lista:
        if item > legnagyobb:
            legnagyobb = item
    return legnagyobb

def lista_feltolt(min: int, max:int , darab: int) -> list:
    """
    Felölt egy listát megadott darabszáámú min és max közé eső véletlen számmal.
    A feltöltött listát adja vissza.
    """
    lista = []
    for i in range(darab):
        lista.append(randint(min, max))

    return lista

def keres(keresett: int, lista: list) -> int|bool:
    """
    A paraméterben megadott elemet megkeresi a listában.
    Visszadja a keresett elem indexét. Ha nincs benne a keresett elem a listában, akkor False-t ad vissza.
    """
    for i in range(len(lista)) :
        if lista[i] == keresett:
            return i
    return False
    
def negativ_atlag(lista: list) -> float:
    darab = 0
    osszeg = 0
    for item in lista:
        if item < 0:
            darab += 1
            osszeg += item
    return osszeg / darab