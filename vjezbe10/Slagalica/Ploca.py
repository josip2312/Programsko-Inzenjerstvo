import random
import Polje


class Ploca:
    def __init__(self, broj_redova, broj_stupaca):
        self.__broj_redova = broj_redova
        self.__broj_stupaca = broj_stupaca

    def vratiVelicinuPloce(self):
        return (self.__broj_redova, self.__broj_stupaca)

    def vratiBrojPolja(self):
        return self.__broj_redova * self.__broj_stupaca

    def postaviPolja(self, brojevi):
        self.__polja = []
        len = 0

        for i in range(self.__broj_stupaca):
            new_row = []
            for j in range(self.__broj_redova):
                new_row.append(Polje.Polje(brojevi[len]))
                len += 1
            self.__polja.append(new_row)

    def __iter__(self):
        polja_lista = []
        print(self.__polja, "---")
        for i in self.__polja:
            for j in i:
                polja_lista.append(j)
        return iter(polja_lista)

    def __str__(self):
        text = ""
        d_ploce = 0
        for i in self.__polja:
            for j in i:
                if(d_ploce == self.__broj_stupaca):
                    text += f"{j}\n"
                    d_ploce = 0
                text += f"{j}\t"
                d_ploce += 1

        return text


print('*** test 1 ***')
broj_redova, broj_stupaca = 3, 3
pl = Ploca(broj_redova, broj_stupaca)
print(pl.vratiVelicinuPloce(), pl.vratiBrojPolja())
print()
pl.postaviPolja([0, 8, 7, 6, 5, 4, 3, 2, 1])
for red in pl._Ploca__polja:
    for p in red:
        print(p, end='|')
    print()

print('*** test 2 ***')
pl = Ploca(3, 4)
pl.postaviPolja([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 0])
print(pl)
for p in pl:
    print(p, repr(p))
