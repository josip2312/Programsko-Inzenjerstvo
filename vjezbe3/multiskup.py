# Counter modul stvara rjecnik od liste sa elementima i brojem ponavljanja elementa
from collections import Counter


class MultiSkup:
    def __init__(self, skup=None):
        self.__skup = {}
        self.__skup_lista = []
        if skup is not None:
            for k, v in Counter(skup).items():
                self.__skup[k] = v
            self.update_list()

    # funkcija koja updatea listu ako dode do promjena
    def update_list(self):
        self.__skup_lista = []
        for k, v in self.__skup.items():
            for i in range(v):
                self.__skup_lista.append(k)

    def __str__(self):
        lista = []
        for k, v in self.__skup.items():
            if(v != 0):
                lista.append((f"{k} * {v}"))
        return str(lista)

    def __repr__(self):
        return f"Multiskup({self.__skup_lista})"

    def __iter__(self):
        return iter(self.__skup_lista)

    def add(self, key, value=1):
        self.__skup[key] += value
        self.update_list()

    def remove(self, key, value):
        self.__skup[key] -= value
        self.update_list()


print('*** test 1 ***')
a = MultiSkup([1, 1, 2, 2, 2, 3, 3, 4])
print(a)

print('*** test 2 ***')
a = MultiSkup([1, 1, 2, 2, 2, 3, 3, 4])
for el in a:
    print(el)
print(repr(a))

print('*** test 3 ***')
a = MultiSkup([1, 1, 2, 2, 2, 3, 3, 4])
a.add(4)
print(a)
a.add(2, 3)
print(a)
a.remove(4, 2)
print(a)
print(repr(a))
