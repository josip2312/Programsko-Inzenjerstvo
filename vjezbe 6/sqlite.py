import sqlite3
import ispit


class IspitiDB():
    def __init__(self, baza):
        self.conn = sqlite3.Connection(baza)
        self.cur = self.conn.cursor()
        self.cur.executescript("""
        DROP TABLE IF EXISTS ispiti;
        DROP TABLE IF EXISTS kolegiji;
        DROP TABLE IF EXISTS studenti;
        CREATE TABLE studenti (
        student_id integer PRIMARY KEY,
        ime_prezime text NOT NULL UNIQUE);
        CREATE TABLE kolegiji (
        kolegij_id integer PRIMARY KEY,
        naziv text NOT NULL UNIQUE);
        CREATE TABLE ispiti (
        student_id integer,
        kolegij_id integer,
        ocjena integer NOT NULL,
        PRIMARY KEY (student_id, kolegij_id),
        FOREIGN KEY (student_id) REFERENCES studenti (student_id),
        FOREIGN KEY (kolegij_id) REFERENCES kolegij (kolegij_id));
        """)

    def vrati_kolegij_id(self, naziv):
        self.cur.execute(
            """SELECT kolegij_id FROM kolegiji WHERE naziv = ?""", (naziv,))
        row = self.cur.fetchone()
        if row:
            return row[0]

    def dodaj_kolegij(self, naziv):
        self.cur.execute(
            """INSERT INTO kolegiji (naziv) VALUES (?)""", (naziv, ))
        self.conn.commit()
        return self.cur.lastrowid

    def vrati_student_id(self, ime_prezime):
        self.cur.execute(
            """SELECT student_id FROM studenti WHERE ime_prezime = ?""", (
                ime_prezime, )
        )
        row = self.cur.fetchone()
        if row:
            return row[0]

    def dodaj_student(self, ime_prezime):
        self.cur.execute(
            """INSERT INTO studenti (ime_prezime) VALUES(?)""", (ime_prezime, )
        )
        self.conn.commit()
        return self.cur.lastrowid

    def promijeni_student(self, ime_prezime, novo_ime_prezime):
        if(self.vrati_student_id(ime_prezime)):
            self.cur.execute("""UPDATE studenti SET ime_prezime = ? WHERE ime_prezime = ? """, (
                novo_ime_prezime, ime_prezime))
            self.conn.commit()
            return self.cur.lastrowid
        else:
            return None

    def izbrisi_student(self, ime_prezime):
        self.cur.execute(
            """DELETE FROM studenti WHERE ime_prezime = ?""", (ime_prezime, ))
        self.conn.commit()

    def ispitaj(self, student, kolegij, ocjena=None):
        student_id = None
        kolegij_id = None

        self.cur.execute(
            """SELECT student_id FROM studenti WHERE ime_prezime = ?""", (student,))
        id_s = self.cur.fetchone()
        if id_s:
            student_id = id_s[0]
        else:
            self.cur.execute(
                "INSERT INTO studenti (ime_prezime) VALUES (?) ", (student, ))
            self.conn.commit()
            self.cur.execute(
                """SELECT student_id FROM studenti WHERE ime_prezime = ?""", (student,))
            id_s = self.cur.fetchone()
            student_id = id_s[0]
            student_id = self.vrati_student_id(student)

        self.cur.execute(
            """SELECT kolegij_id FROM kolegiji WHERE naziv = ?""", (kolegij,))
        id_k = self.cur.fetchone()
        if id_k:
            kolegij_id = id_k[0]
        else:
            self.cur.execute(
                "INSERT INTO kolegiji (naziv) VALUES (?) ", (kolegij, ))
            self.conn.commit()
            kolegij_id = self.vrati_kolegij_id(kolegij)

        if student_id and kolegij_id:

            if ocjena:
                self.cur.execute(
                    """SELECT ocjena FROM ispiti WHERE student_id = ? and kolegij_id =? """, (student_id, kolegij_id))
                testOcjena = self.cur.fetchone()

                if testOcjena:
                    self.cur.execute(
                        "UPDATE ispiti SET ocjena = ? WHERE student_id = ? AND kolegij_id = ?", (ocjena, student_id, kolegij_id))
                    self.conn.commit()

                else:
                    self.cur.execute(
                        "INSERT INTO ispiti (ocjena, student_id,kolegij_id) VALUES (?,?,?)", (ocjena, student_id, kolegij_id))
                    self.conn.commit()

            else:
                self.cur.execute(
                    "DELETE FROM ispiti WHERE student_id = ? AND kolegij_id = ?", (student_id, kolegij_id))
                self.conn.commit()

    def svi_ispiti(self):

        self.cur.execute("""SELECT studenti.ime_prezime, kolegiji.naziv, ocjena FROM ispiti
                            JOIN studenti ON studenti.student_id=ispiti.student_id
                            JOIN kolegiji ON kolegiji.kolegij_id=ispiti.kolegij_id""")

        rows = self.cur.fetchall()
        return rows


''' print('*** TEST SQLite studenti ***')
db = IspitiDB("ispiti.sqlite")
print(db.cur.execute("SELECT * FROM studenti").fetchall())
db.dodaj_student("Ante Antić")
db.dodaj_student("Ana Anić")
db.dodaj_student("Pero Perić")
print(db.cur.execute("SELECT * FROM studenti").fetchall())
print(db.vrati_student_id("Pero Perić"))
print(db.vrati_student_id("Marija Marijić"))
db.izbrisi_student("Pero Perić")
db.promijeni_student("Ana Anić", "Marija Marijić")
print(db.cur.execute("SELECT * FROM studenti").fetchall())
db.ispitaj("Ante Antić", "Linearna algebra", 5)
 '''
print('*** TEST SQLite ispiti ***')
db = IspitiDB("ispiti.sqlite")
db.dodaj_student("Ante Antić")
db.dodaj_student("Marija Marijić")
db.dodaj_kolegij("Linearna algebra")
db.ispitaj("Ante Antić", "Linearna algebra", 5)
print(db.svi_ispiti())
db.ispitaj("Ante Antić", "Linearna algebra", 4)
print(db.svi_ispiti())
db.ispitaj("Ante Antić", "Linearna algebra")
print(db.svi_ispiti())
db.ispitaj("Ante Antić", "Linearna algebra", 5)
db.ispitaj("Marija Marijić", "Programiranje 1", 5)
db.ispitaj("Marija Marijić", "Matematička analiza", 4)
print(db.svi_ispiti())
