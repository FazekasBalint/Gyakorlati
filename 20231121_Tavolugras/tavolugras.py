from Versenyzo import Versenyzo

versenyzok : list[Versenyzo] = []


def beolvas():
    file = open('tavolugras.txt','r',encoding='utf8')
    for sor in file:
        versenyzo = Versenyzo(sor.strip())
        versenyzok.append(versenyzo)

    file.close()