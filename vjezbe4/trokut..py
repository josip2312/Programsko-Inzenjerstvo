import math


class nijeTrokutError(Exception):
    pass


class Trokut():
    def __init__(self, a, b, c):
        self.__stranice = []

        if (a >= 0 and b >= 0 and c >= 0) and (a + b > c and a + c > b and b + c > a):
            self.__a = a
            self.__b = b
            self.__c = c
            self.__stranice.append(a)
            self.__stranice.append(b)
            self.__stranice.append(c)
        else:
            raise Exception("Nije trokut")

    def __str__(self):
        return f"Trokut {self.__a}, {self.__b}, {self.__c}"

    def __repr__(self):
        return f"Trokut({self.__a}, {self.__b}, {self.__c})"

    def opseg(self):
        return self.__a + self.__b + self.__c

    def povrsina(self):
        s = self.opseg() / 2
        return math.sqrt((s - self.__a) * (s - self.__b) * (s - self.__c))


class JednakokracniTrokut(Trokut):
    def __init__(self, baza, krak):
        a = baza
        b = krak
        c = krak
        Trokut.__init__(self, a, b, c)


class JednakostranicniTrokut(Trokut):
    def __init__(self, baza):
        a = baza
        b = baza
        c = baza
        Trokut.__init__(self, a, b, c)


print('*** test 1 ***')
lista_stranica = [(1, 2, 3), (3, 4, 5), (3, 4, 4), (3, 3, 3)]
for stranice in lista_stranica:
    try:
        t = Trokut(*stranice)
        print(repr(t))
    except Exception as e:
        print(e, stranice)

print('*** test 2 ***')
lista_stranica = [(3, 4, 5), (3, 4, 4), (3, 3, 3)]
for stranice in lista_stranica:
    t = Trokut(*stranice)
    print('%r ima opseg %.3f i povrsinu %.3f' % (t, t.opseg(), t.povrsina()))

print('*** test 3 ***')
trokuti = [Trokut(3, 4, 5), JednakokracniTrokut(3, 4),
           JednakostranicniTrokut(5)]
for t in trokuti:
    print(t)
