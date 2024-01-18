# Mit kell tudni egy függvényről:
#   - mit csinál (függvény neve fontos)
#   - mi a paraméter listája (a függvény neve után zárójelben megadott, vesszővel elválasztott változó(k))
#       - formális paraméterek (a függvény daklarációjakor zárójelben megadott változók, amiket a fgv. kap)
#       - aktuális paraméterek (a függvény hívásakor, a fgv-nek átadott értékek (lehet: konstans, változó, kifejezés...))
#   - mit ad vissza (return kulcsszó után megadott érték)
#   - a függvény által visszaadott érték behelyetteítődik a fgv. helyére
#   - a függvény a meghívásakor fut le, deklarációkor csak létrejön
from random import randint

# def osszead(a, b): # a és b formális paraméterek. Ezeket a fgv-en belül lehet használni
def osszead(a: float, b: float) -> float:
    # print(a + b) #az eredmény nem kiírni szeretnénk, hanem visszaadni, ahogy egy randint() vagy egy sqrt() sem ír ki semmit
    return a + b 
    # ami a return mögött van az nem fut le
    print('You should never see this.')

# ezek mind valid kódok csak 'lógnak a levegőben', nincs semmi értelmük
osszead(2, 3) # 2 és 3 - aktuális paraméterek
randint(1, 10)
5
3
34.2
# input('adj meg egy számot: ')
'alma'

x = float(input('Első szám: '))
y = float(input('Második szám: '))
print(f'{x} + {y} = {osszead(x, y)}') # x és y - aktuális paraméterek