import random
import Kvadrat


class Polje:
    def __init__(self, velicina, broj_mina):
        self.__velicina = velicina
        self.__broj_mina = broj_mina
        self.generiraj(velicina, broj_mina)
        
    def generiraj(self, x, mine):
        cols_count = x
        rows_count = x
        self.__kvadrati = [
            [Kvadrat.Kvadrat() for i in range(cols_count)] for j in range(rows_count)]
        i = 0
        while(i < mine):
            row = random.randrange(0, 5)
            col = random.randrange(0, 5)

            self.__kvadrati[row][col] = Kvadrat.Kvadrat(-1)
            i += 1

        for i in range(x):
            for j in range(x):
                if(self.__kvadrati[i][j]).jeMina:
                    continue
                br_mina = 0

                for brojac in [-1, 0, 1]:
                    red1 = self.provjeriMine(i - 1, j + brojac)
                    red2 = self.provjeriMine(i, j + brojac)
                    red3 = self.provjeriMine(i + 1, j + brojac)

                    if (red1 == -1):
                        br_mina += 1
                    if (red2 == -1):
                        br_mina += 1
                    if (red3 == -1):
                        br_mina += 1

                self.__kvadrati[i][j] = Kvadrat.Kvadrat(br_mina)

        

    def provjeriMine(self, x, y):
        if (x >= 0 and y >= 0 and x < self.__velicina and y < self.__velicina):
            if self.__kvadrati[x][y].jeMina:
                return -1
            else:
                return 0

    def __str__(self):
        output = "   1 2 3 4 5\n  -----------"
        for i in range(self.__velicina):
            output += "\n" + str(i + 1) + "| "
            for j in range(self.__velicina):
                output += str(self.__kvadrati[i][j]) + " "
            output += "|"

        output += "\n  ----------"
        return output


print('*** test 1 ***')
print('*** rezultat varira zbog slucajnog izbora mina koristenjem random modula ***')
p = Polje(5, 2)
for red in p._Polje__kvadrati:
    for k in red:
        k.otkrij()
        print(k, end='|')
    print()
print('*** test 2 ***')
print('*** rezultat varira zbog slucajnog izbora mina koristenjem random modula ***')
p = Polje(5, 2)
for red in p._Polje__kvadrati:
    for k in red:
        k.otkrij()
print(p)
