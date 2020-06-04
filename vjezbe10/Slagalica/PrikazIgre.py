import Ploca as P


class PrikazIgre:

    def izaberiVelicinu(self, velicine: list):
        while True:
            lista = []
            nums = []
            for i, num in enumerate(velicine, start=1):
                nums.append(i)
            print(f"Izaberi velicinu ({[i for i in nums]})")
            for i, vel in enumerate(velicine,  start=1):
                lista.append(str(i))
                print(
                    f"{i}. Velicina {vel[0]}, broj mina {vel[1]}")
            velicina = input()
            if(velicina in lista):
                return velicina

    def prikaziPlocu(self, ploca):
        print(ploca)

    def unesiPolje(self, broj_polja):
        while True:
            num = input("Unesi broj polja:")
            print('>>>', num)
            try:
                num = int(num)
            except:
                continue
            if num > 0 and num < broj_polja:
                return num


print('*** test 1 ***')
pi = PrikazIgre()
print(pi.izaberiVelicinu([(3, 3), (3, 4), (4, 4), (2, 2)]))


print('*** test 2 ***')
pl = P.Ploca(3, 3)
pl.postaviPolja([1, 2, 3, 4, 5, 6, 7, 8, 0])
pi = PrikazIgre()
pi.prikaziPlocu(pl)


print('*** test 3 ***')
pi = PrikazIgre()
print(pi.unesiPolje(9))
print('****')
print(pi.unesiPolje(3))
