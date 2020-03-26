from fractions import Fraction


class Razlomak:
    '''Klasa razlomak'''

    def __init__(self, brojnik, nazivnik=1):
        if nazivnik == 0:
            raise Exception("Nazivnik ne moze biti 0")
        self.__brojnik = brojnik
        self.__nazivnik = nazivnik

    def __str__(self):
        return f"{self.__brojnik}|{self.__nazivnik}"

    def inverz(self):
        return Razlomak(self.__nazivnik, self.__brojnik)

    @staticmethod
    def stvori(broj):
        ''' Pretvaram broj u listu odvojenu tockom,
        pomocu duljina_nazivnika znam koliko ce mi nazivnik
        imati nula
         '''
        brojnik_arr = str(broj).split(".")
        duljina_nazivnika = len("".join(brojnik_arr)) - 1
        if(brojnik_arr[0] == "0"):
            # ako imam iza decimalne tocke nule skidam ih
            brojnik_string = ("".join(brojnik_arr[1])).strip("0")
        else:
            brojnik_string = "".join(brojnik_arr)
            # smanjujem duljinu nazivnika ovisno o velicini broja prije decimale
            duljina_nazivnika = len("".join(brojnik_arr)) - len(brojnik_arr[0])

        nazivnik_str = "1" + "0" * duljina_nazivnika
        # pretvaram brojnik i nazivnik u integer iz stringa
        brojnik = int(brojnik_string)
        nazivnik = int(nazivnik_str)
        return Razlomak(brojnik, nazivnik)


print('*** test1 ***')
r1 = Razlomak(314, 100)
r2 = Razlomak.inverz(r1)
print(r1, r2, r1)

print('*** test2 ***')
r1 = Razlomak.stvori(3.14)
print(r1)
r2 = Razlomak.stvori(0.006021)
print(r2)
r3 = Razlomak.stvori(-75.204)
print(r3)
