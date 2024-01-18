from mukorcsolya import atlag, versenyzo_osszes_pontszama, legrosszabb_pontszam, legjobb_ponszam, versenyzok_pontszama, gyoztes


for i in range(10):
    print(f'{i + 1}. versenyző: ')
    versenyzo_pontszamai = versenyzo_osszes_pontszama()
    print('\tA versenyző pontszáma: ', versenyzo_pontszamai)
    print(f'\tA legnagyobb pontszám: {legjobb_ponszam(versenyzo_pontszamai)}')
    print(f'\tA legkisebb pontszám: {legrosszabb_pontszam(versenyzo_pontszamai)}')
    versenyzok_pontszama.append(atlag(versenyzo_pontszamai))
    print(f'\tA versenyző összpontszáma: {versenyzok_pontszama[-1]}')

# print(versenyzok_pontszama)
print(f'\nA győztes versenyző rajtszáma: {gyoztes() + 1}')