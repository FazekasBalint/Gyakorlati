def maganhagzok_szama(nap):
    maganhangzok = 'aáeéiíoóöőuúüű'
    darab = 0
    for n in nap:
        if n in maganhangzok:
            darab += 1
    return darab


napok: list[str] = ['hétfő', 'kedd', 'szerda', 'csütörtök', 'péntek']
# legnagyobb_indexe = 0
# for i, nap in enumerate(napok):
#     if maganhagzok_szama(nap) > maganhagzok_szama(napok[legnagyobb_indexe]):
#         legnagyobb_indexe = i
# print(f'A legtöbb magánhangzó a {napok[legnagyobb_indexe]}-ben van.')


legnagyobb = napok[0]
for nap in napok:
    if maganhagzok_szama(nap) > maganhagzok_szama(legnagyobb):
        legnagyobb = nap
print(f'A legtöbb magánhangzó a {legnagyobb}-ben van.')
