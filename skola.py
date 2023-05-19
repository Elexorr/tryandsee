class ziak:
    def vytvor_ziaka(self, a, b, c, d, e):
        self.meno = a
        self.priezvisko= b
        self.rok = c
        self.vyska = d
        self.rasa = e
    def porovnaj_vysku(self, dalsi):
        if self.vyska > dalsi.vyska:
            print(self.priezvisko, 'je vyssi ako', dalsi.priezvisko)
        elif self.vyska == dalsi.vyska:
            print(self.priezvisko, 'je rovnako vysoky ako', dalsi.priezvisko)
        elif self.vyska < dalsi.vyska:
            print(self.priezvisko, 'je nissi ako', dalsi.priezvisko)
