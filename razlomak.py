from fractions import Fraction
class Razlomak():

    def __init__(self, brojnik, nazivnik):
        self._brojnik = brojnik
        self._nazivnik = nazivnik

    @property
    def brojnik(self):
        return self._brojnik

    @property
    def nazivnik(self):
        return self._nazivnik

    @brojnik.setter
    def brojnik(self, value):
        self._brojnik = value

    @nazivnik.setter
    def nazivnik(self, value):
        self._nazivnik = value
    
    def skrati(self):
        return Fraction(self._brojnik,self._nazivnik)

    #Operatori usporedbe
    def __str__(self):
        return (f"Razlomak({str(self.brojnik)},{str(self.nazivnik)})")

    def __repr__(self):
        return (f"Razlomak {repr(self.brojnik)} | {repr(self.nazivnik)}")

    def __eq__(self, other):
        return self.skrati() == other.skrati()

    def __lt__(self, other):
        return self.skrati() < other.skrati()

    def __le__(self, other):
        return self.skrati() <= other.skrati()

    def __gt__(self, other):
        return self.skrati() > other.skrati()

    def __ge__(self, other):
        return self.skrati() >= other.skrati()

    #Aritmeticki operatori
    def __add__(self, other):
        return self.skrati() + other.skrati()

    def __sub__ (self,other):
        return self.skrati() - other.skrati()

    def __mul__ (self,other):
        return self.skrati() * other.skrati()
    def __truediv__(self,other):
        return self.skrati() / other.skrati()


r1 =  Razlomak(5,1)
r2 = Razlomak(2,1)
#Getting
print("Prvi razlomak")
print(f"Brojnik: {r1.brojnik} \nNazivnik: {r1.nazivnik}")
print("Drugi razlomak")
print(f"Brojnik: {r2.brojnik} \nNazivnik: {r2.nazivnik}")

#Setting
r1.brojnik = 50;
r1.nazivnik = 10;
r2.brojnik = 20;
r2.nazivnik = 10;
print("-----------------------------")
print("NAKON SETTANJA")

print("Prvi razlomak")
print(f"Brojnik: {r1.brojnik} \nNazivnik: {r1.nazivnik}")
print("Drugi razlomak")
print(f"Brojnik: {r2.brojnik} \nNazivnik: {r2.nazivnik}")
print("-----------------------------")

print("Skraceni razlomci i reprezentacije")
print(r1.skrati())
print(r2.skrati())

print(str(r1))
print(repr(r1))
print(str(r2))
print(repr(r2))

print("-----------------------------")

print("Rezultati usporedbi: ")
print(f"R1 vece ili jednako R2 : {r1 >= r2}")
print(f"R1 jednako R2: {r1 == r2}")
print(f"R1 manje ili jednako R2: {r1 <= r2}")
print(f"R1 manje od R2: {r1 < r2}")

print("Rezultati aritmetickih operacija: ")
print(f"R1 + R2 = {r1 + r2}")
print(f"R1 - R2 = {r1 - r2}")
print(f"R1 * R2 = {r1 * r2}")
print(f"R1 / R2 = {r1 / r2}")
