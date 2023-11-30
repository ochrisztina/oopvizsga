class Szoba:
    def __init__(self, nev, ar, szobaszam):
        self.nev = nev
        self.ar = ar
        self.szobaszam = szobaszam
        self.foglalasDatum = []

class EgyagyasSzoba(Szoba):
    def __init__(self, szobaszam):
        super().__init__("Egy ágyas szoba", 100, szobaszam)
        self.klimavan = False

class KetagyasSzoba(Szoba):
    def __init__(self, szobaszam):
        super().__init__("Két ágyas szoba", 200, szobaszam)
        self.klimavan = True
        self.klimavan = True

class Szalloda:
    def __init__(self, nev):
        self.nev = nev
        self.foglalas = Foglalas()

class Foglalas:
    def __init__(self):
        self.szobak = []

    def szobahozzaad(self, szoba):
        self.szobak.append(szoba)

    def foglalas(self, datum, szobatipus):
        szoba.foglalasDatum.append()

    def lemondas(self, datum, szobaszam):
        for szoba in self.szobak:
            if szoba.szobaszam == szobaszam:
                if datum in szoba.foglalasDatum:
                    #szobafoglalas torlese
                    pass

    def listazas(self):
        for szoba in self.szobak:
            if szoba.foglalasDatum:
                for datum in szoba.foglalasDatum:
                    print(f"szobák listája")

