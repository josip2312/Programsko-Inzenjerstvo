import Polje as P


class PrikazIgre:

    def izaberiTezinu(self, tezine: list):
        while True:
            lista = []
            nums = []
            for i, num in enumerate(tezine, start=1):
                nums.append(i)
            print(f"Izaberi tezinu ({nums})")
            for i, tez in enumerate(tezine, start=1):
                lista.append(str(i))
                print(
                    f"{i }. Velicina {tez[0]}, broj mina {tez[1]}")
            tezina = input()

            if(tezina in lista):
                return tezina

    def prikaziPolje(self, polje):
        print(polje)

    def unesiAkciju(self, velicina):
        while True:
            operacija = ""
            koordinate = ""
            akcija = input(
                "Unesi akciju i koordinate (2 3) -> otkrivanje, (? 2 3) -> oznacavanje")
            if '?' in akcija:
                operacija = "oznaci"
                koordinate = akcija.replace("?", "").strip()
            else:
                operacija = "otkrij"
                koordinate = akcija
            if "," in akcija:
                koordinate = koordinate.split(",")
            else:
                koordinate = koordinate.split(" ")
            try:
                koordinate = [int(koordinate[0]), int(koordinate[1])]
            except:
                continue
            x = koordinate[0]
            y = koordinate[1]
            if((x > 0 and x <= velicina) and (x > 0 and y <= velicina)):
                return (operacija, x, y)


""" print('*** test 1 ***')
pi = PrikazIgre()

print(pi.izaberiTezinu([(9, 8), (15, 14), (20, 18), (30, 30)]))
 """
print('*** test 2 ***')
p = P.Polje(5, 2)

pi = PrikazIgre()

pi.prikaziPolje(p)

""" pi = PrikazIgre()
print(pi.unesiAkciju(9))
print(pi.unesiAkciju(3))
 """
