from tavolugras import print_egy_versenyzo, ugrasok_general, versenyzo_legjobb_ugrasa, gyoztes, ervenytelen_ugrasok_szama

eredmenyek = [] # minden versenyző legjobb eredmenye kerül bele

volt_legalabb_3_ervenytelen = False
for i in range(12):
    ugrasok = ugrasok_general()
    legjobb = versenyzo_legjobb_ugrasa(ugrasok)
    eredmenyek.append(legjobb)
    print_egy_versenyzo(i+1, ugrasok)
    if ervenytelen_ugrasok_szama(ugrasok) >= 3:
        volt_legalabb_3_ervenytelen = True

print(f'\nA győztes versenyző rajtszáma: {gyoztes(eredmenyek)}')

#Van-e olyan versenyző, akinek legalább 3 érvénytelen ugrása volt?
if volt_legalabb_3_ervenytelen:
    print('Van olyan versenyző, akinek legalább 3 érvénytelen ugrása volt.')
else:
    print('Nincs olyan versenyző, akinek legalább 3 érvénytelen ugrása volt.')
