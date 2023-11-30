from datetime import date


class Szoba:
    def __init__(self, nev, ar, szobaszam):
        self.nev = nev
        self.ar = ar
        self.szobaszam = szobaszam
        self.foglalasDatum = []


class EgyagyasSzoba(Szoba):
    def __init__(self, szobaszam):
        super().__init__("Egyágyas szoba", 100, szobaszam)
        self.klimavan = False


class KetagyasSzoba(Szoba):
    def __init__(self, szobaszam):
        super().__init__("Kétágyas szoba", 200, szobaszam)
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
        if date.today() < datum:
            for szoba in self.szobak:
                if isinstance(szoba, szobatipus):
                    if datum not in szoba.foglalasDatum:
                        szoba.foglalasDatum.append(datum)
                        return szoba.ar
        return None

    def lemondas(self, datum, szobaszam):
        for szoba in self.szobak:
            if szoba.szobaszam == szobaszam:
                if datum in szoba.foglalasDatum:
                    del szoba.foglalasDatum[szoba.foglalasDatum.index(datum)]
                    return True

    def listazas(self):
        for szoba in self.szobak:
            if szoba.foglalasDatum:
                for datum in szoba.foglalasDatum:
                    print(f"Szobaszám: {szoba.szobaszam} Típus: {szoba.nev} Dátum: {datum} Ár: {szoba.ar}")


szalloda = Szalloda("Hunguest Hotel")

szalloda.foglalas.szobahozzaad(EgyagyasSzoba(1))
szalloda.foglalas.szobahozzaad(KetagyasSzoba(2))
szalloda.foglalas.szobahozzaad(EgyagyasSzoba(3))

szalloda.foglalas.foglalas(date(2023, 12, 10), EgyagyasSzoba)
szalloda.foglalas.foglalas(date(2023, 12, 10), EgyagyasSzoba)
szalloda.foglalas.foglalas(date(2023, 12, 11), KetagyasSzoba)
szalloda.foglalas.foglalas(date(2023, 12, 12), EgyagyasSzoba)
szalloda.foglalas.foglalas(date(2023, 12, 13), EgyagyasSzoba)

szalloda.foglalas.listazas()
