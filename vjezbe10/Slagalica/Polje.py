class Polje:

    def __init__(self, broj):
        self.__broj = broj

    def vratiBroj(self):
        return self.__broj

    @property
    def jeBroj(self):
        if self.__broj == 0:
            return False
        else:
            return True

    @property
    def jePrazno(self):
        if self.__broj == 0:
            return True
        else:
            return False

    def __str__(self):
        if(self.__broj > 0):
            return str(self.__broj)
        else:
            return " "

    def __repr__(self):
        return f"Polje({self.__broj})"


''' print('*** test 1 ***')
brojevi = list(range(9))
for broj in brojevi:
    p = Polje(broj)
    print(p.vratiBroj(), p.jeBroj, p.jePrazno)

print('*** test 2 ***')
polja = [Polje(broj) for broj in range(9)]
for p in polja:
    print(repr(str(p)), repr(p))
 '''
