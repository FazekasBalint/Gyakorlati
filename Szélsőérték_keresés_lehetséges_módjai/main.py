from epuletek import *

betolt('legmagasabb.txt')
# print(len(epuletek))

print(f'A legmagassabb épület magassága: {legmagasabb()} méter.')

legmagasabb_epulet = legmagasabb_epulet()
print(f'A legmagassabb épület:')
print(f'\tneve: {legmagasabb_epulet.név}')
print(f'\tmagassága: {legmagasabb_epulet.magasság} méter')
print(f'\tépült: {legmagasabb_epulet.épült} év')
print(f'\tország: {legmagasabb_epulet.ország}')
print(f'\tváros: {legmagasabb_epulet.város}')


legmagasabb_epulet_index = legmagasabb_epulet_index()
print(f'A legmagassabb épület:')
print(f'\tneve: {epuletek[legmagasabb_epulet_index].név}')
print(f'\tmagassága: {epuletek[legmagasabb_epulet_index].magasság} méter')
print(f'\tépült: {epuletek[legmagasabb_epulet_index].épült} év')
print(f'\tország: {epuletek[legmagasabb_epulet_index].ország}')
print(f'\tváros: {epuletek[legmagasabb_epulet_index].város}')

print('Legmagasabb épletek:')
for l in legmagasabbak():
    print(f'\tneve: {l.név}')

print('A legmagasabb francia épület')
legmagasabb_francia = legmagasabb_epulet_adott_orszagban('Franciaország')
print(f'\tneve: {legmagasabb_francia.név}')
print(f'\tmagassága: {legmagasabb_francia.magasság} méter')
print(f'\tépült: {legmagasabb_francia.épült} év')
print(f'\tváros: {legmagasabb_francia.város}')